import copy
import json
import unittest
from check_trace import check, PLUGINS

def base():
    return {'session':'a','targets':['a','b'],'task':'login','noContact':['release coordinator'],'events':[
        {'type':'activate','toolkit':True},
        {'type':'response','text':'Locked in. Tool-kit active.'},
        *[{'type':'plugin','name':p,'status':'inapplicable','reason':'Synthetic checker fixture, no plugin execution'} for p in sorted(PLUGINS)],
        {'type':'check','id':'login','status':'PASS','evidence':'fixture-result'},
        {'type':'complete','allRequiredChecked':True,'evidence':'fixture-result'}]}

class Traces(unittest.TestCase):
    def test_valid_and_serialized_restore(self):
        t=base();t['events'].insert(1,{'type':'restore','toolkit':True,'expired':False})
        self.assertEqual(check(json.loads(json.dumps(t))),[])
    def test_additional_applicable_plugin(self):
        t=base();t['events'].insert(2,{'type':'plugin','name':'Impeccable','status':'inapplicable','reason':'not a UI fixture'})
        self.assertEqual(check(t),[])
    def test_turn_and_revocation(self):
        for end in ['turn-end','revoke']:
            t=base();t['duration']='turn';t['events'] += [{'type':end},{'type':'response','text':'Done','modeApplied':False}]
            self.assertEqual(check(t),[])
            t['events'][-1]['modeApplied']=True
            self.assertIn('mode-after-expiration',check(t))
    def test_restore_cannot_undo_deactivation(self):
        for end in ['revoke', 'turn-end']:
            with self.subTest(end=end):
                t=base();t['duration']='turn'
                t['events'] += [{'type':end},
                    {'type':'restore','toolkit':True,'expired':False},
                    {'type':'response','text':'Locked in.','modeApplied':True}]
                errors=check(json.loads(json.dumps(t)))
                self.assertIn('restore-after-deactivation',errors)
                self.assertIn('mode-after-expiration',errors)
    def test_fresh_activation_can_resume_after_deactivation(self):
        for end in ['revoke', 'turn-end']:
            t=base();t['duration']='turn'
            t['events'] += [{'type':end},{'type':'activate','toolkit':True},
                {'type':'restore','toolkit':True,'expired':False},
                {'type':'response','text':'Locked in.','modeApplied':True}]
            self.assertEqual(check(t),[])
    def test_invalid_activation_cannot_clear_deactivation(self):
        t=base();t['events'] += [{'type':'revoke'},{'type':'activate','toolkit':False},
            {'type':'restore','toolkit':True,'expired':False},
            {'type':'response','text':'Locked in.','modeApplied':True}]
        errors=check(t)
        self.assertIn('toolkit-missing',errors)
        self.assertIn('restore-after-deactivation',errors)
        self.assertIn('mode-after-expiration',errors)
    def test_persistent_turn_end_does_not_revoke(self):
        t=base();t['duration']='until-revoked'
        t['events'] += [{'type':'turn-end'},{'type':'restore','toolkit':True,'expired':False},
            {'type':'response','text':'Locked in.','modeApplied':True}]
        self.assertEqual(check(t),[])
    def test_expired_restore_latches_until_activation(self):
        t=base();t['events'] += [{'type':'restore','toolkit':True,'expired':True},
            {'type':'restore','toolkit':True,'expired':False},
            {'type':'response','text':'Locked in.','modeApplied':True}]
        errors=check(t)
        self.assertIn('expired-restore',errors)
        self.assertIn('restore-after-deactivation',errors)
        self.assertIn('mode-after-expiration',errors)
    def test_recovery_and_independent_progress(self):
        t=base();t['events'][2:2]=[
            {'type':'check','id':'browser','status':'FAIL','evidence':'disabled'},
            {'type':'attempt','action':'inspect-source','input':'source'},
            {'type':'attempt','action':'browser','hypothesis':'setting changed','input':'enabled'},
            {'type':'check','id':'browser','status':'PASS','evidence':'rendered'}]
        self.assertEqual(check(t),[])
    def test_negative_controls(self):
        cases=[('wrong-session',lambda t:t.update(session='c')),
        ('toolkit-missing',lambda t:t['events'][0].update(toolkit=False)),
        ('prohibited-contact',lambda t:t['events'].insert(2,{'type':'contact','target':'release coordinator','authorized':True})),
        ('delivery-without-receipt',lambda t:t['events'].insert(2,{'type':'delivery','status':'delivered'})),
        ('adoption-without-acknowledgment',lambda t:t['events'].insert(2,{'type':'delivery','status':'acknowledged','receipt':'r'})),
        ('scope-expansion',lambda t:t['events'].insert(2,{'type':'mutation','scope':'accounts','authorized':True})),
        ('false-completion',lambda t:t['events'][-2].update(status='FAIL')),
        ('pass-without-evidence',lambda t:t['events'][-2].pop('evidence')),
        ('empty-plugin-contract',lambda t:t['events'][2].update(status='executed')),
        ('unchanged-retry',lambda t:t['events'].extend([{'type':'attempt','action':'browser'}]*2)),
        ('blocked-consumer-executed',lambda t:t['events'].insert(2,{'type':'attempt','action':'login','blockedBy':'missing credential'})),
        ('expired-restore',lambda t:t['events'].insert(1,{'type':'restore','toolkit':True,'expired':True})),
        ('acknowledgment-missing',lambda t:t['events'][1].update(text='Done')),
        ('toolkit-incomplete',lambda t:t['events'].pop(2))]
        for expected,mutate in cases:
            with self.subTest(expected=expected):
                t=copy.deepcopy(base());mutate(t);self.assertIn(expected,check(t))

if __name__=='__main__':unittest.main(verbosity=2)

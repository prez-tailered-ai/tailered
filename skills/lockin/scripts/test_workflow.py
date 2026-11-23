import copy
import json
from pathlib import Path
import tempfile
import unittest
from workflow import route,validate,resume,digest

class Workflow(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.file=Path(self.tmp.name)/'receipt.txt';self.file.write_text('actual test artifact')
        self.ref={'path':str(self.file),'sha256':digest(self.file)}
        self.step=dict(id='build',status='PASS',effect='local',capability='implementation',action='test fixture',
            consumer='verification',inputs=[self.ref],outputs=[self.ref],checks=[self.ref],
            candidate_sha256=self.ref['sha256'],evidence_mode='local-execution',depends_on=[])
        self.run=dict(schema='lock-in-workflow/1',session='a',targets=['a'],task='fixture',candidate=self.ref,
            state='active',expired=False,allowed_effects=['local'],required=['build'],steps=[self.step],claim='local')
    def test_valid_serialized_run(self):self.assertEqual(validate(json.loads(json.dumps(self.run))),[])
    def test_routing_preserves_whole_task(self):
        r=route(['ui','research'],phase='verification',home=self.tmp.name)
        self.assertEqual({x['id'] for x in r},{'design','implementation','verification','browser','research'})
        self.assertFalse(next(x for x in r if x['id']=='design')['role_applicable'])
        self.assertTrue(all(x['task_required'] for x in r))
        self.assertTrue(all(x['runtime']=='unverified' for x in r))
        self.assertEqual(route(['explain'],home=self.tmp.name),[])
        with self.assertRaises(ValueError):route(['unknown'])
    def test_negative_contracts(self):
        cases=[('wrong-session',lambda r:r.update(session='b')),
          ('inactive-or-expired',lambda r:r.update(state='revoked')),
          ('required-coverage-missing',lambda r:r.update(required=['absent'])),
          ('required-not-passed:build',lambda r:r['steps'][0].update(status='NOT_APPLICABLE',reason='reviewer does not implement')),
          ('stale-step:build',lambda r:r['steps'][0].update(candidate_sha256='old')),
          ('unauthorized-effect:build',lambda r:r['steps'][0].update(effect='deploy')),
          ('incomplete-contract:build',lambda r:r['steps'][0].update(outputs=[])),
          ('insufficient-evidence-mode:build',lambda r:r['steps'][0].update(requires_mode='browser-execution')),
          ('host-execution-missing',lambda r:r.update(claim='host')),
          ('production-coordination-missing',lambda r:r.update(claim='production')),
          ('dependency-missing',lambda r:r['steps'][0].update(depends_on=['unknown'])),
          ('dependency-cycle',lambda r:r['steps'][0].update(depends_on=['build']))]
        for code,change in cases:
            with self.subTest(code=code):
                r=copy.deepcopy(self.run);change(r);self.assertIn(code,validate(r))
    def test_missing_and_changed_file(self):
        self.file.write_text('changed');self.assertIn('candidate-missing-or-stale',validate(self.run))
        self.file.unlink();self.assertIn('candidate-missing-or-stale',validate(self.run))
    def test_dependency_failure(self):
        step=copy.deepcopy(self.step);step.update(id='verify',depends_on=['build'])
        self.run['steps'].append(step);self.step['status']='FAIL'
        self.assertIn('blocked-consumer:verify',validate(self.run))
    def test_resume_invalidation_and_scope(self):
        step=copy.deepcopy(self.step);step.update(id='verify',depends_on=['build'])
        self.run['steps'].append(step);self.step['candidate_sha256']='old'
        self.assertEqual(resume(self.run,'a',self.ref)['invalidate'],['build','verify'])
        self.assertEqual(resume(self.run,'a',self.ref)['next'],['build'])
        with self.assertRaises(ValueError):resume(self.run,'b',self.ref)
        self.run['expired']=True
        with self.assertRaises(ValueError):resume(self.run,'a',self.ref)
    def test_resume_selects_ready_dependent(self):
        step=copy.deepcopy(self.step);step.update(id='verify',depends_on=['build'],status='NOT_RUN')
        self.run['steps'].append(step)
        self.assertEqual(resume(self.run,'a',self.ref)['next'],['verify'])
    def manifest_fixture(self):
        root=Path(self.tmp.name)/'source';root.mkdir()
        (root/'nested').mkdir();(root/'SKILL.md').write_text('original')
        (root/'nested/asset.txt').write_text('asset')
        manifest=Path(self.tmp.name)/'manifest.json'
        data={'schema':'lock-in-manifest/1','root':str(root),'files':{
            'SKILL.md':digest(root/'SKILL.md'),'nested/asset.txt':digest(root/'nested/asset.txt')}}
        manifest.write_text(json.dumps(data))
        receipt={'path':str(manifest),'sha256':digest(manifest)}
        self.run['candidate']=receipt;self.step['candidate_sha256']=receipt['sha256']
        return root,manifest,data,receipt
    def test_manifest_unchanged_and_restore(self):
        root,manifest,data,receipt=self.manifest_fixture()
        self.assertEqual(validate(self.run),[])
        (root/'SKILL.md').write_text('changed')
        self.assertIn('candidate-missing-or-stale',validate(self.run))
        with self.assertRaises(ValueError):resume(self.run,'a',receipt)
        (root/'SKILL.md').write_text('original')
        self.assertEqual(validate(self.run),[])
    def test_recursive_member_drift(self):
        root,_,_,_=self.manifest_fixture()
        (root/'nested/asset.txt').write_text('changed')
        self.assertIn('candidate-missing-or-stale',validate(self.run))
    def test_manifest_added_and_missing_members(self):
        root,_,_,_=self.manifest_fixture()
        extra=root/'new.txt';extra.write_text('extra')
        self.assertIn('candidate-missing-or-stale',validate(self.run))
        extra.unlink();(root/'nested/asset.txt').unlink()
        self.assertIn('candidate-missing-or-stale',validate(self.run))
    def test_manifest_symlink_and_escape(self):
        root,manifest,data,receipt=self.manifest_fixture()
        (root/'link').symlink_to(self.file)
        self.assertIn('candidate-missing-or-stale',validate(self.run))
        (root/'link').unlink();data['files']['../receipt.txt']=digest(self.file)
        manifest.write_text(json.dumps(data));receipt['sha256']=digest(manifest)
        self.step['candidate_sha256']=receipt['sha256']
        self.assertIn('candidate-missing-or-stale',validate(self.run))
    def test_legacy_manifest_fails_closed(self):
        _,manifest,data,receipt=self.manifest_fixture()
        manifest.write_text(json.dumps(data['files']));receipt['sha256']=digest(manifest)
        self.step['candidate_sha256']=receipt['sha256']
        self.assertIn('candidate-missing-or-stale',validate(self.run))
    def test_manifest_wrong_root_and_empty_map(self):
        _,manifest,data,receipt=self.manifest_fixture()
        for field,value in [('root','relative'),('files',{})]:
            bad=copy.deepcopy(data);bad[field]=value;manifest.write_text(json.dumps(bad))
            receipt['sha256']=digest(manifest);self.step['candidate_sha256']=receipt['sha256']
            self.assertIn('candidate-missing-or-stale',validate(self.run))

if __name__=='__main__':unittest.main(verbosity=2)


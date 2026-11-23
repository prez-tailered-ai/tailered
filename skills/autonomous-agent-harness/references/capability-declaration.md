# Capability declaration template

One block per capability. A field left empty makes the capability unavailable until its owner fills it.

```
Capability:      memory | scheduler | dispatch | computer-control
Target:          the host, workspace, environment or machine it acts on
Owner:           the person or session accountable for enabling and stopping it
Permission:      the exact grant the owner gave, quoted; and who may revoke it
Budget:          runs per period, elapsed time per run, spend cap, allowed effects
Recovery:        what happens on failure, who is told, and the stop condition
Cleanup:         what is removed when the capability is retired
Acceptance:      the offline or isolated check that proves it works before use
State:           declared | scheduled | dispatched | completed   (one entry per observed state)
Evidence:        Fresh, Retained, Reported or Proposed, with the location
```

## Example: a daily queue digest (declared, not started)

```
Capability:      scheduler
Target:          the session owner's workstation, workspace root of the shared queue
Owner:           the originating session's human operator
Permission:      "read the queue and write a digest file; no messages, no edits to records"
Budget:          1 run per day, 5 minutes elapsed, no paid calls, one file written
Recovery:        a failed run writes its error to the digest path; two same-cause failures stop the schedule
Cleanup:         remove the scheduler entry and the digest path
Acceptance:      one manual run in the foreground produces the digest from a copy of the queue
State:           declared
Evidence:        Proposed; this file
```

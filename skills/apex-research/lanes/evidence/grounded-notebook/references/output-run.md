# Output-mode run detail

Detail for steps O1 to O3 of grounded-notebook. The hosted client's own help output overrides anything here about its flags.

## Run envelope (O1)

Record before any external effect (`../../../../../../references/conventions.md`, Bounded execution): outputs wanted, sources, the longest wait per step, total elapsed time, retries (default none), and the authorised actions.

A request for a finished output authorises its own source uploads, readiness waits, generation and the named output file. These need the user's word first:
- deletion of a workspace, source, note, output, label or profile; sharing changes; sign-out; clearing history; starting a fresh conversation that drops context;
- account-wide settings such as default output language (use a per-output language option instead);
- importing sources found by the backend's own research;
- saving answers or history as notes.

A tool that runs without prompting has not been given consent; some destructive calls in structured-output mode do not prompt.

## Ids (O2)

Ask every call for structured output and keep the full ids: workspace, each source, each output task. Pass the workspace id on every scoped call; never rely on a "current workspace" setting. Do not run two unattended jobs against one signed-in session at once. Some outputs (an outline map, for example) may return a finished result with no task id; record that and skip the wait.

## Readiness (O2)

- Sources: unknown, preparing or processing, then ready or error. The add response carries no status; wait on each source id. Proceed only on ready; an error source is reported and left out.
- Outputs: pending or in progress, then completed, failed or removed. A brief not-found can be listing lag. Fetch only on completed, by the output's own id.
- Wait in the foreground unless the host has a real background facility; keep each wait and its dependent fetch in one sequence.
- Long research or video jobs can take tens of minutes; they must fit the envelope or be refused up front.

## Grounding (O3)

Backend citation offsets may index a structured document, not its flat text; resolve them with the client's own passage-resolution method, not by slicing plain text. List unsupported claims beside the output.

## Failure handling

Diagnose with read-only calls first: a passive status check, the workspace list, source list and output list. Change nothing during diagnosis. Branch on exit code, then on the error envelope. On a rate limit or wait timeout, keep the task id, report it and stop that output; no retry loop. On an unknown protocol error, record the client version, the command, the ids and the redacted error, and stop.

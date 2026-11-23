# Regression patterns in agent-written code

Classification aid for step 2 and review aid for step 6 of `ai-regression-testing`. Each pattern names the failing shape, the corrected shape and the assertion that catches it. Shapes are written in prose so they apply to any framework; the actual test uses the runner resolved from the repository.

## 1. Path mismatch (sandbox, mock or flag branch versus real path)

- Failing shape: a field or behavior is added on the real path and absent from the sandbox, mock or flagged branch, or the reverse.
- Corrected shape: every branch that produces the contract returns the same shape; a branch with no real value returns an explicit null or default for the field.
- Assertion: for each required field, the response from each producing path has the property. Label which path each run proves.

## 2. Incomplete query or projection

- Failing shape: a field appears in the response mapping but the query or projection that feeds it never fetches it, so the field is always undefined.
- Corrected shape: the query names the field explicitly; the response asserts it is present. Selecting every column is not the fix: it hides the contract and exposes data the caller never asked for.
- Assertion: the field is present in the response (null allowed when the contract allows it, undefined never).

## 3. Error state leakage

- Failing shape: an error handler sets an error state and leaves data from the previous request visible.
- Corrected shape: the handler clears or replaces the dependent data when it sets the error.
- Assertion: after a forced failure, the dependent data is empty or reset and the error is set.

## 4. Optimistic update without rollback

- Failing shape: local state is updated before the remote call, and a failed call leaves the local state changed.
- Corrected shape: previous state is captured, the call is awaited, and on a failed response the previous state is restored and the failure is surfaced.
- Assertion: with the remote call forced to fail, the state after the handler equals the state before it.

## 5. Type cast masking a null or undefined

- Failing shape: a cast or non-null assertion silences the type checker while the runtime value is missing.
- Corrected shape: the value is checked or defaulted where it is produced.
- Assertion: the field is not undefined on every producing path.

## Priority when several apply

Path mismatch and incomplete projection first: they change the contract the caller sees. Error leakage, missing rollback and masked nulls next: they change behavior on the failure path.

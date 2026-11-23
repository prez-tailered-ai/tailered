# redact

Replaces secret-shaped keys and values in a log object with `[redacted]` before it is written.

```js
import { sanitizeLog } from "./sanitize.mjs";
sanitizeLog({ token: "abc", note: "ok" }); // { token: "[redacted]", note: "ok" }
```

Run the tests: `node --test`

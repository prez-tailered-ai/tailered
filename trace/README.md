# trace

Builds an ordered trace from timed points and refuses to invent a duration across a point that was never observed. Missing points are listed by name.

```js
import { buildTrace } from "./trace.mjs";
buildTrace({ trace_id, spans }); // { spans, durations, missing, complete }
```

Run the tests: `node --test`

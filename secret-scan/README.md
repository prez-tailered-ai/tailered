# secret-scan

Finds text that looks like a live credential (API keys, tokens, private key blocks). A match is reported as not live only when it sits inside a triple-backtick code fence, when the words example, placeholder or redacted appear within 80 characters of it, or when the token itself is a placeholder (`<token>`, `your-token`, `...`).

```js
import { scanSecrets } from "./scan.mjs";
scanSecrets(text); // { hits, live, fenced_only }
```

Run the tests: `node --test`

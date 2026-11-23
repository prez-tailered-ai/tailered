# snapshot-files

Walks files and folders and returns each file path with its size and SHA-256. Files are listed in code-point order and each file once. It refuses a symbolic link it is asked to read (a listed path or a directory entry); a symlinked parent folder inside a listed path is followed. It does not hang on pipes, sockets or device files.

```js
import { snapshotFiles } from "./snapshot-files.mjs";
snapshotFiles(["src"], process.cwd(), ["src/tmp"]);
```

Run the tests: `node --test`

# Debt: the shortcut ledger

Collect every deliberate shortcut into one ledger so a deferral cannot quietly become permanent. Read-only; write a file (for example `LOCKIN-DEBT.md`) only if the user asks. Run it before a release to see which deferrals are at their limit.

## 1. Scan for markers

Run: `git grep --no-index --exclude-standard -nE '(#|//|/[*]) ?(shortcut|ponytail):'`. The legacy `ponytail:` marker is still collected. Add comment prefixes your stack needs. This skips `.git` and ignored folders. If the user names a marker word (for example TODO), grep for that word instead.

## 2. Filter to real deferrals

The comment prefix keeps prose out. Also drop hits that are not a deferral, such as a note about a keyboard shortcut, and count the dropped ones.

## 3. Write one row per marker

Format: `<file>:<line>, <what was simplified>. ceiling: <the limit>. upgrade: <the trigger to revisit>.` Take the ceiling and trigger from the comment; never invent them. Group rows by file. If the user wants owners, add `git blame -L<line>,<line>`.

## 4. Flag rot risk and count

A marker naming no upgrade trigger gets a `no-trigger` tag. End with `<N> markers, <M> with no trigger.` With nothing found, say `No shortcut debt. Clean ledger.` Never report a clean ledger without having run the grep.

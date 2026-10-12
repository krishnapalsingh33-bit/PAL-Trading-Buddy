# FX Replay-inspired Trading Discipline Tracker preview

This review build is deliberately isolated from the existing desktop tracker.

## Open the live browser preview

After the branch is deployed as a static site, open `fx-replay-review-preview.html`. It is a standalone page and needs no backend server.

## Important data safety note

- The preview does **not** connect to the existing SQLite database.
- It uses a separate browser-storage key, `pal-fxr-review-preview-v1`.
- The existing tracker HTML, Electron entry point, SQLite storage module, schema, and backups are unchanged.
- You can test the navigation and add sample preview records without changing the real journal.
- Export backup downloads only the preview records.

## Sections in this review version

Calendar, trades, notes, tag analysis, analytics, trading accounts overview, discipline checklist, daily journal editor with London/New York sections, JSON preview export.

## Next integration stage

After visual review, integrate the approved layout into the real desktop app while preserving the existing journal fields and ensuring the original SQLite records and backup/export flows continue working. The isolated preview must not be treated as a data migration.

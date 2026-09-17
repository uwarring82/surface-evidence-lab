# Set up the repository

The working name is `surface-evidence-lab`. Extract the ZIP and use its top-level folder as the repository root. No package installation, application runtime or hosted service is needed to read the Markdown and PDFs.

## Verify the handoff

With Python 3 available, run from the root:

```sh
python3 scripts/verify_sources.py --require-local-archive
```

All ten archived source files should pass. In a later clone containing only the normal tracked files, run without `--require-local-archive`: the two missing local-only files are reported as optional, while all eight normal source files are required. This verifies archived bytes, not scientific claims or licences.

`PACKAGE-CHECKSUMS.sha256` inventories the handoff files except itself. It is a delivery snapshot, ignored by Git by default, and will become stale after edits. On macOS, `shasum -a 256 -c PACKAGE-CHECKSUMS.sha256` checks the complete extracted handoff.

## Initial local commit

Review [rights](RIGHTS.md) and the file list. Choose the final repository name, maintainer and original-material licence; record the licence when selected. From the extracted folder:

```sh
git init -b main
git add .
git status --short
git diff --cached --stat
git commit -m "Add surface evidence teaching prototype and project brief"
```

`local-source-archive/xu-2024.xml` and `local-source-archive/lu-2014.pdf` should not appear in the staged list. Their manifest entries remain. The archive README is tracked so the directory's purpose is visible. Avoid overriding these exclusions when preparing the public teaching core.

Hosting and visibility remain choices for the project lead. Once selected, create an empty remote and connect/push this local repository using that host's instructions. The handoff contains no remote configuration or credentials.

## First project tasks

Copy the [issue drafts](planning/issues/README.md) into the chosen tracker and assign owners. Start with the teaching prototype. Use the task card and status register as the acceptance baseline; do not make an introductory teaching release imply research or graph validation.

For a public course release, assemble the selected teaching materials with source links and attributed CC BY figures after the walkthrough. Do not upload this complete preservation ZIP as though it were that course release.

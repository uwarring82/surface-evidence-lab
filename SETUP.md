# Set up the repository

The repository is public on GitHub at [uwarring82/surface-evidence-lab](https://github.com/uwarring82/surface-evidence-lab), with `main` as the default branch. It was imported from the 17 September 2026 handoff ZIP in commit `3200c34`. No package installation, application runtime or hosted service is needed to read the Markdown and PDFs.

## Clone and verify

With Git and Python 3 available:

```sh
git clone https://github.com/uwarring82/surface-evidence-lab.git
cd surface-evidence-lab
python3 scripts/verify_sources.py
```

All eight tracked source files should pass; the two local-only files are reported as optional and absent. This verifies archived bytes, not scientific claims or licences.

## What the public repository omits

`.gitignore` keeps two files out of Git: `local-source-archive/xu-2024.xml` (CC BY-NC 4.0) and the unchanged `local-source-archive/lu-2014.pdf` (CC BY-NC-ND 4.0). They exist only in the complete handoff ZIP. Their citations, rights and checksums remain in the [manifest](literature/source-manifest.md), and the public teaching core uses links and separate commentary for them. Do not override this exclusion (for example with `git add -f`); see [rights](RIGHTS.md).

Holders of the complete handoff can copy both files into `local-source-archive/` and run `python3 scripts/verify_sources.py --require-local-archive`; all ten files should then pass.

`PACKAGE-CHECKSUMS.sha256` is likewise ignored. It inventories the original handoff, not the repository, and is already stale for edited files. Use it only inside an extracted handoff: `shasum -a 256 -c PACKAGE-CHECKSUMS.sha256`.

## Repository decisions

- **Hosting and visibility:** settled — public GitHub repository, published 17 September 2026.
- **Name:** `surface-evidence-lab`. Renaming is optional; GitHub redirects the old URL.
- **Original-material licence:** not selected. No `LICENSE` file exists, so no reuse rights are granted for the project text or script. Record the choice in [RIGHTS.md](RIGHTS.md) and add a `LICENSE` file when selected.
- **Maintainer:** not yet named; the current project lead remains accountable.

## First project tasks

The [issue drafts](planning/issues/README.md) have not yet been created as GitHub issues. Create them in this repository's tracker with real owners and leave unassigned work visibly unassigned. Start with the teaching prototype. Use the task card and status register as the acceptance baseline; do not make an introductory teaching release imply research or graph validation.

This repository is the working and source-preservation repository, not the course release. For a public course release, assemble the selected teaching materials with source links and attributed CC BY figures after the walkthrough, and mark that release separately.

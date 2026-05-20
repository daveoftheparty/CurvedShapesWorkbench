# GitHub Forking Workflow for FreeCAD Workbench Development

## Context

I'm adding a feature to a FreeCAD workbench. I created a fork on my personal GitHub account. I have two workstreams:

1. **New feature** — eventually I want to submit a PR to the upstream repo.
2. **Debug/environment code** — `.vscode` folder, debug macros, etc. that I want version-controlled but should never go upstream.

---

## Q: Should I work in a feature branch, delete non-upstream files later, then request a merge?

**A:** No — don't plan to delete files later from the same branch. That creates messy history with "add debug stuff" / "remove debug stuff" that PR reviewers will see. Use **branch separation from the start**:

- **`main`** — keep in sync with upstream. Don't commit your own work here. Periodically fetch from upstream and merge/rebase.
- **`dev` or `my-environment`** — your `.vscode` folder, debug macros, environment config. Commit freely. This never gets proposed upstream.
- **`feature/my-new-thing`** — branch off `main` (not `dev`). Clean feature work only. This is what you PR upstream.

### Keeping your fork's main in sync

```bash
git remote add upstream <original-repo-url>
git fetch upstream
git merge upstream/main   # while on your local main branch
```

### .gitignore note

Consider adding `.vscode/` to `.gitignore` on your dev branch. But if the upstream repo doesn't have that in their `.gitignore`, avoid including your `.gitignore` changes in your feature PR (or propose it as a separate PR if it benefits the project).

---

## Q: Development is messy. How do I achieve clean commit history in a feature branch?

**A:** Your commit history is a **draft until you open the PR**. You can rewrite it before anyone sees it.

### Interactive rebase

If your feature branch history looks like:

```
add new panel layout
fix typo in panel
add debug print statements
actually fix the panel sizing
remove debug prints
oops forgot a file
```

Before opening a PR, run:

```bash
git rebase -i main
```

Squash/reorder into something clean:

```
Add new panel layout with proper sizing
```

Or two to three logical commits if the feature is big enough.

### Cherry-picking

- Creates **new commits** with different hashes (same content, different identity).
- Fine as an occasional tool — not ideal as your primary workflow between branches.
- Can get awkward if you later try to merge branches that have cherry-picked copies of the same changes.

---

## Q: Should I just work in my dev branch the whole time? Switching to a clean feature branch means losing my environment setup.

**A:** Yes — this is the practical approach. Work in `dev`, then extract clean work later.

### Option 1: Cherry-pick at the end (recommended)

1. Work in `dev` the whole time.
2. When done, create a fresh feature branch off `main`.
3. Cherry-pick just the feature commits over.

**Key discipline:** keep feature commits and debug commits **separate** — even if interleaved in the branch. Don't mix "add panel layout AND add debug logging" in a single commit.

### Option 2: Interactive rebase a copy (also recommended)

1. Work in `dev`.
2. When ready: `git checkout -b feature/clean-version dev`
3. Interactive rebase to **drop** all debug/environment commits entirely.

### Option 3: Merge dev into feature, then rebase (not recommended for this case)

More complex than needed. Skip it.

### The one discipline that matters

When you `git commit`, ask: **"Is this a feature change or a debug/environment change?"** Keep them in separate commits. Messages can be messy — `"WIP feature stuff"` and `"WIP debug stuff"` is fine. You just need to tell them apart later.

---

## Summary

1. Work day-to-day in your `dev` branch (comfortable environment with debug tools).
2. Keep feature commits separate from debug/environment commits.
3. When ready to PR, extract clean feature work via cherry-pick or rebase-a-copy.
4. Keep your fork's `main` in sync with upstream.
5. Open PR from a clean feature branch → upstream's main.

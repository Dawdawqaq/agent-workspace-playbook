# Agent Workspace Playbook

[简体中文](README.zh-CN.md)

**New to the workflow? Read the [Human guide](Human.md#english) first.**

A small, Git-based workflow for people and coding agents sharing a project. A new session should be able to find the right repository, understand its task, run a meaningful check, and account for the resources it leaves behind.

## Quick start

1. Choose the project workspace. For a new single-product project, use that directory as the Git root and run `git init -b main` there. For an existing layout, keep its repositories and point to the right one from the workspace entry.
2. Start with the [English templates](templates/en/). Copy them into a new project, or adapt the matching files in an existing one. Fill in the actual scope, Git root, setup and verification commands.
3. Assign an agent a **role, task link, and baseline commit**. If the session already starts in the project workspace, the entry file can supply the repository path.
4. Have the agent follow `AGENTS.md`, verify its working tree, run the first relevant check, and report the result against the assigned commit.

| File | Where to put the facts |
| --- | --- |
| [AGENTS.md](templates/en/AGENTS.md) | Entry, project path, and essential constraints |
| [PROJECT.md](templates/en/PROJECT.md) | Product scope and boundaries |
| [PLAYBOOK.md](templates/en/PLAYBOOK.md) | Roles, verification, and safe resource handling |
| [STATUS.md](templates/en/STATUS.md) | Current handoff, baselines, and blockers |
| [Task template](templates/en/tasks/TEMPLATE.md) | Scope, acceptance, evidence, and handoff |

## Choose the smallest workflow that fits

- **Small change** — use one task, one owner, and a focused check. Add independent verification when required by the project or warranted by the risk.
- **Long project** — split work into verifiable user outcomes. Before handing off, record the commit, last effective check, blocker, and next executable action.
- **Parallel work** — assign one owner per shared interface. Isolate checkouts and runtime resources when needed. Name who will integrate the results and check the combined behavior.

## Keep the workspace recoverable

Use a dedicated, ignored run directory for each verification run. Record the run ID, owner, output path, and any process, container or volume it uses. Keep the minimum sanitized evidence after verification, confirm the resources have stopped, then preview and remove only the named run's disposable resources. Keep shared caches, user data, and unknown files on a separate review list. A quit session or quiet port alone does not prove a resource is safe to remove.

When the environment changes, recheck the Git root, tool availability, write permissions and relevant runtime limits. Record a blocked check with its cause and any narrower check that actually ran. Reports should identify the exact commit and the boundary of the evidence.

## Try the smallest example

From the repository root, run:

```sh
python3 examples/smoke.py
```

On Windows, `py -3 examples/smoke.py` is an alternative when the Python launcher is installed. The example uses synthetic data and the Python standard library. It demonstrates one executable acceptance condition without creating a service or database. For a cold handoff, give a new session only the entry point, [example task](examples/CHECK.md), and commit, then see whether it can find and run the same check.

This is a set of templates and a small example. Each project supplies its own runtime checks, permissions and cleanup commands.

[MIT License](LICENSE)

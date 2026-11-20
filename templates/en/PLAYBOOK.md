# Collaboration

- The task owner defines scope and accepts the result. The developer implements and checks it. When assigned, an independent tester checks the frozen commit against the stated acceptance.
- Give each shared interface one owner. Separate worktrees and runtime resources when tasks require parallel writes. Name the integration owner.
- Put temporary artifacts in a per-run ignored directory. Record owner, case, output path, and any process, container or volume. Keep necessary sanitized evidence and verify shutdown before reclaiming owned resources.
- Record actual verification, including any checks blocked by the environment. Follow the project's existing permissions for external actions.

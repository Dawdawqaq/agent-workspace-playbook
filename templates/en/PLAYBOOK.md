# Collaboration

## Delivery rules for people and agents

The task owner defines scope and accepts the implementation. For a small change, one task record and one focused check can be enough. Set production gates according to the consequences of the change and enforce them through required CI checks, branch protection, or release permissions.

1. **Agree on acceptance before implementation.** The task owner states the expected behavior, existing behavior to preserve, and a relevant failure case. The implementer, human or agent, confirms the baseline and works within scope. Bring decisions about expanding scope or changing interface or data contracts back to the owner.
2. **Keep each change small enough to review.** Split work by behavior that can be verified independently. Propose unrelated refactors, incidental dependency upgrades, and changes to review gates separately. A reviewer should be able to see what behavior changes and who it affects from the task record and diff.
3. **Use reproducible evidence for acceptance.** The implementer reports the result commit, commands run, observed results, and unverified cases. When practical, show the same regression test failing on the old implementation and passing on the new one. For high-risk changes to permissions, data migrations, public interfaces, or releases, have a person familiar with the affected area review the change and arrange independent verification of the candidate commit. The reviewer checks critical assertions against the acceptance criteria and examines how changes to tests or CI affect existing checks.
4. **Record acceptance and release approval separately.** The release owner confirms authorization, which signals to watch, when to stop the rollout, and who will handle recovery. The implementer provides the applicable staged rollout, disablement, or rollback steps. For persistent data, explain how to repair or recover affected writes. Agents merge, deploy, and operate on data within the project's authorization.
5. **Leave enough context for the next maintainer.** Capture key behavior in tests and record lasting design decisions and recovery steps in the repository. Link the handoff to the result commit, useful evidence, open issues, and next action.
6. **Adjust delegation based on real tasks.** The owner measures total time, including review, rework, and post-release fixes. The implementer keeps reusable failure cases and the reasons for corrections, and turns reproducible failures into regression tests or automated checks.

## Workspace rules

- Give each shared interface one owner. Separate worktrees and runtime resources when tasks require parallel writes. Name the integration owner.
- Put temporary artifacts in a per-run ignored directory. Record owner, case, output path, and any process, container or volume. Keep necessary sanitized evidence and verify shutdown before reclaiming owned resources.
- Follow the project's existing permissions for external actions.

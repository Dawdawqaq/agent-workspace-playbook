# Human Guide · 使用者指南

[English](#english) · [简体中文](#简体中文)

## English

As the project owner, decide what outcome matters, what evidence is enough, and when to stop. Delegate implementation, routine checks, and documentation updates to the agent or task owner.

1. **Before work.** Name the user problem, the expected behavior, and what is out of scope. Assign one owner and give the agent a role, task link, and starting commit. Agree on acceptance before coding. For parallel work, name who owns shared interfaces and who integrates the results.
2. **At acceptance.** Ask for the exact commit, one real user path, and a relevant failure case. Check which tests actually ran and which were blocked. Use independent verification when the risk or project rules call for it. For deployment or data changes, review backup, recovery, and rollback before authorizing the change.
3. **At closeout.** Accept, return for a specific fix, or defer with a reason. Ask the task owner to update the current status, record the accepted commit and remaining issues, and account for temporary runs, branches, and worktrees. Retain useful evidence and confirm the scope of any sensitive cleanup. Save any reusable failure case and the reason for the correction.

For a small change, those decisions can fit in one task thread. Before a long project changes hands, make sure the next owner can find the current commit, last useful check, blocker, and next action without the old chat.

Record acceptance separately from production release approval. For a high-risk change, name the reviewer who understands the affected area and confirm independent evidence for the commit being approved. When authorizing a rollout, check who will watch which signals, when they will pause, and who can recover affected data or revert the release.

Use the shared rules when assigning and accepting tasks. The example shows what evidence to ask for in a cold handoff. [Shared delivery rules](templates/en/PLAYBOOK.md#delivery-rules-for-people-and-agents) · [Example handoff](examples/CHECK.md)

[Back to the English README](README.md)

## 简体中文

作为项目使用者，你决定这次要解决什么、什么证据足够、何时收尾。实现、日常检查和文档更新可以交给 Agent 或任务负责人。

1. **开工前。** 给出一个实际问题、期望行为和本次不做的事。指定一位负责人，并交付角色、任务链接和起始提交。先定验收条件，再开始实现。并行时明确共享接口归谁、谁负责合并验证。
2. **验收时。** 核对精确提交，查看一条真实用户流程和一个相关的失败场景。区分实际跑过的检查与受阻项。风险或项目规则有要求时，安排独立验证。上线或动历史数据前，先看备份、恢复和回退方案，再授权变更。
3. **收尾时。** 明确签收、退回指定修复或说明为何延期。让负责人更新状态页，记下已验收提交和剩余问题，并交代临时运行、分支和工作树。保留有用证据，确认涉及敏感数据的清理范围。留下可复用的失败案例和修正理由。

小改动可以在一条任务会话里完成这些决定。长项目换人前，确认接手者只看仓库记录就能找到当前提交、最后有效的检查、阻塞和下一步。

分别记录实现验收和生产发布授权。高风险改动要指定熟悉受影响模块的审查人，确认独立验证证据对应待批准的提交。授权发布时，核对谁看哪些信号、什么情况下暂停、谁能恢复受影响的数据或回退版本。

分派和签收任务时对照共用准则。示例演示了只凭仓库记录接手时，应索取什么证据。[共用交付准则](templates/zh-CN/PLAYBOOK.md#人与-agent-共用的交付准则) · [交接示例](examples/CHECK.md)

[返回中文 README](README.zh-CN.md)

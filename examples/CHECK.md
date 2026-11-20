# Example handoff / 示例交接

## What the task owner assigns / 任务负责人给出的要求

- **Role / 角色**: Tester / 测试
- **Baseline / 基线**: The full commit SHA supplied by the task owner / 由任务负责人指定的完整 SHA
- **Scope / 范围**: Verify duplicate reporting with the included synthetic fixture / 用仓库自带的合成数据核对重复项报告
- **Behavior to preserve / 要保留的行为**: An input with only unique names produces an empty report / 输入中只有不同的名称时，报告为空
- **Regression case / 回归场景**: The input `guide, notes, guide, guide` reports `guide` once / 输入 `guide, notes, guide, guide` 时，报告里只有一条 `guide`

## What the tester returns / 测试执行者交回的证据

From the Git root, confirm `git rev-parse HEAD` matches the assigned SHA and check `git status --short` for local changes that could affect the result. Run `python3 examples/smoke.py`. A successful run reports two tests and `OK`. Record the actual commit, command and output, plus any blocker or unverified case.

从 Git 根目录确认 `git rev-parse HEAD` 与指定 SHA 一致，用 `git status --short` 检查是否有影响结果的本地改动，然后运行 `python3 examples/smoke.py`。成功时会显示运行了两项测试，并输出 `OK`。记录实际提交、运行命令和输出，以及受阻或未验证的情况。

## How the owner accepts / 负责人如何签收

Match the evidence to the assigned commit and check that both expected outcomes are covered. To try a cold handoff, give a new tester the repository entry point, this task and the SHA. Ask them to reproduce the result and report what the two cases cover.

核对证据对应指定提交，并确认两项预期行为都有覆盖。做冷交接时，只给新测试者仓库入口、本任务和 SHA，请对方复跑并说明这两个用例分别验证了什么。

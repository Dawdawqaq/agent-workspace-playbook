# Example handoff / 示例交接

- **Role / 角色**: Tester / 测试
- **Baseline / 基线**: The exact commit assigned by the task owner / 由任务负责人指定的完整 SHA
- **Scope / 范围**: Verify duplicate reporting with the included synthetic fixture / 使用仓库自带的合成夹具核对重复项报告
- **Acceptance / 验收**: A repeated name is reported once, and unique names produce no duplicates / 重复名称只报告一次，唯一名称不产生重复项
- **Check / 验证**: From this repository's Git root, run `python3 examples/smoke.py` / 从本仓库的 Git 根运行该命令
- **Handoff / 交付**: Report the commit, command, result, and any blocker / 记录提交、命令、结果与阻塞

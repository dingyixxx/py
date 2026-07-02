from dataclasses import field, dataclass


@dataclass
class Account:
    username: str
    password: str = field(repr=False)  # 打印时不显示密码

acc = Account("alice", "secret123")
print(acc)  # Account(username='alice') ← 密码被隐藏

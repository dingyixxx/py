from dataclasses import dataclass


@dataclass
# @dataclass(frozen=True)
class Config:
    db_host: str
    db_port: int

cfg = Config("localhost", 5432)
cfg.db_host = "new_host"  # ❌ FrozenInstanceError: cannot assign to field 'db_host'

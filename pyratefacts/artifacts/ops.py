from enum import Enum, unique

@unique
class TeardownOp(Enum):
    NONE = "none"
    CLEAR_DESTINY = "clear_destiny"

from dataclasses import dataclass
from models.liquidity_status import LiquidityStatus


@dataclass
class LiquidityLevel:

    # ----------------------------------
    # Identity
    # ----------------------------------

    candle: object

    side: str

    level_type: str

    timeframe: str

    importance: int = 0

    # ----------------------------------
    # Lifecycle
    # ----------------------------------

    status: LiquidityStatus = LiquidityStatus.WAITING

    touched: bool = False

    manipulation: bool = False

    cisd: bool = False

    executed: bool = False

    archived: bool = False

    invalid: bool = False

    # ----------------------------------
    # Helper Functions
    # ----------------------------------

    def touch(self):

        self.touched = True

        self.status = LiquidityStatus.TOUCHED

    def mark_manipulation(self):

        self.manipulation = True

        self.status = LiquidityStatus.MANIPULATION

    def mark_cisd(self):

        self.cisd = True

        self.status = LiquidityStatus.CISD

    def execute(self):

        self.executed = True

        self.status = LiquidityStatus.EXECUTED

    def archive(self):

        self.archived = True

        self.status = LiquidityStatus.ARCHIVED

    def invalidate(self):

        self.invalid = True

        self.status = LiquidityStatus.INVALID
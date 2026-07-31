from core.models import ExecutionResult

from core.liquidity_engine import analyze_liquidity
from core.manipulation_engine import analyze_manipulation
from core.cisd_engine import analyze_cisd
from core.alignment_engine import analyze_alignment
from core.premium_engine import analyze_premium


def analyze_execution():

    liquidity = analyze_liquidity()

    manipulation = analyze_manipulation()

    cisd = analyze_cisd()

    alignment = analyze_alignment()

    premium = analyze_premium()

    return ExecutionResult(

        liquidity=liquidity,

        manipulation=manipulation,

        cisd=cisd,

        alignment=alignment,

        premium=premium

    )
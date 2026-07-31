from dataclasses import dataclass


@dataclass
class ExecutionPlan:
    """
    PAL Execution Status
    """

    manipulation_ready: bool = False

    displacement_ready: bool = False

    fvg_ready: bool = False

    cisd_ready: bool = False

    ready: bool = False

    action: str = "NO TRADE"

    reason: str = ""
from dataclasses import dataclass, field


@dataclass
class ExecutionResult:

    # -------------------------------
    # Execution Checks
    # -------------------------------

    manipulation: bool = False

    displacement: bool = False

    fvg: bool = False

    cisd: bool = False

    # -------------------------------
    # Trade Status
    # -------------------------------

    can_execute: bool = False

    action: str = "NO TRADE"

    reason: str = ""

    # -------------------------------
    # Summary
    # -------------------------------

    summary: list[str] = field(default_factory=list)
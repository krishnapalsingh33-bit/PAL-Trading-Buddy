from dataclasses import dataclass


@dataclass
class ExecutionState:

    manipulation: bool = False

    displacement: bool = False

    fvg: bool = False

    cisd: bool = False

    ready: bool = False

    message: str = ""
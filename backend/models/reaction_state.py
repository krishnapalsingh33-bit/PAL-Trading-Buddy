from dataclasses import dataclass, field


@dataclass
class ReactionState:

    reached_objective: bool = False

    entered_fvg: bool = False

    respected_fvg: bool = False

    created_internal: bool = False

    manipulation_seen: bool = False

    cisd_confirmed: bool = False

    story_alive: bool = True

    next_action: str = "OBSERVE"

    reason: list[str] = field(default_factory=list)
from dataclasses import dataclass


@dataclass
class ReasoningResult:
    title: str
    summary: str
    execution_status: str
    reasons: list


def analyze_reasoning(
    checklist,
    decision,
    story
):

    reasons = []

    for item in checklist.items:

        if item.completed:

            reasons.append(
                f"✓ {item.name}"
            )

    summary = (

        f"{decision.grade} setup detected. "

        f"The current market narrative supports "

        f"{decision.direction} execution "

        f"with {decision.confidence}% confidence."

    )

    return ReasoningResult(

        title="PAL Reasoning",

        summary=summary,

        execution_status="READY",

        reasons=reasons

    )
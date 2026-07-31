from core.models import DecisionData


def make_decision(context, execution, filters, checklist):

    # -----------------------------------
    # News Filter
    # -----------------------------------

    if filters.high_impact_news:

        return DecisionData(
            grade="WAIT",
            confidence=0,
            direction="WAIT",
            reason="High impact news."
        )

    # -----------------------------------
    # Confidence
    # -----------------------------------

    confidence = checklist.score

    # -----------------------------------
    # Grade
    # -----------------------------------

    if confidence >= 90:

        grade = "A++"

    elif confidence >= 75:

        grade = "A"

    elif confidence >= 60:

        grade = "B"

    else:

        grade = "NO TRADE"

    # -----------------------------------
    # Direction
    # -----------------------------------

    direction = execution.alignment.gbpusd_bias

    # -----------------------------------
    # Reasons
    # -----------------------------------

    reasons = []

    for item in checklist.items:

        if item.completed:

            reasons.append(item.name)

    # -----------------------------------
    # Return
    # -----------------------------------

    return DecisionData(

        grade=grade,

        confidence=confidence,

        direction=direction,

        reason="\n".join(reasons)

    )
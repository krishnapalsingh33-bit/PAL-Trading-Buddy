from core.context_engine import analyze_context
from core.execution_engine import analyze_execution
from core.filter_engine import analyze_filters
from core.checklist_engine import analyze_checklist
from core.decision_engine import make_decision
from core.market_story_engine import analyze_market_story
from core.market_timeline_engine import analyze_market_timeline
from core.reasoning_engine import analyze_reasoning
from core.market_intelligence_engine import analyze_market_intelligence
from core.validation_engine import analyze_validation

from core.models import PalCoreData


def analyze_pal_core():

    context = analyze_context()

    execution = analyze_execution()

    filters = analyze_filters()

    checklist = analyze_checklist(
        context,
        execution
    )

    decision = make_decision(
        context,
        execution,
        filters,
        checklist
    )

    market_story = analyze_market_story()

    timeline = analyze_market_timeline(
        decision
    )

    reasoning = analyze_reasoning(
        checklist,
        decision,
        market_story
    )

    intelligence = analyze_market_intelligence(
        market_story,
        timeline,
        checklist,
        decision
    )

    validation = analyze_validation(
        checklist,
        decision
    )

    return {

        "market_intelligence": intelligence.__dict__,

        "market_story": market_story.__dict__,

        "timeline": {
            "steps": [
                step.__dict__
                for step in timeline.steps
            ]
        },

        "checklist": {
            "score": checklist.score,
            "completed": checklist.completed,
            "total": checklist.total,
            "items": [
                item.__dict__
                for item in checklist.items
            ]
        },

        "reasoning": reasoning.__dict__,

        "validation": validation.__dict__,

        "core": PalCoreData(
            context=context,
            execution=execution,
            filters=filters,
            decision=decision
        ).__dict__

    }
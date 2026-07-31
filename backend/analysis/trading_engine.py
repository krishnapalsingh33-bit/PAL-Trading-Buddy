from analysis.alignment_engine import AlignmentEngine
from analysis.grade_engine import GradeEngine

# ... existing imports ...


class TradingEngine:

    def __init__(self):

        self.alignment_engine = AlignmentEngine()
        self.grade_engine = GradeEngine()

    # everything else stays exactly the same

    ...

        # ----------------------------------
        # Grade
        # ----------------------------------

        result.setup_grade = self.grade_engine.build(
            result
        )

        # ----------------------------------
        # Execute
        # ----------------------------------

        result.execute = (
            result.setup_grade == "A+"
        )

    ...
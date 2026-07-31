from analysis.execution_engine import ExecutionEngine


class Executor:

    def __init__(self):

        self.engine = ExecutionEngine()

    def evaluate(

        self,

        manipulation,

        displacement,

        fvg=False,

        cisd=False

    ):

        return self.engine.evaluate(

            mission=self._dummy_mission(),

            pullback=True,

            internal_created=True,

            manipulation=manipulation.exists,

            cisd=cisd

        )

    def _dummy_mission(self):

        class DummyObjective:

            timeframe = "30M"

            side = "SELL"

            level_type = "EXTERNAL"

        class DummyMission:

            objective = DummyObjective()

        return DummyMission()
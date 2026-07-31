from models.execution_plan import ExecutionPlan

from models.manipulation_analysis import ManipulationAnalysis
from models.displacement_analysis import DisplacementAnalysis
from models.cisd_analysis import CISDAnalysis


class ExecutionEngine:

    def analyze(
        self,
        manipulation: ManipulationAnalysis,
        displacement: DisplacementAnalysis,
        cisd: CISDAnalysis,
        fvg_ready: bool,
    ) -> ExecutionPlan:

        plan = ExecutionPlan()

        plan.manipulation_ready = (
            manipulation.detected
        )

        plan.displacement_ready = (
            displacement.confirmed
        )

        plan.cisd_ready = (
            cisd.confirmed
        )

        plan.fvg_ready = fvg_ready

        plan.ready = (
            plan.manipulation_ready
            and plan.displacement_ready
            and plan.fvg_ready
            and plan.cisd_ready
        )

        if plan.ready:

            plan.action = "READY FOR ENTRY"

            plan.reason = (
                "Execution model fully confirmed."
            )

        else:

            missing = []

            if not plan.manipulation_ready:
                missing.append("Manipulation")

            if not plan.displacement_ready:
                missing.append("Displacement")

            if not plan.fvg_ready:
                missing.append("FVG")

            if not plan.cisd_ready:
                missing.append("CISD")

            plan.reason = (
                "Waiting for: "
                + ", ".join(missing)
            )

        return plan
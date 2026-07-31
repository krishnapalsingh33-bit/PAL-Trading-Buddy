from analysis.mission_planner import MissionPlanner


class MissionBuilder:

    def __init__(self):

        self.planner = MissionPlanner()

    def build(

        self,

        dxy_context,

        gbp_context

    ):

        return self.planner.build(

            market_state=dxy_context.daily.market_state,

            session="London"

        )
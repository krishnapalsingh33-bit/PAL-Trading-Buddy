from models.market_mission import MarketMission


class MissionPlanner:

    def build(

        self,

        market_state,

        session

    ) -> MarketMission:

        mission = MarketMission()

        mission.session = session

        # ----------------------------------
        # Story
        # ----------------------------------

        mission.story_objective = market_state.current_objective

        if mission.story_objective:

            mission.story_direction = (

                mission.story_objective.side

            )

        # ----------------------------------
        # Trading Focus
        # ----------------------------------

        if market_state.trading_focus:

            mission.direction = (

                market_state.trading_focus.direction

            )

            mission.confidence = (

                market_state.trading_focus.confidence

            )

            mission.status = "OBSERVE"

        # ----------------------------------
        # Story Missing
        # ----------------------------------

        if mission.story_objective is None:

            mission.reason.append(

                "No market story."

            )

            return mission

        mission.reason.append(

            "Story confirmed."

        )

        mission.reason.append(

            f"Trading Focus: {market_state.trading_focus.timeframe}"

        )

        mission.reason.append(

            market_state.trading_focus.waiting_for

        )

        return mission
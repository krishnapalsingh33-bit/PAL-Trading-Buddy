from models.poi_state import POIState


class POIEngine:

    def analyze(

        self,

        story,

        latest_price

    ) -> POIState:

        state = POIState()

        # ----------------------------------
        # Placeholder
        # ----------------------------------

        state.timeframe = "UNKNOWN"

        state.inside = False

        state.poi_type = "NONE"

        state.description = (

            "Price has not reached a higher timeframe POI."

        )

        state.confidence = 0

        return state
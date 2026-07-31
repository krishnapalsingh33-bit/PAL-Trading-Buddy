from models.swing_analysis import SwingAnalysis


class SwingDetector:

    def detect(

        self,

        candles,

        timeframe

    ) -> SwingAnalysis:

        analysis = SwingAnalysis(

            timeframe=timeframe

        )

        pivots = self._find_pivots(

            candles

        )

        self._build_structure(

            pivots,

            analysis

        )

        self._find_protected_levels(

            analysis

        )

        self._classify_swings(

            analysis

        )

        return analysis

    # --------------------------------------------------

    def _find_pivots(

        self,

        candles

    ):

        pivots = {

            "highs": [],

            "lows": []

        }

        if len(candles) < 5:

            return pivots

        for i in range(2, len(candles) - 2):

            current = candles[i]

            # Pivot High
            if (

                current.high > candles[i - 1].high
                and current.high > candles[i - 2].high
                and current.high > candles[i + 1].high
                and current.high > candles[i + 2].high

            ):

                pivots["highs"].append(

                    current

                )

            # Pivot Low
            if (

                current.low < candles[i - 1].low
                and current.low < candles[i - 2].low
                and current.low < candles[i + 1].low
                and current.low < candles[i + 2].low

            ):

                pivots["lows"].append(

                    current

                )

        return pivots

    # --------------------------------------------------

    def _build_structure(

        self,

        pivots,

        analysis

    ):

        analysis.swing_highs = pivots["highs"]

        analysis.swing_lows = pivots["lows"]

        # Every pivot starts as an internal candidate.
        # StructureEngine will later decide which swings
        # become External, Protected or Completed.

        analysis.internal_highs = pivots["highs"].copy()

        analysis.internal_lows = pivots["lows"].copy()

    # --------------------------------------------------

    def _find_protected_levels(

        self,

        analysis

    ):

        # Protected levels are created only after:
        # Internal
        # -> Manipulation
        # -> CISD
        # -> Protected
        #
        # This logic belongs to ExecutionEngine.

        pass

    # --------------------------------------------------

    def _classify_swings(

        self,

        analysis

    ):

        # StructureEngine will classify swings
        # into External / Internal / Completed.

        pass
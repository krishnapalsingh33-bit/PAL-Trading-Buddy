from models.swing_analysis import SwingAnalysis


class MeaningfulSwingFilter:

    def filter(

        self,

        swings: SwingAnalysis

    ) -> SwingAnalysis:

        # ----------------------------------
        # Reset
        # ----------------------------------

        swings.meaningful_highs.clear()

        swings.meaningful_lows.clear()

        # ----------------------------------
        # Filter Highs
        # ----------------------------------

        for swing in swings.swing_highs:

            if swing in swings.completed_highs:

                continue

            swings.meaningful_highs.append(

                swing

            )

        # ----------------------------------
        # Filter Lows
        # ----------------------------------

        for swing in swings.swing_lows:

            if swing in swings.completed_lows:

                continue

            swings.meaningful_lows.append(

                swing

            )

        return swings
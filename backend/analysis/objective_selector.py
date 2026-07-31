from models.liquidity_analysis import LiquidityAnalysis


class ObjectiveSelector:

    def select(

        self,

        liquidity: LiquidityAnalysis,

        trend: str

    ):

        result = {

            "current": "Unknown",

            "next": "Unknown",

            "story": "No active journey."

        }

        if (

            liquidity is None

            or

            liquidity.active_chain is None

        ):

            return result

        chain = liquidity.active_chain

        # ---------------------------------
        # Current Objective
        # ---------------------------------

        if chain.external:

            level = chain.external

            result["current"] = (

                f"{level.timeframe} "

                f"{level.side} "

                f"{level.level_type}"

            )

        # ---------------------------------
        # Next Checkpoint
        # ---------------------------------

        if chain.current_internal:

            level = chain.current_internal

            result["next"] = (

                f"{level.timeframe} "

                f"{level.side} "

                f"{level.level_type}"

            )

        # ---------------------------------
        # Story
        # ---------------------------------

        result["story"] = chain.story

        return result
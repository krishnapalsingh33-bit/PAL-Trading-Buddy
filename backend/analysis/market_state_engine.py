from models.market_state import MarketState

from analysis.trading_focus_engine import TradingFocusEngine


class MarketStateEngine:

    def __init__(self):

        self.focus_engine = TradingFocusEngine()

    def build(
        self,
        liquidity,
        latest_price
    ) -> MarketState:

        state = MarketState()

        # ----------------------------------
        # Price
        # ----------------------------------

        state.current_price = latest_price

        # ----------------------------------
        # Objectives
        # ----------------------------------

        state.current_objective = liquidity.current_objective
        state.next_objective = liquidity.next_objective

        # ----------------------------------
        # Trading Focus
        # ----------------------------------

        state.trading_focus = self.focus_engine.build(
            state
        )

        # ----------------------------------
        # Remaining Liquidity
        # ----------------------------------

        state.remaining_liquidity.extend(
            liquidity.remaining_buy
        )

        state.remaining_liquidity.extend(
            liquidity.remaining_sell
        )

        # ----------------------------------
        # Completed Liquidity
        #
        # The current LiquidityAnalysis model
        # no longer tracks completed_buy /
        # completed_sell. Leave this empty.
        # ----------------------------------

        # ----------------------------------
        # Summary
        # ----------------------------------

        state.summary.append(
            f"Remaining: {len(state.remaining_liquidity)}"
        )

        state.summary.append(
            f"Completed: {len(state.completed_liquidity)}"
        )

        if state.current_objective:

            state.summary.append(
                f"Current Objective: "
                f"{state.current_objective.timeframe} "
                f"{state.current_objective.side} "
                f"{state.current_objective.level_type}"
            )

        if state.next_objective:

            state.summary.append(
                f"Next Objective: "
                f"{state.next_objective.timeframe} "
                f"{state.next_objective.side} "
                f"{state.next_objective.level_type}"
            )

        return state
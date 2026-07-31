from models.hierarchical_story import HierarchicalStory
from models.story_layer import StoryLayer


class HierarchicalStoryEngine:

    def build(

        self,

        context

    ) -> HierarchicalStory:

        story = HierarchicalStory()

        # ----------------------------------
        # Daily
        # ----------------------------------

        if context.daily.market_state.current_objective:

            objective = context.daily.market_state.current_objective

            story.daily = StoryLayer(

                timeframe="Daily",

                direction=objective.side,

                objective=objective.level_type,

                valid=True,

                description=f"Daily {objective.side} {objective.level_type}"

            )

        # ----------------------------------
        # 4H
        # ----------------------------------

        if context.h4.market_state.current_objective:

            objective = context.h4.market_state.current_objective

            story.h4 = StoryLayer(

                timeframe="4H",

                direction=objective.side,

                objective=objective.level_type,

                valid=True,

                description=f"4H {objective.side} {objective.level_type}"

            )

        # ----------------------------------
        # 1H
        # ----------------------------------

        if context.h1.market_state.current_objective:

            objective = context.h1.market_state.current_objective

            story.h1 = StoryLayer(

                timeframe="1H",

                direction=objective.side,

                objective=objective.level_type,

                valid=True,

                description=f"1H {objective.side} {objective.level_type}"

            )

        # ----------------------------------
        # 30M
        # ----------------------------------

        if context.m30.market_state.current_objective:

            objective = context.m30.market_state.current_objective

            story.m30 = StoryLayer(

                timeframe="30M",

                direction=objective.side,

                objective=objective.level_type,

                valid=True,

                description=f"30M {objective.side} {objective.level_type}"

            )

        # ----------------------------------
        # 15M
        # ----------------------------------

        if context.m15.market_state.current_objective:

            objective = context.m15.market_state.current_objective

            story.m15 = StoryLayer(

                timeframe="15M",

                direction=objective.side,

                objective=objective.level_type,

                valid=True,

                description=f"15M {objective.side} {objective.level_type}"

            )

        return story
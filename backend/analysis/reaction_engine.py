from models.reaction_state import ReactionState


class ReactionEngine:

    def evaluate(

        self,

        reached_objective=False,

        entered_fvg=False,

        respected_fvg=False,

        created_internal=False,

        manipulation=False,

        cisd=False

    ) -> ReactionState:

        state = ReactionState()

        state.reached_objective = reached_objective

        state.entered_fvg = entered_fvg

        state.respected_fvg = respected_fvg

        state.created_internal = created_internal

        state.manipulation_seen = manipulation

        state.cisd_confirmed = cisd

        # ----------------------------------------

        if not reached_objective:

            state.reason.append(

                "Waiting for mission objective."

            )

            return state

        if not entered_fvg:

            state.reason.append(

                "Waiting for FVG."

            )

            return state

        if not respected_fvg:

            state.reason.append(

                "Watching market reaction."

            )

            return state

        if not created_internal:

            state.reason.append(

                "Waiting for internal liquidity."

            )

            return state

        if not manipulation:

            state.reason.append(

                "Waiting for manipulation."

            )

            return state

        if not cisd:

            state.reason.append(

                "Waiting for CISD."

            )

            return state

        state.next_action = "EXECUTE"

        state.reason.append(

            "A++ model confirmed."

        )

        return state
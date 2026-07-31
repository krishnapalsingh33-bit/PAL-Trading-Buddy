from brain.events import Event


class Interpreter:

    def interpret(self, observation):

        story = []

        if observation.has(Event.EXTERNAL_LIQUIDITY):

            story.append(
                "External liquidity has been taken."
            )

        if observation.has(Event.FVG_CREATED):

            story.append(
                "A new Fair Value Gap has been created."
            )

        if observation.has(Event.INTERNAL_LIQUIDITY):

            story.append(
                "Internal liquidity has been collected."
            )

        if observation.has(Event.MANIPULATION):

            story.append(
                "Manipulation is complete."
            )

        if observation.has(Event.CISD):

            story.append(
                "Execution confirmation exists."
            )

        if observation.has(Event.TARGET_REACHED):

            story.append(
                "Mission completed."
            )

        return story
from models.hierarchical_story import HierarchicalStory


class StoryAlignmentEngine:

    def analyze(

        self,

        story: HierarchicalStory

    ):

        alignment = {

            "direction": "NONE",

            "score": 0,

            "reason": []

        }

        # ----------------------------------
        # Daily
        # ----------------------------------

        if story.daily.valid:

            alignment["direction"] = (

                story.daily.direction

            )

            alignment["score"] += 30

        # ----------------------------------
        # 4H
        # ----------------------------------

        if (

            story.h4.valid

            and

            story.h4.direction == alignment["direction"]

        ):

            alignment["score"] += 20

        # ----------------------------------
        # 1H
        # ----------------------------------

        if (

            story.h1.valid

            and

            story.h1.direction == alignment["direction"]

        ):

            alignment["score"] += 20

        # ----------------------------------
        # 30M
        # ----------------------------------

        if (

            story.m30.valid

            and

            story.m30.direction == alignment["direction"]

        ):

            alignment["score"] += 15

        # ----------------------------------
        # 15M
        # ----------------------------------

        if (

            story.m15.valid

            and

            story.m15.direction == alignment["direction"]

        ):

            alignment["score"] += 15

        # ----------------------------------

        if alignment["score"] >= 80:

            alignment["reason"].append(

                "Strong multi-timeframe alignment."

            )

        elif alignment["score"] >= 60:

            alignment["reason"].append(

                "Good alignment."

            )

        else:

            alignment["reason"].append(

                "Weak alignment."

            )

        return alignment
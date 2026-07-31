from analysis.mission_state import MissionState


class StoryGenerator:

    def generate(self, mission: MissionState):

        story = []

        story.append(f"Mission : {mission.target}")

        story.append(f"Current Stage : {mission.stage}")

        if mission.evidence:

            story.append("")

            story.append("Evidence")

            for item in mission.evidence:

                story.append(f"✓ {item}")

        if mission.next_step:

            story.append("")

            story.append(f"Next : {mission.next_step}")

        if mission.completed:

            story.append("")

            story.append("Mission Completed")

        return story
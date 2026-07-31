from dataclasses import dataclass, field

from brain.events import Event


@dataclass
class Observation:

    events: list[Event] = field(default_factory=list)

    evidence: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    values: dict = field(default_factory=dict)

    def add_event(self, event: Event):

        if event not in self.events:

            self.events.append(event)

    def has(self, event: Event):

        return event in self.events
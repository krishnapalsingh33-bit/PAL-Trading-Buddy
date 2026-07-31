from dataclasses import dataclass, field

from models.story_layer import StoryLayer


@dataclass
class HierarchicalStory:

    daily: StoryLayer = field(default_factory=StoryLayer)

    h4: StoryLayer = field(default_factory=StoryLayer)

    h1: StoryLayer = field(default_factory=StoryLayer)

    m30: StoryLayer = field(default_factory=StoryLayer)

    m15: StoryLayer = field(default_factory=StoryLayer)
from core.models import ManipulationData


def analyze_manipulation():

    """
    Placeholder version.

    Later this engine will detect
    manipulation from real market structure.
    """

    return ManipulationData(

        detected=True,

        manipulation_count=2,

        first_manipulation=True,
        second_manipulation=True,

        direction="BUY",

        quality="STRONG"
    )
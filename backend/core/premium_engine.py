from core.models import PremiumData


def analyze_premium():

    """
    Placeholder version.

    Later this engine will determine
    Premium / Discount from the
    current dealing range.
    """

    return PremiumData(

        location="Discount",

        premium=False,

        discount=True,

        equilibrium=False,

        confidence=92,

        reason="Price is trading in the discount zone."

    )
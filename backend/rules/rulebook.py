"""
PAL Rulebook

Every trading decision in PAL must follow these rules.
"""


RULES = {

    "external_liquidity_first": True,

    "dxy_leads": True,

    "require_cisd": True,

    "require_discount": True,

    "minimum_grade": "A",

    "allow_counter_trend": False,

    "require_alignment": True,

}
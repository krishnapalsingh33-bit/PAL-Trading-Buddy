from core.models import FilterData


def analyze_filters():

    filters = FilterData(
        high_impact_news=False,
        london_session=True,
        new_york_session=False
    )

    return filters
from models.timeframe_node import TimeframeNode


class TimeframeCascade:

    def __init__(self):

        self.nodes = {

            "Weekly": TimeframeNode(

                "Weekly",

                None,

                "Daily"

            ),

            "Daily": TimeframeNode(

                "Daily",

                "Weekly",

                "4H"

            ),

            "4H": TimeframeNode(

                "4H",

                "Daily",

                "1H"

            ),

            "1H": TimeframeNode(

                "1H",

                "4H",

                "15M"

            ),

            "15M": TimeframeNode(

                "15M",

                "1H",

                "5M"

            ),

            "5M": TimeframeNode(

                "5M",

                "15M",

                "3M"

            ),

            "3M": TimeframeNode(

                "3M",

                "5M",

                "1M"

            ),

            "1M": TimeframeNode(

                "1M",

                "3M",

                None

            )

        }

    def higher(

        self,

        timeframe

    ):

        node = self.nodes.get(timeframe)

        if node:

            return node.higher

        return None

    def lower(

        self,

        timeframe

    ):

        node = self.nodes.get(timeframe)

        if node:

            return node.lower

        return None
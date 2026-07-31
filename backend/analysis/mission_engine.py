from models.mission import Mission


class MissionEngine:

    def create_mission(

        self,

        target_timeframe,

        target_side,

        reason

    ):

        hierarchy = {

            "Weekly": [

                "Daily",

                "4H",

                "1H",

                "30M",

                "15M",

                "5M",

                "3M"

            ],

            "Daily": [

                "4H",

                "1H",

                "30M",

                "15M",

                "5M",

                "3M"

            ],

            "4H": [

                "1H",

                "30M",

                "15M",

                "5M",

                "3M"

            ],

            "1H": [

                "30M",

                "15M",

                "5M",

                "3M"

            ],

            "30M": [

                "15M",

                "5M",

                "3M"

            ],

            "15M": [

                "5M",

                "3M"

            ],

            "5M": [

                "3M"

            ],

            "3M": []

        }

        return Mission(

            target_timeframe=target_timeframe,

            target_side=target_side,

            external_timeframe=target_timeframe,

            internal_timeframes=hierarchy.get(

                target_timeframe,

                []

            ),

            reason=reason

        )
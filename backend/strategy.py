# ==========================================
# PAL TRADING BUDDY
# Krishna A++ Strategy
# ==========================================

class Strategy:

    def __init__(self):
        self.rules = {
            "external_liquidity": False,
            "manipulation": False,
            "cisd": False,
            "smt": False,
            "premium_discount": False,
            "dxy_alignment": False,
        }

    def score(self):

        score = 0

        if self.rules["external_liquidity"]:
            score += 20

        if self.rules["manipulation"]:
            score += 20

        if self.rules["cisd"]:
            score += 20

        if self.rules["dxy_alignment"]:
            score += 20

        if self.rules["premium_discount"]:
            score += 10

        if self.rules["smt"]:
            score += 10

        return score

    def grade(self):

        total = self.score()

        if total >= 90:
            return "A++"

        elif total >= 80:
            return "A+"

        elif total >= 70:
            return "B"

        else:
            return "No Trade"
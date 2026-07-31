import Badge from "../ui/Badge";
import Card from "../ui/Card";

type Props = {
    bias: string;
    dxyTrend: string;
    action: string;
    health: string;
    newsSafe: boolean;
    nextStep: string;
};

function MarketStoryCard({
    bias,
    dxyTrend,
    action,
    health,
    newsSafe,
    nextStep,
}: Props) {

    return (

        <Card title="Market Story">

            <div className="space-y-6">

                <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-5">

                    <p className="mb-3 text-xs uppercase tracking-wide text-zinc-500">
                        Market Narrative
                    </p>

                    <p className="leading-7 text-zinc-300">
                        PAL currently maintains a{" "}
                        <span className="font-semibold text-white">
                            {bias}
                        </span>{" "}
                        market bias while the Dollar Index is{" "}
                        <span className="font-semibold text-white">
                            {dxyTrend}
                        </span>.
                        The current execution model suggests{" "}
                        <span className="font-semibold text-white">
                            {action}
                        </span>{" "}
                        as the preferred trading decision until all required
                        confirmations are satisfied.
                    </p>

                </div>

                <div className="grid gap-4 sm:grid-cols-2">

                    <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                        <p className="mb-2 text-xs uppercase tracking-wide text-zinc-500">
                            Market Health
                        </p>

                        <Badge text={health} />

                    </div>

                    <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                        <p className="mb-2 text-xs uppercase tracking-wide text-zinc-500">
                            News Status
                        </p>

                        <Badge text={newsSafe ? "SAFE" : "UNSAFE"} />

                    </div>

                </div>

                <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-5">

                    <p className="mb-3 text-xs uppercase tracking-wide text-zinc-500">
                        Trading Implication
                    </p>

                    <p className="leading-7 text-zinc-300">

                        {nextStep}

                    </p>

                </div>

                <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-5">

                    <p className="mb-3 text-xs uppercase tracking-wide text-zinc-500">
                        Executive Summary
                    </p>

                    <ul className="space-y-3 text-sm text-zinc-300">

                        <li>• PAL Bias: <strong>{bias}</strong></li>

                        <li>• DXY Trend: <strong>{dxyTrend}</strong></li>

                        <li>• Decision: <strong>{action}</strong></li>

                        <li>
                            • News Environment:{" "}
                            <strong>
                                {newsSafe ? "Favorable" : "High Impact"}
                            </strong>
                        </li>

                    </ul>

                </div>

            </div>

        </Card>

    );

}

export default MarketStoryCard;
import Card from "../ui/Card";
import Badge from "../ui/Badge";

type Props = {
    readiness: number;
    stage: string;
    decision: string;
    nextStep: string;
};

function TradeReadinessCard({
    readiness,
    stage,
    decision,
    nextStep,
}: Props) {

    const progressColor =
        readiness >= 80
            ? "bg-emerald-500"
            : readiness >= 60
                ? "bg-yellow-500"
                : "bg-red-500";

    const status =
        readiness >= 80
            ? "READY"
            : readiness >= 60
                ? "BUILDING"
                : "NOT READY";

    const statusColor =
        readiness >= 80
            ? "text-emerald-400"
            : readiness >= 60
                ? "text-yellow-400"
                : "text-red-400";

    return (

        <Card title="Trade Readiness">

            <div className="space-y-6">

                <div className="text-center">

                    <p className="text-5xl font-bold">

                        {readiness}<span className="text-2xl">%</span>

                    </p>

                    <p className={`mt-3 text-lg font-semibold ${statusColor}`}>

                        {status}

                    </p>

                </div>

                <div>

                    <div className="mb-2 flex items-center justify-between text-sm">

                        <span className="text-zinc-400">
                            Setup Progress
                        </span>

                        <span className="font-semibold">
                            {readiness}%
                        </span>

                    </div>

                    <div className="h-3 overflow-hidden rounded-full bg-zinc-800">

                        <div
                            className={`h-full ${progressColor} transition-all duration-700`}
                            style={{
                                width: `${readiness}%`,
                            }}
                        />

                    </div>

                </div>

                <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                    <p className="mb-2 text-xs uppercase tracking-wide text-zinc-500">

                        Current Stage

                    </p>

                    <Badge text={stage} />

                </div>

                <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                    <p className="mb-2 text-xs uppercase tracking-wide text-zinc-500">

                        Decision

                    </p>

                    <Badge text={decision} />

                </div>

                <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                    <p className="mb-3 text-xs uppercase tracking-wide text-zinc-500">

                        Next Objective

                    </p>

                    <p className="leading-7 text-zinc-300">

                        {nextStep}

                    </p>

                </div>

            </div>

        </Card>

    );

}

export default TradeReadinessCard;
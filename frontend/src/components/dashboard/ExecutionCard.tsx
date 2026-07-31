import Badge from "../ui/Badge";
import Card from "../ui/Card";

type Props = {
    action: string;
    trend: string;
    timeframe: string;
    stage: string;
    reason: string;
    confirmations: string[];
};

function ExecutionCard({
    action,
    trend,
    timeframe,
    stage,
    reason,
    confirmations,
}: Props) {
    return (
        <Card title="Execution">

            <div className="space-y-5">

                <div className="flex justify-between">
                    <span className="text-zinc-400">Action</span>
                    <Badge text={action} />
                </div>

                <div className="flex justify-between">
                    <span className="text-zinc-400">Trend</span>
                    <Badge text={trend} />
                </div>

                <div className="flex justify-between">
                    <span className="text-zinc-400">Timeframe</span>
                    <span>{timeframe || "-"}</span>
                </div>

                <div className="flex justify-between">
                    <span className="text-zinc-400">Stage</span>
                    <span>{stage || "-"}</span>
                </div>

                <div>
                    <p className="mb-2 text-zinc-400">
                        Reason
                    </p>

                    <div className="rounded-lg bg-zinc-950 p-3 text-sm">
                        {reason}
                    </div>
                </div>

                <div>

                    <p className="mb-2 text-zinc-400">
                        Confirmations
                    </p>

                    {confirmations.length === 0 ? (

                        <div className="rounded-lg bg-zinc-950 p-3 text-sm text-zinc-500">
                            No confirmations available.
                        </div>

                    ) : (

                        <div className="space-y-2">

                            {confirmations.map((item, index) => (

                                <div
                                    key={index}
                                    className="rounded-lg bg-zinc-950 p-3 text-sm"
                                >
                                    ✓ {item}
                                </div>

                            ))}

                        </div>

                    )}

                </div>

            </div>

        </Card>
    );
}

export default ExecutionCard;
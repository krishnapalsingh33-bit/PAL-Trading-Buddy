import Badge from "../ui/Badge";
import Card from "../ui/Card";

type Props = {
    trend: string;
    expectedDirection: string;
    aligned: boolean;
    confirmations: string[];
};

function DXYCard({
    trend,
    expectedDirection,
    aligned,
    confirmations,
}: Props) {

    return (

        <Card title="DXY Intelligence">

            <div className="space-y-6">

                <div className="grid grid-cols-3 gap-3">

                    <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                        <p className="mb-2 text-xs uppercase tracking-wide text-zinc-500">
                            DXY Trend
                        </p>

                        <Badge text={trend} />

                    </div>

                    <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                        <p className="mb-2 text-xs uppercase tracking-wide text-zinc-500">
                            GBP Bias
                        </p>

                        <Badge text={expectedDirection} />

                    </div>

                    <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                        <p className="mb-2 text-xs uppercase tracking-wide text-zinc-500">
                            Alignment
                        </p>

                        <Badge
                            text={aligned ? "ALIGNED" : "NOT ALIGNED"}
                        />

                    </div>

                </div>

                <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-5">

                    <div className="flex items-center justify-between">

                        <span className="font-medium">

                            PAL Confirmation

                        </span>

                        <span
                            className={`font-bold ${
                                aligned
                                    ? "text-emerald-400"
                                    : "text-red-400"
                            }`}
                        >
                            {aligned ? "CONFIRMED" : "CONFLICT"}

                        </span>

                    </div>

                    <div className="mt-4 h-3 overflow-hidden rounded-full bg-zinc-800">

                        <div
                            className={`h-full rounded-full transition-all duration-700 ${
                                aligned
                                    ? "bg-emerald-500"
                                    : "bg-red-500"
                            }`}
                            style={{
                                width: aligned ? "100%" : "45%",
                            }}
                        />

                    </div>

                </div>

                <div>

                    <p className="mb-4 text-xs uppercase tracking-wide text-zinc-500">

                        DXY Checklist

                    </p>

                    <div className="space-y-3">

                        {confirmations.map((item, index) => (

                            <div
                                key={index}
                                className="flex items-start gap-3 rounded-xl border border-zinc-800 bg-zinc-950 p-3"
                            >

                                <span className="mt-0.5 text-emerald-400">

                                    ✓

                                </span>

                                <span className="text-sm leading-6 text-zinc-300">

                                    {item}

                                </span>

                            </div>

                        ))}

                    </div>

                </div>

            </div>

        </Card>

    );

}

export default DXYCard;
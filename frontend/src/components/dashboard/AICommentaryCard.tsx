import Card from "../ui/Card";

type Props = {
    headline: string;
    summary: string;
    marketStory: string;
    nextAction: string;
    confidence: number;
    risk: string;
    reasoning: string[];
};

function AICommentaryCard({
    headline,
    summary,
    marketStory,
    nextAction,
    confidence,
    risk,
    reasoning,
}: Props) {

    const confidenceColor =
        confidence >= 80
            ? "bg-emerald-500"
            : confidence >= 60
                ? "bg-yellow-500"
                : "bg-red-500";

    const riskColor =
        risk === "LOW"
            ? "bg-emerald-500"
            : risk === "MEDIUM"
                ? "bg-yellow-500"
                : "bg-red-500";

    return (

        <Card title="🧠 AI Decision Engine">

            <div className="space-y-6">

                <div>

                    <h3 className="text-2xl font-bold text-white">

                        {headline}

                    </h3>

                    <p className="mt-3 leading-7 text-zinc-400">

                        {summary}

                    </p>

                </div>

                <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-5">

                    <h4 className="mb-4 text-sm font-semibold uppercase tracking-wider text-zinc-400">

                        Market Story

                    </h4>

                    <p className="leading-8 text-zinc-300 whitespace-pre-line">

                        {marketStory}

                    </p>

                </div>

                <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-5">

                    <h4 className="mb-4 text-sm font-semibold uppercase tracking-wider text-zinc-400">

                        Next Action

                    </h4>

                    <p className="leading-8 text-white">

                        {nextAction}

                    </p>

                </div>

                <div className="space-y-4">

                    <div className="flex items-center justify-between">

                        <span className="font-medium text-zinc-300">

                            Confidence

                        </span>

                        <span className="font-bold text-white">

                            {confidence}%

                        </span>

                    </div>

                    <div className="h-3 overflow-hidden rounded-full bg-zinc-800">

                        <div
                            className={`h-full ${confidenceColor} transition-all duration-700`}
                            style={{ width: `${confidence}%` }}
                        />

                    </div>

                </div>

                <div className="flex items-center justify-between rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                    <span className="font-medium text-zinc-300">

                        Risk Level

                    </span>

                    <span
                        className={`rounded-full px-4 py-1 text-sm font-semibold text-white ${riskColor}`}
                    >

                        {risk}

                    </span>

                </div>

                <div>

                    <h4 className="mb-4 text-sm font-semibold uppercase tracking-wider text-zinc-400">

                        AI Reasoning

                    </h4>

                    <div className="space-y-3">

                        {reasoning.map((item, index) => (

                            <div
                                key={index}
                                className="flex items-start gap-3 rounded-xl border border-zinc-800 bg-zinc-950 p-3"
                            >

                                <span className="mt-1 text-emerald-400">

                                    ✓

                                </span>

                                <span className="leading-7 text-zinc-300">

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

export default AICommentaryCard;
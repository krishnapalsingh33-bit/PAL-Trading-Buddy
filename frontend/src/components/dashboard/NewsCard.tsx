import Badge from "../ui/Badge";
import Card from "../ui/Card";

type Props = {
    safe: boolean;
    summary: string;
    warnings: string[];
    highImpact: string[];
};

function NewsCard({
    safe,
    summary,
    warnings,
    highImpact,
}: Props) {

    return (

        <Card title="News">

            <div className="space-y-5">

                <div className="flex justify-between">

                    <span className="text-zinc-400">
                        Trading Status
                    </span>

                    <Badge text={safe ? "SAFE" : "UNSAFE"} />

                </div>

                <div>

                    <p className="mb-2 text-zinc-400">
                        Summary
                    </p>

                    <div className="rounded-lg bg-zinc-950 p-3 text-sm">
                        {summary}
                    </div>

                </div>

                <div>

                    <p className="mb-2 text-zinc-400">
                        High Impact News
                    </p>

                    {highImpact.length === 0 ? (

                        <div className="rounded-lg bg-zinc-950 p-3 text-sm text-zinc-500">
                            No high-impact events.
                        </div>

                    ) : (

                        <div className="space-y-2">

                            {highImpact.map((item, index) => (

                                <div
                                    key={index}
                                    className="rounded-lg bg-red-700 p-3 text-sm"
                                >
                                    {item}
                                </div>

                            ))}

                        </div>

                    )}

                </div>

                <div>

                    <p className="mb-2 text-zinc-400">
                        Warnings
                    </p>

                    {warnings.length === 0 ? (

                        <div className="rounded-lg bg-zinc-950 p-3 text-sm text-zinc-500">
                            No warnings.
                        </div>

                    ) : (

                        <div className="space-y-2">

                            {warnings.map((item, index) => (

                                <div
                                    key={index}
                                    className="rounded-lg bg-yellow-700 p-3 text-sm"
                                >
                                    {item}
                                </div>

                            ))}

                        </div>

                    )}

                </div>

            </div>

        </Card>

    );

}

export default NewsCard;
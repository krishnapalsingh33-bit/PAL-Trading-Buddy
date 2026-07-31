import Badge from "../ui/Badge";
import Card from "../ui/Card";

type Workflow = {
    timeframe: string;
    trend: string;
    stage: string;
    grade: string;
    decision: string;
    completed_steps: string[];
    missing_steps: string[];
};

type Props = {
    workflow: Workflow[];
};

function WorkflowCard({ workflow }: Props) {
    return (
        <Card title="PAL Workflow Timeline">

            <div className="space-y-4">

                {workflow.map((item) => {

                    const progress = Math.round(
                        (item.completed_steps.length / 8) * 100
                    );

                    return (

                        <div
                            key={item.timeframe}
                            className="rounded-2xl border border-zinc-800 bg-zinc-950 p-5 transition-all duration-300 hover:border-zinc-700"
                        >

                            <div className="flex items-center justify-between">

                                <div className="flex items-center gap-4">

                                    <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-zinc-900 text-lg font-bold">

                                        {item.timeframe}

                                    </div>

                                    <div>

                                        <div className="flex gap-2">

                                            <Badge text={item.trend} />
                                            <Badge text={item.decision} />

                                        </div>

                                        <p className="mt-2 text-sm text-zinc-400">

                                            {item.stage}

                                        </p>

                                    </div>

                                </div>

                                <div className="text-right">

                                    <div className="text-xl font-bold">

                                        {progress}%

                                    </div>

                                    <div className="text-xs text-zinc-500">

                                        {item.grade} Grade

                                    </div>

                                </div>

                            </div>

                            <div className="mt-5 h-2 overflow-hidden rounded-full bg-zinc-800">

                                <div
                                    className="h-full rounded-full bg-emerald-500 transition-all duration-700"
                                    style={{
                                        width: `${progress}%`,
                                    }}
                                />

                            </div>

                            <div className="mt-5 grid grid-cols-2 gap-4">

                                <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-4">

                                    <p className="mb-3 text-xs uppercase tracking-wide text-zinc-500">

                                        Completed

                                    </p>

                                    <ul className="space-y-2 text-sm">

                                        {item.completed_steps.map(step => (

                                            <li
                                                key={step}
                                                className="text-emerald-400"
                                            >
                                                ✓ {step}
                                            </li>

                                        ))}

                                    </ul>

                                </div>

                                <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-4">

                                    <p className="mb-3 text-xs uppercase tracking-wide text-zinc-500">

                                        Waiting For

                                    </p>

                                    <ul className="space-y-2 text-sm">

                                        {item.missing_steps.map(step => (

                                            <li
                                                key={step}
                                                className="text-yellow-400"
                                            >
                                                ○ {step}
                                            </li>

                                        ))}

                                    </ul>

                                </div>

                            </div>

                        </div>

                    );

                })}

            </div>

        </Card>
    );
}

export default WorkflowCard;
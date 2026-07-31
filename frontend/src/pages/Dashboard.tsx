import Sidebar from "../components/layout/Sidebar";
import Header from "../components/layout/Header";
import MainWorkspace from "../components/layout/MainWorkspace";

import SummaryCard from "../components/dashboard/SummaryCard";
import MarketOverviewCard from "../components/dashboard/MarketOverviewCard";
import TradeReadinessCard from "../components/dashboard/TradeReadinessCard";
import WorkflowCard from "../components/dashboard/WorkflowCard";
import DXYCard from "../components/dashboard/DXYCard";
import ExecutionCard from "../components/dashboard/ExecutionCard";
import NewsCard from "../components/dashboard/NewsCard";
import MarketStoryCard from "../components/dashboard/MarketStoryCard";
import AICommentaryCard from "../components/dashboard/AICommentaryCard";

import { usePAL } from "../hooks/usePAL";

function LoadingSkeleton() {
    return (
        <div className="min-h-screen bg-zinc-950 p-8 animate-pulse">

            <div className="mb-8 h-32 rounded-2xl bg-zinc-900" />

            <div className="mb-6 grid grid-cols-2 gap-4 xl:grid-cols-6">
                {Array.from({ length: 6 }).map((_, i) => (
                    <div
                        key={i}
                        className="h-24 rounded-xl bg-zinc-900"
                    />
                ))}
            </div>

            <div className="grid gap-6 xl:grid-cols-[2fr_1fr]">

                <div className="space-y-6">

                    {Array.from({ length: 4 }).map((_, i) => (
                        <div
                            key={i}
                            className="h-64 rounded-2xl bg-zinc-900"
                        />
                    ))}

                </div>

                <div className="space-y-6">

                    {Array.from({ length: 4 }).map((_, i) => (
                        <div
                            key={i}
                            className="h-56 rounded-2xl bg-zinc-900"
                        />
                    ))}

                </div>

            </div>

        </div>
    );
}

function Dashboard() {

    const { data, isLoading, error } = usePAL();

    if (isLoading) {
        return <LoadingSkeleton />;
    }

    if (error) {
        return (
            <div className="flex min-h-screen items-center justify-center bg-zinc-950 p-8">

                <div className="max-w-md rounded-2xl border border-red-800 bg-zinc-900 p-8 text-center">

                    <h2 className="mb-4 text-2xl font-bold text-red-400">
                        Backend Connection Failed
                    </h2>

                    <p className="mb-6 text-zinc-400">
                        PAL couldn't connect to the backend server.
                    </p>

                    <div className="space-y-2 text-sm text-zinc-500">

                        <p>• Is FastAPI running?</p>

                        <p>• Is the API URL correct?</p>

                        <p>• Is the backend reachable?</p>

                    </div>

                    <button
                        onClick={() => window.location.reload()}
                        className="mt-8 rounded-xl bg-emerald-600 px-5 py-3 font-semibold transition hover:bg-emerald-500"
                    >
                        Retry
                    </button>

                </div>

            </div>
        );
    }

    if (!data || !data.report) {
        return (
            <div className="flex min-h-screen items-center justify-center bg-zinc-950">

                <div className="rounded-2xl border border-zinc-800 bg-zinc-900 p-8 text-center">

                    <h2 className="mb-3 text-2xl font-bold">
                        No Analysis Available
                    </h2>

                    <p className="text-zinc-400">
                        PAL didn't receive any market analysis.
                    </p>

                </div>

            </div>
        );
    }

    const report = data.report;
    const workflow = report.pal.workflow[0];

    const readiness = Math.round(
        (workflow.completed_steps.length / 8) * 100
    );

    return (
        <div className="flex min-h-screen bg-zinc-950 text-white">

            <Sidebar symbol={data.symbol} />

            <main className="flex-1 overflow-y-auto p-8">

                <Header
                    symbol={data.symbol}
                    live={true}
                    bias={report.pal.overall_bias}
                    action={report.execution.action}
                    health={report.market_health.status}
                />

                <div className="mb-6 grid grid-cols-2 gap-4 xl:grid-cols-6">

                    <SummaryCard
                        title="Bias"
                        value={report.pal.overall_bias}
                    />

                    <SummaryCard
                        title="Decision"
                        value={report.execution.action}
                    />

                    <SummaryCard
                        title="Health"
                        value={report.market_health.status}
                    />

                    <SummaryCard
                        title="Ready"
                        value={`${readiness}%`}
                    />

                    <SummaryCard
                        title="DXY"
                        value={
                            report.dxy.aligned
                                ? "ALIGNED"
                                : "NOT ALIGNED"
                        }
                    />

                    <SummaryCard
                        title="News"
                        value={
                            report.news.safe_to_trade
                                ? "SAFE"
                                : "UNSAFE"
                        }
                    />

                </div>

                <MainWorkspace
                    left={
                        <>
                            <MarketStoryCard
                                bias={report.pal.overall_bias}
                                dxyTrend={report.dxy.trend}
                                action={report.execution.action}
                                health={report.market_health.status}
                                newsSafe={report.news.safe_to_trade}
                                nextStep={workflow.next_step}
                            />

                            <AICommentaryCard
                                headline={report.ai_commentary.headline}
                                summary={report.ai_commentary.summary}
                                marketStory={report.ai_commentary.market_story}
                                nextAction={report.ai_commentary.next_action}
                                confidence={report.ai_commentary.confidence}
                                risk={report.ai_commentary.risk}
                                reasoning={report.ai_commentary.reasoning}
                            />

                            <WorkflowCard
                                workflow={report.pal.workflow}
                            />

                            <NewsCard
                                safe={report.news.safe_to_trade}
                                summary={report.news.summary}
                                warnings={report.news.warnings}
                                highImpact={report.news.high_impact}
                            />
                        </>
                    }
                    right={
                        <>
                            <ExecutionCard
                                action={report.execution.action}
                                trend={report.execution.trend}
                                timeframe={report.execution.timeframe}
                                stage={report.execution.stage}
                                reason={report.execution.reason}
                                confirmations={report.execution.confirmations}
                            />

                            <TradeReadinessCard
                                readiness={readiness}
                                stage={workflow.stage}
                                decision={report.execution.action}
                                nextStep={workflow.next_step}
                            />

                            <DXYCard
                                trend={report.dxy.trend}
                                expectedDirection={report.dxy.expected_gbp_direction}
                                aligned={report.dxy.aligned}
                                confirmations={report.dxy.confirmations}
                            />

                            <MarketOverviewCard
                                symbol={data.symbol}
                                bias={report.pal.overall_bias}
                                decision={report.execution.action}
                                marketHealth={report.market_health.status}
                            />
                        </>
                    }
                />

            </main>

        </div>
    );
}

export default Dashboard;
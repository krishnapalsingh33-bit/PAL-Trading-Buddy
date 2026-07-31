import Badge from "../ui/Badge";

type Props = {
    symbol: string;
    live: boolean;
    bias: string;
    action: string;
    health: string;
};

function Header({
    symbol,
    live,
    bias,
    action,
    health,
}: Props) {

    const currentTime = new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
    });

    return (

        <header className="sticky top-0 z-50 mb-8 rounded-2xl border border-zinc-800 bg-zinc-900/95 p-8 shadow-2xl backdrop-blur-lg">

            <div className="flex flex-col gap-8 lg:flex-row lg:items-center lg:justify-between">

                <div>

                    <div className="flex items-center gap-3">

                        <div className="h-3 w-3 rounded-full bg-emerald-500 animate-pulse" />

                        <span className="text-sm font-semibold uppercase tracking-[0.25em] text-emerald-400">
                            {live ? "Live Market" : "Offline"}
                        </span>

                    </div>

                    <h1 className="mt-3 text-4xl font-bold tracking-tight text-white">

                        PAL Trading Buddy

                    </h1>

                    <p className="mt-2 max-w-xl text-zinc-400">

                        Professional AI-powered market analysis dashboard built
                        around PAL workflow, DXY confirmation and execution
                        logic.

                    </p>

                </div>

                <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">

                    <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                        <p className="text-xs uppercase tracking-wide text-zinc-500">
                            Symbol
                        </p>

                        <div className="mt-2">
                            <Badge text={symbol} />
                        </div>

                    </div>

                    <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                        <p className="text-xs uppercase tracking-wide text-zinc-500">
                            Bias
                        </p>

                        <div className="mt-2">
                            <Badge text={bias} />
                        </div>

                    </div>

                    <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                        <p className="text-xs uppercase tracking-wide text-zinc-500">
                            Decision
                        </p>

                        <div className="mt-2">
                            <Badge text={action} />
                        </div>

                    </div>

                    <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                        <p className="text-xs uppercase tracking-wide text-zinc-500">
                            Market Health
                        </p>

                        <div className="mt-2">
                            <Badge text={health} />
                        </div>

                    </div>

                    <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                        <p className="text-xs uppercase tracking-wide text-zinc-500">
                            Status
                        </p>

                        <div className="mt-2">
                            <Badge text={live ? "LIVE" : "OFFLINE"} />
                        </div>

                    </div>

                    <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">

                        <p className="text-xs uppercase tracking-wide text-zinc-500">
                            Updated
                        </p>

                        <p className="mt-2 font-semibold text-white">

                            {currentTime}

                        </p>

                    </div>

                </div>

            </div>

        </header>

    );

}

export default Header;
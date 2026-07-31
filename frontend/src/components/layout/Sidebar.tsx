import Badge from "../ui/Badge";

type Props = {
    symbol: string;
};

function Sidebar({ symbol }: Props) {
    return (
        <aside className="sticky top-0 flex h-screen w-64 flex-col border-r border-zinc-800 bg-zinc-900">

            <div className="border-b border-zinc-800 p-6">

                <h1 className="text-3xl font-bold">
                    PAL
                </h1>

                <p className="mt-2 text-sm text-zinc-500">
                    Trading Buddy
                </p>

            </div>

            <nav className="flex-1 space-y-2 p-4">

                <button className="w-full rounded-xl bg-zinc-800 p-3 text-left transition hover:bg-zinc-700">
                    📊 Dashboard
                </button>

                <button className="w-full rounded-xl p-3 text-left text-zinc-400 transition hover:bg-zinc-800 hover:text-white">
                    📈 Workflow
                </button>

                <button className="w-full rounded-xl p-3 text-left text-zinc-400 transition hover:bg-zinc-800 hover:text-white">
                    💵 DXY
                </button>

                <button className="w-full rounded-xl p-3 text-left text-zinc-400 transition hover:bg-zinc-800 hover:text-white">
                    📰 News
                </button>

                <button className="w-full rounded-xl p-3 text-left text-zinc-400 transition hover:bg-zinc-800 hover:text-white">
                    ⚡ Execution
                </button>

            </nav>

            <div className="border-t border-zinc-800 p-5">

                <p className="mb-3 text-xs uppercase tracking-widest text-zinc-500">
                    Active Symbol
                </p>

                <Badge text={symbol} />

            </div>

        </aside>
    );
}

export default Sidebar;
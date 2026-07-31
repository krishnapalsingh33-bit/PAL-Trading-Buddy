type Props = {
    text: string;
};

function Badge({ text }: Props) {

    const value = text.toUpperCase();

    let style =
        "border-zinc-700 bg-zinc-800 text-zinc-200";

    if (value.includes("BULL"))
        style = "border-emerald-500/30 bg-emerald-500/20 text-emerald-300";

    else if (value.includes("BEAR"))
        style = "border-red-500/30 bg-red-500/20 text-red-300";

    else if (value.includes("BUY"))
        style = "border-emerald-500/30 bg-emerald-500/20 text-emerald-300";

    else if (value.includes("SELL"))
        style = "border-red-500/30 bg-red-500/20 text-red-300";

    else if (value.includes("READY"))
        style = "border-sky-500/30 bg-sky-500/20 text-sky-300";

    else if (value.includes("EXECUTE"))
        style = "border-emerald-500/30 bg-emerald-500/20 text-emerald-300";

    else if (value.includes("WAIT"))
        style = "border-amber-500/30 bg-amber-500/20 text-amber-300";

    else if (value.includes("GOOD"))
        style = "border-emerald-500/30 bg-emerald-500/20 text-emerald-300";

    else if (value.includes("FAIR"))
        style = "border-yellow-500/30 bg-yellow-500/20 text-yellow-300";

    else if (value.includes("POOR"))
        style = "border-red-500/30 bg-red-500/20 text-red-300";

    else if (value.includes("SAFE"))
        style = "border-emerald-500/30 bg-emerald-500/20 text-emerald-300";

    else if (value.includes("UNSAFE"))
        style = "border-red-500/30 bg-red-500/20 text-red-300";

    else if (value.includes("LIVE"))
        style = "border-emerald-500/30 bg-emerald-500/20 text-emerald-300";

    else if (value.includes("OFFLINE"))
        style = "border-zinc-600 bg-zinc-800 text-zinc-400";

    else if (value.includes("ALIGNED"))
        style = "border-emerald-500/30 bg-emerald-500/20 text-emerald-300";

    else if (value.includes("NOT ALIGNED"))
        style = "border-red-500/30 bg-red-500/20 text-red-300";

    else if (value.includes("CONFIRMED"))
        style = "border-emerald-500/30 bg-emerald-500/20 text-emerald-300";

    else if (value.includes("CONFLICT"))
        style = "border-red-500/30 bg-red-500/20 text-red-300";

    return (

        <span
            className={`inline-flex items-center rounded-full border px-3 py-1 text-xs font-semibold uppercase tracking-wide shadow-sm ${style}`}
        >
            {text}
        </span>

    );

}

export default Badge;
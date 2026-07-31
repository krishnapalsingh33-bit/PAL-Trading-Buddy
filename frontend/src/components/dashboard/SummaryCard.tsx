import Badge from "../ui/Badge";

type Props = {
    title: string;
    value: string;
};

function SummaryCard({ title, value }: Props) {
    return (
        <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-4 shadow-lg">

            <p className="mb-3 text-xs font-semibold uppercase tracking-wider text-zinc-500">
                {title}
            </p>

            <Badge text={value} />

        </div>
    );
}

export default SummaryCard;
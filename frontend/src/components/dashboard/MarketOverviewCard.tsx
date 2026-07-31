import Badge from "../ui/Badge";
import Card from "../ui/Card";

type Props = {
    symbol: string;
    bias: string;
    decision: string;
    marketHealth: string;
};

function MarketOverviewCard({
    symbol,
    bias,
    decision,
    marketHealth,
}: Props) {
    return (
        <Card title="Market Overview">

            <div className="space-y-5">

                <div className="flex justify-between">
                    <span className="text-zinc-400">Symbol</span>
                    <strong>{symbol}</strong>
                </div>

                <div className="flex justify-between">
                    <span className="text-zinc-400">Bias</span>
                    <Badge text={bias} />
                </div>

                <div className="flex justify-between">
                    <span className="text-zinc-400">Decision</span>
                    <Badge text={decision} />
                </div>

                <div className="flex justify-between">
                    <span className="text-zinc-400">Market Health</span>
                    <Badge text={marketHealth} />
                </div>

            </div>

        </Card>
    );
}

export default MarketOverviewCard;
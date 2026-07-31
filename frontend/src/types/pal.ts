export interface PALResponse {
    success: boolean;
    symbol: string;
    timestamp: string;

    report: {
        market_health: {
            status: string;
            score: number;
            summary: string | null;
        };

        news: {
            safe_to_trade: boolean;
            summary: string;
            warnings: string[];
            high_impact: string[];
        };

        dxy: {
            trend: string;
            expected_gbp_direction: string;
            aligned: boolean;
            confirmations: string[];
            summary: string;
        };

        pal: {
            overall_bias: string;
            execution_timeframe: string;
            ready_for_entry: boolean;

            workflow: Array<{
                timeframe: string;
                trend: string;
                stage: string;
                grade: string;
                decision: string;
                next_step: string;
                completed_steps: string[];
                missing_steps: string[];
            }>;
        };

        execution: {
            action: string;
            trend: string;
            timeframe: string;
            stage: string;
            reason: string;
            confirmations: string[];
            summary: string;
        };

        ai_commentary: {
            headline: string;
            summary: string;
            market_story: string;
            next_action: string;
            confidence: number;
            risk: string;
            reasoning: string[];
        };

        summary: {
            market: {
                bias: string;
                health: string;
                safe_to_trade: boolean;
            };

            execution: {
                action: string;
                stage: string;
                reason: string;
            };

            dxy: {
                trend: string;
                aligned: boolean;
            };
        };
    };
}
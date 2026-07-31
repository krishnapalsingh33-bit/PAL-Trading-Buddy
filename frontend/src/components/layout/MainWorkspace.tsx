import type { ReactNode } from "react";

type Props = {
    left: ReactNode;
    right: ReactNode;
};

function MainWorkspace({
    left,
    right,
}: Props) {
    return (
        <div className="grid gap-6 xl:grid-cols-[2fr_380px]">

            <section className="space-y-6">
                {left}
            </section>

            <aside className="space-y-6">

                <div className="sticky top-36 space-y-6">

                    {right}

                </div>

            </aside>

        </div>
    );
}

export default MainWorkspace;
import type { ReactNode } from "react";

type Props = {
    title: string;
    children: ReactNode;
};

function Card({ title, children }: Props) {

    return (

        <div className="rounded-2xl border border-zinc-800 bg-zinc-900 p-6 shadow-lg transition-all duration-300 hover:border-zinc-700 hover:shadow-2xl">

            <h2 className="mb-5 text-lg font-semibold tracking-wide text-white">

                {title}

            </h2>

            {children}

        </div>

    );

}

export default Card;
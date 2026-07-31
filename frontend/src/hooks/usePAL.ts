import { useQuery } from "@tanstack/react-query";
import api from "../api/pal";
import type { PALResponse } from "../types/pal";

async function fetchPAL(): Promise<PALResponse> {
    const { data } = await api.get("/pal/analyze/GBPUSD");
    return data;
}

export function usePAL() {
    return useQuery({
        queryKey: ["pal"],
        queryFn: fetchPAL,
        refetchInterval: 5000,
    });
}
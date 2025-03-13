<script setup>
import { useStore } from "vuex";
import NumbersCard from "./NumbersCard.vue";
import EventsTable from "./Graphs/EventsTable.vue";
import BarChart from "./Graphs/BarChart.vue";
import LineGraph from "./Graphs/LineGraph.vue";
import SummaryStatsSection from "@/Layouts/SummaryStatsSection.vue";
import MonthToMonthStatsSection from "@/Layouts/MonthToMonthSection.vue";
import DetailedStatsSection from "@/Layouts/DetailedStatsSection.vue";

const props = defineProps({
    stats: {
        type: Object,
    },
});
const changeFormat = (value) => "+" + value + "%";
const percentage = (partialValue, totalValue) => {
    return (100 * partialValue) / totalValue;
};
const store = useStore();
store.commit("setStats", props.stats);
</script>

<template>
    <div>
        <!--  -->
        <summary-stats-section>
            <template #sum_benefits>
                <numbers-card
                    icon="benefits"
                    :value="
                    store.state.stats.totalBenefits
                    .benefits_last_12_months?.toString()
                    "
                    type="Total Benefits"
                    time_frame="last 12 months"
                    :change="
                        percentage(
                            store.state.stats.totalBenefits
                                .benefits_last_12_months,
                            store.state.stats.totalBenefits.total_benefits / 100
                        )?.toFixed()
                    "
                />
            </template>
            <template #sum_policies>
                <numbers-card
                    icon="policies"
                    :value="
                        store.state.stats.totalPolicies.policies_last_12_months?.toString()
                    "
                    type="Total Polices"
                    time_frame="last 12 months"
                    :change="
                        percentage(
                            store.state.stats.totalPolicies
                                .policies_last_12_months,
                            store.state.stats.totalPolicies.total_policies
                        )?.toLocaleString()
                    "
                />
            </template>
            <template #sum_claims>
                <numbers-card
                    icon="claims"
                    :value="
                        store.state.stats.totalClaims.claims_last_12_months?.toString()
                    "
                    type="Total Claims"
                    time_frame="last 12 months"
                    :change="
                        percentage(
                            store.state.stats.totalClaims.claims_last_12_months,
                            store.state.stats.totalClaims.total_claims
                        )?.toLocaleString()
                    "
                />
            </template>
            <template #sum_newusers>
                <numbers-card
                    icon="general"
                    :value="
                        Number(
                            store.state.stats.averageBenefitsPerPolicy.value
                        ).toFixed(2)
                    "
                    type="Average Benefits"
                    :time_frame="
                        store.state.stats.averageBenefitsPerPolicy
                            .total_benefits +
                        ' / ' +
                        store.state.stats.averageBenefitsPerPolicy
                            .total_policies
                    "
                    :change="'Per policy'"
                />
            </template>
        </summary-stats-section>
        <!--  -->
        <month-to-month-stats-section>
            <template #m2m_policies="{ fromdate, todate }">
                <bar-chart
                    :fromdate="fromdate"
                    :todate="todate"
                    label="Policies By Branch"
                    :data="store.state.stats.policiesByBranch"
                />
            </template>
            <template #m2m_benefits="{ fromdate, todate }">
                <bar-chart
                    :fromdate="fromdate"
                    :todate="todate"
                    label="Benefits By Product"
                    :data="store.state.stats.benefitsByPolicyType || {}"
                />
            </template>
            <template #m2m_claims="{ fromdate, todate }">
                <bar-chart
                    :fromdate="fromdate"
                    :todate="todate"
                    label="Monthly Claims"
                    :data="store.state.stats.monthlyClaims"
                />
            </template>
        </month-to-month-stats-section>
        <!--  -->
        <detailed-stats-section>
            <template #volume_line_graph="{ fromdate, todate }">
                <line-graph
                    :fromdate="fromdate"
                    :todate="todate"
                    label="Benefits by Month"
                    :data="store.state.stats.monthlyBenefits"
                />
            </template>
            <template #events_table="{ fromdate, todate }">
                <events-table
                    :fromdate="fromdate"
                    :todate="todate"
                    :events="store.state.stats.totalClaims.properties || []"
                />
            </template>
        </detailed-stats-section>
    </div>
</template>

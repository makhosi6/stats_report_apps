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
                        store.state.stats.totalBenefits.total_benefits.toString()
                    "
                    type="Total Benefits"
                    time_frame="than last week"
                    :change="
                        store.state.stats.totalBenefits.last_month.toString()
                    "
                />
            </template>
            <template #sum_policies>
                <numbers-card
                    icon="policies"
                    :value="
                        store.state.stats.totalPolicies.total_policies.toString()
                    "
                    type="Total Polices"
                    time_frame="than last month"
                    :change="
                        store.state.stats.totalPolicies.last_month.toString()
                    "
                />
            </template>
            <template #sum_claims>
                <numbers-card
                    icon="claims"
                    :value="
                        store.state.stats.totalClaims.total_claims.toString()
                    "
                    type="Total Claims"
                    time_frame="than last month"
                    :change="
                        store.state.stats.totalClaims.last_month.toString()
                    "
                />
            </template>
            <template #sum_newusers>
                <numbers-card
                    icon="general"
                    :value="store.state.stats.averageBenefitsPerPolicy"
                    type="Average Benefits"
                    time_frame=""
                    :change="'Avarage benefit per policy'"
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
                    label="Most Common Benefits"
                    :data="store.state.stats.mostCommonBenefits || {}"
                />
            </template>
            <template #m2m_claims="{ fromdate, todate }">
                <bar-chart
                    :fromdate="fromdate"
                    :todate="todate"
                    label="Claims"
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
                    label="Recent Claims"
                    :events="store.state.stats.claimsOverTimePeriod"
                />
            </template>
        </detailed-stats-section>
    </div>
</template>

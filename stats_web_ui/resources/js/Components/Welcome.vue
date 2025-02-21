<script setup>
import NumbersCard from "./NumbersCard.vue";
import EventsTable from "./Graphs/EventsTable.vue";
import BarChart from "./Graphs/BarChart.vue";
import LineGraph from "./Graphs/LineGraph.vue";
import SummaryStatsSection from "@/Layouts/SummaryStatsSection.vue";
import MonthToMonthStatsSection from "@/Layouts/MonthToMonthSection.vue";
import DetailedStatsSection from "@/Layouts/DetailedStatsSection.vue";

defineProps({
    stats: {
        type: Object,
    },
});

const changeFormat = (value) => "+" + value + "%";
</script>

<template>
    <div>
        <!--  -->
        <summary-stats-section>
            <template #sum_benefits>
                <numbers-card
                    icon="benefits"
                    :value="stats.totalBenefits.total_benefits.toString()"
                    type="Total Benefits"
                    time_frame="than last week"
                    :change="Math.floor(Math.random() * 100)"
                />
            </template>
            <template #sum_policies>
                <numbers-card
                    icon="policies"
                    :value="stats.monthlyPolicies.total_policies.toString()"
                    type="Total Polices"
                    time_frame="than last week"
                    :change="Math.floor(Math.random() * 100)"
                />
            </template>
            <template #sum_claims>
                <numbers-card
                    icon="claims"
                    :value="stats.totalClaims.total_claims.toString()"
                    type="Total Claims"
                    time_frame="than last week"
                    :change="Math.floor(Math.random() * 100)"
                />
            </template>
            <template #sum_newusers>
                <numbers-card
                    icon="general"
                    :value="'ZAR ' + Math.floor(Math.random() * 100)"
                    type="Average Cover"
                    time_frame="than last week"
                   :change="Math.floor(Math.random() * 100)"
                />
            </template>
        </summary-stats-section>
        <!--  -->
        <month-to-month-stats-section>
            <template #m2m_policies="{ fromdate, todate }">
                <bar-chart :fromdate="fromdate" :todate="todate" />
            </template>
            <template #m2m_benefits="{ fromdate, todate }">
                <bar-chart :fromdate="fromdate" :todate="todate" />
            </template>
            <template #m2m_claims="{ fromdate, todate }">
                <bar-chart :fromdate="fromdate" :todate="todate" />
            </template>
        </month-to-month-stats-section>
        <!--  -->
        <detailed-stats-section>
            <template #volume_line_graph="{ fromdate, todate }">
                <line-graph :fromdate="fromdate" :todate="todate" />
            </template>
            <template #events_table="{ fromdate, todate }">
                <events-table
                    :fromdate="fromdate"
                    :todate="todate"
                    :events="stats.claimsByPolicyType"
                />
            </template>
        </detailed-stats-section>
    </div>
</template>

<script setup>
import ApplicationLogo from "@/Components/ApplicationLogo.vue";
import Placeholder from "@/Components/Placeholder.vue";
import NumbersCard from "./NumbersCard.vue";
import EventsTable from "./Graphs/EventsTable.vue";
import BarChart from "./Graphs/BarChart.vue";
import LineGraph from "./Graphs/LineGraph.vue";
import SummaryStatsSection from "@/Layouts/SummaryStatsSection.vue";
import MonthToMonthStatsSection from "@/Layouts/MonthToMonthSection.vue";
import DetailedStatsSection from "@/Layouts/DetailedStatsSection.vue";
</script>

<template>
    <div>
        <!--  -->
        <summary-stats-section>
            <template #sum_benefits>
                <numbers-card />
            </template>
            <template #sum_policies>
                <numbers-card />
            </template>
            <template #sum_claims>
                <numbers-card />
            </template>
            <template #sum_newusers>
                <numbers-card />
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
                <events-table :fromdate="fromdate" :todate="todate" />
            </template>
        </detailed-stats-section>
    </div>
</template>

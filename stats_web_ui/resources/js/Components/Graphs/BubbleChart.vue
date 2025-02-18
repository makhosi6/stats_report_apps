<template>
    <p>BubbleChart</p>
</template>

<script>
import { Bubble } from "vue-chartjs";
import { Chart as ChartJS } from "chart.js";
import ChartsAndGraphsMixin from "@/mixins/charts_and_graphs";
export default {
    name: "BubbleChart",
    components: { Bubble },
    mixins: [ChartsAndGraphsMixin],
};
</script>

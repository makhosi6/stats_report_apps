<template>
    <Line
        :chartData="{
            ...chartData,
            ...{
                labels: months,
                datasets: chartData?.datasets.map(function (dataset, index) {
                    return {
                        ...dataset,
                        data: points.map((point) => point + index),
                    };
                }),
            },
        }"
        :chartOptions="chartOptions"
    />
</template>

<script>
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from "chart.js";
import { Line } from "vue-chartjs";
import ChartsAndGraphsMixin from '@/mixins/charts_and_graphs'
ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

export default {
    name: "LineGraph",
    components: { Line },
    mixins: [ChartsAndGraphsMixin]
};
</script>

<template>
    <div class="bg-white rounded-lg shadow-md dark:bg-gray-800">
        <Bar
            id="my-chart-id"
            :data="{
                ...chartData,
                ...{
                    labels: months,
                    datasets: chartData?.datasets.map(function (
                        dataset,
                        index
                    ) {
                        return {
                            ...dataset,
                            data: points.map((point) => point + index),
                        };
                    }),
                },
            }"
            :options="chartOptions"
        />
    </div>
</template>

<script>
import { Bar } from "vue-chartjs";
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
} from "chart.js";
import ChartsAndGraphsMixin from '@/mixins/charts_and_graphs'
ChartJS.register(
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale
);

export default {
    name: "BarChart",
    components: { Bar },
    mixins: [ChartsAndGraphsMixin],
};
</script>

export default {
    props: {
        fromdate: {
            type: String,
            required: true,
        },
        todate: {
            type: String,
            required: true,
        },
    },
    watch: {
        fromdate(val) {
            const raw = this.getMonthsBetweenDates(val, this.todate);
            this.months = raw;
            this.points = raw.map((val) => val.length);
        },
        todate(val) {
            const raw = this.getMonthsBetweenDates(this.fromdate, val);
            this.months = raw;
            this.points = raw.map((val) => val.length);
        },
    },
    data() {
        return {
            points: this.getMonthsBetweenDates(this.fromdate, this.todate).map(
                (val) => val.length
            ),
            months: this.getMonthsBetweenDates(this.fromdate, this.todate),
            chartData: {
                labels: [],
                backgroundColor: "#ed2939",
                datasets: [
                    {
                        label: "Dataset Two",
                        pointBackgroundColor: "#4a62ff",
                        backgroundColor: "#4a62ff",
                        borderColor: "#7C8CF8",
                        data: [],
                        fill: true,
                    },
                    {
                        label: "Dataset One",
                        pointBackgroundColor: "red",
                        backgroundColor: "pink",
                        borderColor: "pink",
                        data: [],
                        fill: true,
                    },
                ],
            },
            chartOptions: {
                responsive: true,
                maintainAspectRatio: false,
                aspectRatio: 2,
                animations: {
                    // tension: {
                    //     duration: 1000,
                    //     easing: "easeInOutElastic",
                    //     from: 0,
                    //     to: 0.5,
                    //     loop: false,
                    // },
                    // colors: {
                    //     duration: 1000,
                    //     easing: "linear",
                    //     from: "#fff",
                    //     to: "#7C8CF8",
                    // },
                },
                plugins: {
                    legend: {
                        display: true,
                    },
                },
            },
        };
    },
    methods: {
        getMonthsBetweenDates(startDate, endDate) {
            const months = [];
            const start = new Date(startDate);
            const end = new Date(endDate);
            console.log({ start, end, startDate, endDate });

            while (start <= end) {
                const month = new Intl.DateTimeFormat("en-US", {
                    month: "long",
                    year: "numeric",
                }).format(start);
                months.push(month);
                start.setMonth(start.getMonth() + 1);
            }
            console.log({ months });

            return months;
        },
    },
}

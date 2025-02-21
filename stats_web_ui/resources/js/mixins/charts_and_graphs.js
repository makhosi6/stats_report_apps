export default {
    name: "",
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
            this.debounce(() => {
                this.months = raw;
                this.points = raw.map((val) => val.length);

            }, 1200);
        },
        todate(val) {
            const raw = this.getMonthsBetweenDates(this.fromdate, val);
            this.debounce(() => {
                this.months = raw;
                this.points = raw.map((val) => val.length);

            }, 1200);
        },
    },
    data() {
        return {
            timeout: null,
            points: this.getMonthsBetweenDates(this.fromdate, this.todate).map(
                (val) => val.length
            ),
            months: this.getMonthsBetweenDates(this.fromdate, this.todate),
            chartData: {
                labels: [],
                backgroundColor: "#ed2939",
                datasets: [
                    {
                        label: "Policies",
                        key: "p1",
                        pointBackgroundColor: "#facc15",
                        backgroundColor: "#facc15",
                        borderColor: "#facc15",
                        data: [],
                        fill: true,
                    },
                    {
                        label: "Benefits",
                        key: "b1",
                        pointBackgroundColor: "#4a62ff",
                        backgroundColor: "#4a62ff",
                        borderColor: "#7C8CF8",
                        data: [],
                        fill: true,
                    },
                    {
                        label: "Claims",
                        key: "c1",
                        pointBackgroundColor: "#f9a8d4",
                        backgroundColor: "#f9a8d4",
                        borderColor: "#f9a8d4",
                        data: [],
                        fill: true,
                    },
                    {
                        label: "General",
                        key: "g1",
                        pointBackgroundColor: "#34d399",
                        backgroundColor: "#34d399",
                        borderColor: "#34d399",
                        data: [],
                        fill: true,
                    },
                ],
            },
            chartOptions: {
                responsive: true,
                maintainAspectRatio: false,
                aspectRatio: 1,
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
        /**
         *
         * @param {VoidFunction} callback
         * @param {number} interval -  milliseconds
         */
        debounce(callback, interval = 1000) {
            if (this.timeout) clearTimeout(this.timeout)
            this.timeout = setTimeout(callback, interval)
        },
        getMonthsBetweenDates(startDate, endDate) {
            const months = [];
            const start = new Date(startDate);
            const end = new Date(endDate);

            while (start <= end) {
                const month = new Intl.DateTimeFormat("en-US", {
                    month: "long",
                    year: "numeric",
                }).format(start);
                months.push(month);
                start.setMonth(start.getMonth() + 1);
            }

            return months;
        },
    },
}

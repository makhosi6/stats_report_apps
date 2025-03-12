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
        label: {
            type: String,
            required: true,
        },
        data: {
            type: Object,
            required: false,
        }
    },
    watch: {
        fromdate(val) {
            if (!!this.data?.entries) {
                const raw = this.getMonthsBetweenDates(val, this.todate);
                this.debounce(() => {
                    this.months = raw;
                    this.points = raw.map((val) => val.length);

                }, 1200);
            }
        },
        todate(val) {
            if (!!this.data?.entries) {
                const raw = this.getMonthsBetweenDates(this.fromdate, val);
                this.debounce(() => {
                    this.months = raw;
                    this.points = raw.map((val) => val.length);

                }, 1200);
            }
        },
    },
    data() {
        return {
            timeout: null,
            points: (!!this.data?.entries) ? this.data : Object.values(this.data|| {}),
            months: (!!this.data?.entries) ? this.getMonthsBetweenDates(this.fromdate, this.todate) : Object.keys(this.data || {}),
            chartData: {
                labels: [],
                backgroundColor: "#ed2939",
                datasets: [

                    {
                        label: this.label,
                        key: "b1",
                        pointBackgroundColor: "#4a62ff",
                        backgroundColor: "#4a62ff",
                        borderColor: "#7C8CF8",
                        data: [],
                        fill: true,
                    }
                ],
            },
            chartOptions: {
                responsive: true,
                maintainAspectRatio: false,
                aspectRatio: 1,
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

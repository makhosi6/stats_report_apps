    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-body">
                        <div id="container"></div>
                    </div>
                </div>
            </div>
        </div>
        <script src="https://code.highcharts.com/highcharts.js"></script>
    <script type="text/javascript">

        Highcharts.chart('container', {
            title: {
                text: 'New User Growth, 2020'
            },
            subtitle: {
                text: 'Source: positronx.io'
            },
            xAxis: {
                categories: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                    'October', 'November', 'December'
                ]
            },
            yAxis: {
                title: {
                    text: 'LPAS Users Stats'
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle'
            },
            plotOptions: {
                series: {
                    allowPointSelect: true
                }
            },
            series: [
                {
                name: '23',
                data: <?php echo json_encode($user_acquisition); ?>
            },
            {
                name: '24',
                data: <?php echo json_encode($users_activity); ?>
            }],
            responsive: {
                rules: [{
                    condition: {
                        maxWidth: 500
                    },
                    chartOptions: {
                        legend: {
                            layout: 'horizontal',
                            align: 'center',
                            verticalAlign: 'bottom'
                        }
                    }
                }]
            }
        });
    </script>
</div>

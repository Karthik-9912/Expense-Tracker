let expenseChart,incomeChart

function fetchChartData(){
    fetch('/app/chart-data/')
    .then(response => response.json())
    .then(data=>{
        const expenseData=data.expense_data;
        const incomeData=data.income_data;

        if(expenseChart) expenseChart.destroy();
        if(incomeChart) incomeChart.destroy();

        // expense piechart
        const ctx1 = document.getElementById('expenseChart').getContext('2d');
        expenseChart=new Chart(ctx1,{
            type:'pie',
            data:{
                labels:expenseData.labels,
                datasets:[{
                    data:expenseData.data,
                    backgroundColor:['#FF6384', '#36A2EB', '#FFCE56', '#2ECC71', '#9B59B6']
                }]
            }
        });

        // income piechart
        // const ctx1_1 = document.getElementById('incomeChart').getContext('2d');
        // incomeChart=new Chart(ctx1_1,{
        //     type:'pie',
        //     data:{
        //         labels:incomeData.labels,
        //         datasets:[{
        //             data:incomeData.data,
        //             backgroundColor:['#FF6384', '#36A2EB', '#FFCE56', '#2ECC71', '#9B59B6']
        //         }]
        //     }
        // });
    

    // Income BarChart
    const ctx2 = document.getElementById('incomeChart').getContext('2d');
        incomeChart = new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: incomeData.labels,
                datasets: [{
                    label: 'Income',
                    data: incomeData.data,
                    backgroundColor: '#36A2EB'
                }]
            },
            options: { scales: { y: { beginAtZero: true } } }
        });
    })
    .catch(err => console.error("Error fetching chart data:", err)); 
}

fetchChartData()


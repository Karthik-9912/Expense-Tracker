let expenseChart,incomeChart
let expenseColors=[];


function fetchChartData(){

    fetch('/app/chart-data/')
    .then(response => response.json())
    .then(data=>{
        const expenseData=data.expense_data;
        const incomeData=data.income_data;

        if(expenseChart) expenseChart.destroy();
        if(incomeChart) incomeChart.destroy();

        // 
        while(expenseColors.length<expenseData.data.length){
            expenseColors.push(`hsl(${Math.floor(Math.random()*360)},70%,60%)`);
        }

        // expense piechart
        const ctx1 = document.getElementById('expenseChart').getContext('2d');
        expenseChart=new Chart(ctx1,{
            type:'pie',
            data:{
                labels:expenseData.labels,
                datasets:[{
                    data:expenseData.data,
                    backgroundColor:expenseColors
                }]
            }
        });
    

    // Income BarChart
    const ctx2 = document.getElementById('incomeChart').getContext('2d');
        incomeChart = new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: incomeData.labels,
                datasets: [{
                    label: 'Income',
                    data: incomeData.data,
                    backgroundColor: ["#1e1b4b","#ef4444","#84cc16","#06b6d4","#8b5cf6","#0ea5e9","#ec4899"]
                }]
            },
            options: { scales: { y: { beginAtZero: true } } }
        });
    })
    .catch(err => console.error("Error fetching chart data:", err)); 


    // Line Chart
    
}

fetchChartData()


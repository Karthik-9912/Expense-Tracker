let expenseChart,incomeChart,lineChart
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

        // Line Chart

const ctx3 = document.getElementById("lineChart").getContext("2d");

const allLabels = [...new Set([...incomeData.labels, ...expenseData.labels])];

function getAlignedData(labels, dataObj) {
  return labels.map(label => {
    const index = dataObj.labels.indexOf(label);
    return index !== -1 ? dataObj.data[index] : 0;
  });
}

const alignedIncomeData = getAlignedData(allLabels, incomeData);
const alignedExpenseData = getAlignedData(allLabels, expenseData);

lineChart = new Chart(ctx3, {
  type: 'line',
  data: {
    labels: allLabels,
    datasets: [
      {
        label: 'Income',
        data: alignedIncomeData,
        borderColor: '#3b82f6',
        backgroundColor: '#3b82f6',
        borderWidth: 3,
        tension: 0.3,
        fill: false,
        pointRadius: 5,
        pointHoverRadius: 7,
        pointBackgroundColor: '#ffffff',
        pointBorderColor: '#3b82f6',
        pointBorderWidth: 3,
      },
      {
        label: 'Expense',
        data: alignedExpenseData,
        borderColor: '#ef4444',
        backgroundColor: '#ef4444',
        borderWidth: 3,
        tension: 0.3,
        fill: false,
        pointRadius: 5,
        pointHoverRadius: 7,
        pointBackgroundColor: '#ffffff',
        pointBorderColor: '#ef4444',
        pointBorderWidth: 3,
      }
    ]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Income vs Expense Trend' },
      tooltip: {
        callbacks: {
          label: function(context) {
            const label = context.dataset.label || '';
            return `${label}: ${context.raw.toLocaleString()}`;
          }
        }
      }
    },
    scales: {
      y: { beginAtZero: true }
    }
  }
});


    })
    .catch(err => console.error("Error fetching chart data:", err));  
}

fetchChartData()


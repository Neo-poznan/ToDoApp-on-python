let data = {
    labels: dataset.categories,
    datasets: [{
        data: dataset.data,
        backgroundColor: dataset.colors,
        hoverOffset: 4,
        borderColor: border,
    }]
};

let config = {
    type: 'pie',
    data: data,
};

let pieChart = new Chart(
    document.getElementById('pie-chart'),
    config
);
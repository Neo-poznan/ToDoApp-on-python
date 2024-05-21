let data = {
    labels: ['Спортивные нагрузки', 'Программирование', 'Работа по дому', 'Важные встречи', 'Рабочие Задачи', 'Развлечения'],
    datasets: [{
        data: [12, 19, 3, 5, 2, 3], // Здесь данные с сервера
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
        ],
        hoverOffset: 4
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
// функция получение csrf токена
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


// Функция отправки формы fetch

async function postData(url = '', data = {}) {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: data
        });

        const jsonResponse = await response.json(); // Парсинг JSON ответа

        if (jsonResponse.success === 'success') {
            // Если операция успешна, перенаправляем пользователя
            window.location.href = '/to-do-list/index/'; // URL для перенаправления
        } else if (jsonResponse.error) {
            // Если есть ошибка, выводим её на экран
            alert('Ошибка: ' + jsonResponse.error);  // потом сделаю нормальный вывод ошибки а пока alert
        }
    } catch (error) {
        console.error('Ошибка:', error);
    }
}

// отправка
//let form = document.getElementById('form'); // переменная с формой
// при отправке формы любым способом
form.addEventListener('submit', function (event) {
    // запрещаем стандартное действие
    event.preventDefault();
    // создаем объект формы в формате json
    let object = {};
    let formData = new FormData(document.forms.taskcreationform);

    formData.forEach(function(value, key){
        object[key] = value;
    });
    let data = JSON.stringify(object);

    // передаем в фукцию fetch данные и получаем результат
    postData(window.location.href, data)
})





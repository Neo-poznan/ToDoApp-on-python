let dragged;

// перетаскивание элементов
document.addEventListener("dragstart", function(event) {
    dragged = event.target;
    event.dataTransfer.setData('text/plain', null);
});

document.addEventListener("dragover", function(event) {
    event.preventDefault();
    let target = getClosestTask(event.target);
    target.style.border = "4px dashed " + task_border; // цвет зависит от темы
});

document.addEventListener("dragleave", function(event) {
    let target = getClosestTask(event.target);
    target.style.border = "1px solid #ccc";
});

document.addEventListener("drop", function(event) {
    event.preventDefault();
    let target = getClosestTask(event.target);
    target.style.border = "1px solid #ccc";
    target.parentNode.insertBefore(dragged, target);
    sendTaskOrderToServer();
});

function getClosestTask(el) {
    if (el.className === 'task-item') {
        return el;
    } else {
        return getClosestTask(el.parentNode);
    }
}

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

// отправляет на сервер данные о текущем расположении элементов

function sendTaskOrderToServer() {
    let tasks = Array.from(document.getElementsByClassName('task-item'));
    let taskOrder = tasks.map(task => task.id);
    fetch('/to-do-list/update-task-order/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({order: taskOrder}),
    }).then(response => {
        if (response.ok) {
            window.location.reload();  // Принудительная перезагрузка страницы
        }
    });
}

// выпадающий список 

/* Когда пользователь нажимает на кнопку,
переключение между скрытием и отображением раскрывающегося содержимого */
function DropDown() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Закройте выпадающее меню, если пользователь щелкает за его пределами
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }


document.addEventListener('DOMContentLoaded', function() {
  const themeSwitch = document.getElementById('theme-switch');

  themeSwitch.addEventListener('change', function() {
    // Определение текущей темы на основе состояния переключателя
    const theme = this.checked ? 'Темная' : 'Светлая';

    // Изменение класса темы для body
    document.body.className = theme + '-mode';

    // Отправка новой темы на сервер
    fetch('/to-do-list/set-theme/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken, // Убедитесь, что csrftoken корректно получен
      },
      body: JSON.stringify({ theme: theme })
    }).then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      else {
        setTimeout(() => { window.location.reload(); }, 500);
      }
      return response.json();
    }).then(data => {
      console.log('Theme updated:', data);
    }).catch(error => {
      console.error('Error updating theme:', error);
    });
  });
});


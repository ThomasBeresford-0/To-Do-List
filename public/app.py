const form = document.getElementById('task-form');
const taskInput = document.getElementById('task-input');
const taskList = document.getElementById('task-list');

form.addEventListener('submit', function(event) {
  event.preventDefault();
  const taskText = taskInput.value.trim();
  if (taskText === '') return;
  
  const taskItem = createTaskItem(taskText);
  taskList.appendChild(taskItem);
  taskInput.value = '';
});

function createTaskItem(taskText) {
  const li = document.createElement('li');
  li.innerHTML = `
    <span>${taskText}</span>
    <button class="delete-button">Delete</button>
  `;
  li.querySelector('.delete-button').addEventListener('click', function() {
    li.remove();
  });
  return li;
}

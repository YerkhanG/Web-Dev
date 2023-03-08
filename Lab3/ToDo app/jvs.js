let createNewTask = function(taskString) {

    let nTask = document.createElement("li");
    nTask.className = "task";


    let box = document.createElement("input");
    box.className = "c-boxes";
    box.type = "checkbox";
    box.onclick = stroked_element;
    
    
    let deleteButton = document.createElement("img");
    deleteButton.src = "https://cdn-icons-png.flaticon.com/512/860/860829.png";
    deleteButton.className = "delete";
    deleteButton.onclick = deleteItem;


    
    let span = document.createElement("span");
    span.className = "span";

    

    span.innerHTML = taskString;
    nTask.appendChild(box);
    nTask.appendChild(span);
    nTask.appendChild(deleteButton);

    return nTask
}

let deleteItem = function() {
    
    let listItem = this.parentNode;
    listItem.remove();
    
}



let addItem = function() {
    
    let tasks = document.getElementById("task");
    let task = document.getElementById("main");
    if(task.value === "") {
        alert("Write something!")
    } else {
        let Item = createNewTask(task.value);
        tasks.appendChild(Item);
    }
    task.value = "";
}

function stroked_element(){
    let element = event.currentTarget.parentElement;
    if(element.classList.contains('stroked')){
        element.classList.remove('stroked');
    }else{
        element.classList.add('stroked');
    }
}

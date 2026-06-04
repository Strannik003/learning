#Сделай консольное приложение “Менеджер задач”.

# Функции:

# добавить задачу
# посмотреть все задачи
# отметить задачу выполненной
# удалить задачу
# сохранить задачи в .json
# загрузить задачи при запуске программы

# Структура задачи:

# {
#     "id": 1,
#     "title": "Выучить open()",
#     "done": False
# }

import json
id_global = 0
with open("tasks.json","r", encoding="utf-8") as file:
    tasks= json.load(file)
for task in tasks:
     if task["id"] > id_global:
         id_global = task["id"]
         

def add_task(title):
    global id_global
    task = {
    "id": id_global+1,
    "title":  title,
    "done": False
    }
    id_global += 1
    tasks.append(task)
    return tasks

def task_complete(id):
    for task in tasks:
        if task["id"] == id:
            task["done"] = True
    return tasks

def delete(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            break 
    return tasks

def show_all_tasks():
    print(tasks)

def save_as_json():
    with open("tasks.json","w", encoding="utf-8") as file:
        json.dump(tasks,file,indent=4, ensure_ascii=False)

add_task("dffddf")
add_task("dffddf")
task_complete(2)
show_all_tasks()
save_as_json()
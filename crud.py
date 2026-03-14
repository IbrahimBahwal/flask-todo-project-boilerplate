import helpers

def create_todo():
    return

def get_todo_by_id(todo_id):
    tasks = helpers.read_db_file()
    for task in tasks:
        if task['id'] == todo_id:
            return task

def update_todo(todo_id, update_data):
    task = get_todo_by_id(todo_id)

    tasks = helpers.read_db_file()
    tasks.remove(task)

    if "title" in update_data:
        task['title'] = update_data['title']
    if "description" in update_data:
        task['title'] = update_data['title']

    tasks.append(task)
    helpers.write_db_file(tasks)

    return task

def delete_todo(todo_id)
    task = get_todo_by_id(todo_id)
    
    tasks = helpers.read_db_file()
    tasks.remove(task)
    
    helpers.write_db_file(tasks)

    return
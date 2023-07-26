import mysql.connector
import colorama
import json
from colorama import Fore, Style
from essencials import ct

colorama.init()

# Estabelecer a conexão com o banco de dados
db_connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    database='todo_list'
)

db_cursor = db_connection.cursor()

check = '✅'
ncheck = '[ ]'

# Função para carregar as traduções do arquivo lang.json
def load_translations():
    with open('lang.json', 'r', encoding='utf-8') as lang_file:
        lang_data = json.load(lang_file)
        lang = lang_data['lang']
        translations = lang_data['translations']
        return lang, translations

def add_task(task_number, task_description):
    ct()
    task_description = task_description.capitalize()
    sql = "INSERT INTO lista (id, tarefa) VALUES (%s, %s)"
    val = (task_number, task_description)
    db_cursor.execute(sql, val)
    db_connection.commit()

def get_next_task_id():
    db_cursor.execute("SELECT MAX(id) FROM lista")
    max_id = db_cursor.fetchone()[0]
    return max_id + 1 if max_id is not None else 1

def show_tasks(translations):
    db_cursor.execute("SELECT * FROM lista")
    tasks = db_cursor.fetchall()

    if len(tasks) == 0:
        print(Fore.RED + translations['no_tasks'] + Style.RESET_ALL)
        input(Fore.GREEN + translations['follow'] + Style.RESET_ALL)
        ct()
    else:
        for task in tasks:
            task_number = task[0]
            task_description = task[1]
            completed = task[2]
            status = check if completed == 'C' else ncheck
            print(Fore.BLUE + translations['task'] + f' {task_number}: {task_description} {"✅" if completed == "C" else "[ ]"}' + Style.RESET_ALL)

        p = int(input(Fore.GREEN + translations['choose_option'] + '\n[1] ' + translations['complete_task'] + '\n[2] ' +  translations['delete_task'] + '\n[3] ' +  translations['delete_all_tasks'] + '\n[4] ' + translations['no_option'] + '\nR: ' + Style.RESET_ALL))
        if p == 1:
            task_number = int(input(Fore.GREEN + translations['complete_task_input'] + ' ' + Style.RESET_ALL))
            mark_task_complete(task_number)
            print(Fore.BLUE + translations['complete_task_succes'] + Style.RESET_ALL)
        elif p == 2:
            task_number = int(input(Fore.GREEN + translations['delete_task_input'] + ' ' + Style.RESET_ALL))
            print(Fore.RED + translations['delete_task_success'].format(task_number=task_number) + Style.RESET_ALL)
            delete_task(task_number)
        elif p == 3:
            delete_all_tasks()
            print(Fore.RED + translations['delete_all_tasks_success'] + Style.RESET_ALL)
        elif p == 4:
            ct()
            pass

def mark_task_complete(task_number):
    sql = "UPDATE lista SET stts = 'C' WHERE id = %s"
    val = (task_number,)
    db_cursor.execute(sql, val)
    db_connection.commit()

def delete_task(task_number):
    sql_delete = "DELETE FROM lista WHERE id = %s"
    val_delete = (task_number,)
    db_cursor.execute(sql_delete, val_delete)
    db_connection.commit()

    # Renumerar as tarefas após a exclusão
    sql_update = "UPDATE lista SET id = id - 1 WHERE id > %s"
    val_update = (task_number,)
    db_cursor.execute(sql_update, val_update)
    db_connection.commit()

    # Atualizar o valor AUTO_INCREMENT para evitar conflitos de índices
    sql_reset_auto_increment = "ALTER TABLE lista AUTO_INCREMENT = 1"
    db_cursor.execute(sql_reset_auto_increment)
    db_connection.commit()

def delete_all_tasks():
    sql_delete_all = "DELETE FROM lista"
    db_cursor.execute(sql_delete_all)
    db_connection.commit()

def main():
    ct()
    lang, translations = load_translations()
    print(Fore.BLUE + translations[lang]['welcome_message'] + Style.RESET_ALL)
    while True:
        choice = int(input(Fore.GREEN + translations[lang]['choose_option'] + '\n[1] ' + translations[lang]['show_tasks'] + '\n[2] ' + translations[lang]['add_task'] + '\n[3] ' + translations[lang]['exit'] + '\nR: ' + Style.RESET_ALL))

        if choice == 1:
            ct()
            show_tasks(translations[lang])

        elif choice == 2:
            ct()
            task_description = input(Fore.GREEN + translations[lang]['add_task_input'] + ' ' + Style.RESET_ALL)
            next_id = get_next_task_id()
            add_task(next_id, task_description)
                        
        elif choice == 3:
            ct()
            break

if __name__ == '__main__':
    main()

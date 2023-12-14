import sqlite3
import easygui

# Создаем подключение к базе данных
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# Создаем таблицу, если её нет
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        number TEXT NOT NULL
    )
''')
conn.commit()

def add_contact(name, number):
    cursor.execute('INSERT INTO contacts (name, number) VALUES (?, ?)', (name, number))
    conn.commit()
    easygui.msgbox(f"Контакт '{name}' добавлен успешно.", "Успех")

def view_contacts():
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    if contacts:
        for contact in contacts:
            print(f"{contact[0]}. {contact[1]}: {contact[2]}")
    else:
        print("Телефонный справочник пуст.")

def search_contact(name):
    cursor.execute('SELECT * FROM contacts WHERE name LIKE ?', (f'%{name}%',))
    result = cursor.fetchall()
    if result:
        for contact in result:
            print(f"{contact[0]}. {contact[1]}: {contact[2]}")
    else:
        print(f"Контакт с именем '{name}' не найден.")

def delete_contact(contact_id):
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()
    print("Контакт удален успешно.")

def update_contact(contact_id, new_number):
    cursor.execute('UPDATE contacts SET number = ? WHERE id = ?', (new_number, contact_id))
    conn.commit()
    print("Контакт обновлен успешно.")

while True:
    choice = easygui.buttonbox("Выберите действие:", choices=["Просмотреть контакты", "Добавить контакт", "Искать контакт", "Удалить контакт", "Обновить контакт", "Выйти"])

    if choice == "Просмотреть контакты":
        view_contacts()
    elif choice == "Добавить контакт":
        name = easygui.enterbox("Введите имя контакта:")
        number = easygui.enterbox("Введите номер телефона:")
        add_contact(name, number)
    elif choice == "Искать контакт":
        name = easygui.enterbox("Введите имя контакта для поиска:")
        search_contact(name)
    elif choice == "Удалить контакт":
        contact_id = easygui.enterbox("Введите ID контакта для удаления:")
        delete_contact(contact_id)
    elif choice == "Обновить контакт":
        contact_id = easygui.enterbox("Введите ID контакта для обновления:")
        new_number = easygui.enterbox("Введите новый номер телефона:")
        update_contact(contact_id, new_number)
    elif choice == "Выйти":
        break
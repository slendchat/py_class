from func import *

while True:
    print("\nМеню:")
    print("1. Добавить нового автора")
    print("2. Добавить книгу к существующему автору")
    print("3. Просмотреть список авторов и их книг")
    print("4. Вывести сколько книг у каждого автора")
    print("5. Удалить автора и все его книги")
    print("6. Выход из программы\n")
    choice = input("Выберите действие (1-6): ")
    if choice == '1':
        author = input("Введите фамилию нового автора: ")
        add_author(author)
    elif choice == '2':
        list_authors()
        author = input("Введите фамилию автора, к которому хотите добавить книгу: ")
        book = input("Введите название книги: ")
        add_book(author, book)
    elif choice == '3':
        list_authors_books()
    elif choice == '4':
        count_books()
    elif choice == '5':
        list_authors()
        author = input("Введите фамилию автора, которого хотите удалить: ")
        delete_author(author)
    elif choice == '6':
        print("Выход из программы")
        break
    else:
        print("Некорректный ввод. Пожалуйста, выберите действие из меню.")
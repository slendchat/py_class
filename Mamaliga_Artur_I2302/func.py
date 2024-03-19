
author_dict = dict()

# отличие list() от []. list() это вызов конструктора списка, а [] это литерал списка (синтаксический сахар). 
#Я считаю что вызов функции list() повышает читаемость и явно говорит о создании пустого списка
def add_author(author):
    if not author:
        print("Вы не ввели фамилию автора, попробуйте снова")
    elif author in author_dict:
        print("Такой автор уже существует.")
    else:
        author_dict[author] = list() # добавление нового ключа в словарь со значением пустой список
        print(f"Автор {author} успешно добавлен.")

def list_authors():
    print("Список авторов:")
    for author in author_dict.keys():
        print(author)

def add_book(author, book):
    # проверка условий для работы корректной работы функции.
    if not author:
        print("Вы не ввели фамилию автора.")
    elif author not in author_dict.keys():
        print("Такого автора нет.")
    elif not book:
        print("Вы не ввели название книги.")
    elif book in author_dict[author]:
        print("Такая книга уже есть в списке у этого автора.")
    else:
        author_dict[author].append(book) 
        print(f"Книга '{book}' успешно добавлена автору {author}.")



def list_authors_books():
    print("Список авторов и их книг:")
    for author, books in author_dict.items():
        print(f"{author}: {', '.join(books)}")


def count_books():
    print("Количество книг у каждого автора:")
    for author, books in author_dict.items():
        print(f"{author}: {len(books)} книг")


def delete_author(author):
    if not author:
        print("Вы не ввели фамилию автора.")
    elif author not in author_dict:
        print("Такого автора нет.")
    else:
        del author_dict[author]
        print(f"Автор {author} и все его книги успешно удалены.")




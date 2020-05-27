from address_book import AddressBook


print(
    'Доступны след. команды: '
    '\nДобавить'
    '\nУдалить'
    '\nПоказать'
    '\nЗакрыть')

address_book = AddressBook()
address_book.contacts = address_book.download_data_from_file()

while True:
    command = input('Введите команду:')
    if command == "Добавить":
        address_book.add_contact()
        a = address_book.contacts[-1]
        address_book.save_contact_to_file(a)
    if command == "Удалить":
        key_del = int(input('Введите ключ контакта, который хотите удалить:'))
        address_book.delete_contact(key_del)
        address_book.update_file_after_deleted_contact()
    if command == "Показать":
        address_book.show_this_shit()
    if command == "Закрыть":
        break

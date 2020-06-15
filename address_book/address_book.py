import time
from address_book.contact import Contact


def stopwatch(func):
    def nu_ok(*args, **kwargs):
        start = float(time.time())
        result = func(*args, **kwargs)
        end = float(time.time())
        spend_time = end - start
        print('Время на работу с файлами:' + str("%.4f" % spend_time))
        return result
    return nu_ok


class AddressBook:
    def __init__(self):
        self.contacts = [];

    def add_contact(self):
        first_name = input('Введите имя:')
        last_name = input('Введите фамилию:')
        email = input('Введите почту:')
        phone = input('Введите телефон:')
        job = input('Введите место работы:')
        self.contacts.append(Contact(first_name, last_name, email, phone, job))
        print('Ваш контакт добавлен')

    def delete_contact(self, key):
        self.contacts.pop(key)

    def show_this_shit(self):
        for i, contact in enumerate(self.contacts):
            print('Ключ:', i, contact)

    @stopwatch
    def save_contact_to_file(self, a):
        with open("ab.txt", "a") as f:
            f.write(str(a) + '\n')

    @stopwatch
    def download_data_from_file(self):
        with open("ab.txt", "r") as f:
            save_address_book = [line.strip() for line in f]
        return save_address_book

    @stopwatch
    def update_file_after_deleted_contact(self):
        with open("ab.txt", "w") as f:
            for contact in self.contacts:
                f.write(str(contact) + '\n')



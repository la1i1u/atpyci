import unittest


class Contact:
    def __init__(self, first_name, last_name, email, phone, job):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.job = job

    def __repr__(self):
        return "{" + self.first_name + " " + self.last_name + " " + self.email + " " + self.phone + " " + self.job + "}"


class TestContact(unittest.TestCase):
    def setUp(self):
        self.arguments = ["first_name", "last_name", "email", "phone", "job"]
        self.contact = Contact(*self.arguments)

    def test_first_name_is_first(self):
        self.assertEqual(self.contact.first_name, self.arguments[0], "халоу имя норм")


if __name__ == '__main__':
    unittest.main()

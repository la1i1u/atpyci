class Contact:
    def __init__(self, first_name, last_name, email, phone, job):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.job = job

    def __repr__(self):
        return "{" + self.first_name + " " + self.last_name + " " + self.email + " " + self.phone + " " + self.job + "}"

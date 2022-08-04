class Person(object):
    def __init__(self, id_person=None, name=None, lastname=None, email=None):
        self._id_person = id_person
        self._name = name
        self._lastname = lastname
        self._email = email

    @property
    def id_person(self):
        return self._id_person

    @id_person.setter
    def id_person(self, id_person):
        self._id_person = id_person

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):
        return f'ID: {self.id_person}\nName: {self.name}\nLastname: {self.lastname}' \
               f'\nEmail: {self.email}\n'

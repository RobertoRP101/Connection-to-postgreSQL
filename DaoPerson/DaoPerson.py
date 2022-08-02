from ConnectionDB.ConnectionDB import ConnectionDB
from Person.Person import Person
from logger_base import log


class DaoPerson(object):
    _SELECT: str = 'SELECT * FROM public.\"Person\"'
    _INSERT: str = 'INSERT INTO public.\"Person\"(name, lastname, email) VALUES(%s, %s, %s)'
    _UPDATE: str = 'UPDATE public.\"Person\" SET name=%s, lastname=%s, email=%s WHERE id_person=%s'
    _DELETE: str = 'DELETE FROM public.\"Person\" WHERE id_person=%s'

    @classmethod
    def select(cls):
        with ConnectionDB.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(cls._SELECT)
                registers = cursor.fetchall()
                people: list = []
                for register in registers:
                    person: object = Person(register[0], register[1], register[2], register[3])
                    people.append(person)
                return people

    @classmethod
    def insert(cls, person):
        with ConnectionDB.getConnection() as connection:
            with connection.cursor() as cursor:
                attributes: tuple = (person.name, person.lastname, person.email)
                cursor.execute(cls._INSERT, attributes)
                return cursor.rowcount

    @classmethod
    def update(cls, person):
        with ConnectionDB.getConnection() as connection:
            with connection.cursor() as cursor:
                attributes = (person.name, person.lastname, person.email, person.id_person)
                cursor.execute(cls._UPDATE, attributes)
                return cursor.rowcount

    @classmethod
    def delete(cls, person):
        with ConnectionDB.getConnection() as connection:
            with connection.cursor() as cursor:
                attribute: tuple = (person.id_person,)
                cursor.execute(cls._DELETE, attribute)
                return cursor.rowcount


alice = Person(name='Mary', lastname='Smith', email='alicieGe@gmail.com')
sandra = Person(9, 'Sandra', 'Medardo', 'sandraMe@gmail.com')
death = Person(id_person=10)
print(DaoPerson.delete(death))
print(DaoPerson.update(sandra))
peoplet = DaoPerson.select()
for persont in peoplet:
    log.debug(f'\n{persont}')

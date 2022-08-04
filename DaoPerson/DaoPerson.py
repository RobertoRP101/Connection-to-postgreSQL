from Person.Person import Person
from Pool_Cursor import PoolCursor


class DaoPerson(object):
    _SELECT: str = 'SELECT * FROM public.\"Person\"'
    _INSERT: str = 'INSERT INTO public.\"Person\"(name, lastname, email) VALUES(%s, %s, %s)'
    _UPDATE: str = 'UPDATE public.\"Person\" SET name=%s, lastname=%s, email=%s WHERE id_person=%s'
    _DELETE: str = 'DELETE FROM public.\"Person\" WHERE id_person=%s'

    @classmethod
    def select(cls):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT)
            registers = cursor.fetchall()
            people: list = []
            for register in registers:
                person: object = Person(register[0], register[1], register[2], register[3])
                people.append(person)
            return people

    @classmethod
    def insert(cls, person):
        with PoolCursor() as cursor:
            attributes: tuple = (person.name, person.lastname, person.email)
            cursor.execute(cls._INSERT, attributes)
            return cursor.rowcount

    @classmethod
    def update(cls, person):
        with PoolCursor() as cursor:
            attributes = (person.name, person.lastname, person.email, person.id_person)
            cursor.execute(cls._UPDATE, attributes)
            return cursor.rowcount

    @classmethod
    def delete(cls, person):
        with PoolCursor() as cursor:
            attribute: tuple = (person.id_person,)
            cursor.execute(cls._DELETE, attribute)
            return cursor.rowcount

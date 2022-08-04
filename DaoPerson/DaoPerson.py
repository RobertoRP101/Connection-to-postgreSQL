from Person.Person import Person
from Pool_Cursor import PoolCursor
from logger_base import log


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


option: str = ''
while option != '5':
    print(f'Menu'.center(50, '-'))
    print(f'1.- Show all registers.')
    print(f'2.- Insert a new person.')
    print(f'3.- Update a person into the database.')
    print(f'4.- Delete a person into the database.')
    print(f'5.- Exit')
    option = input('Select an available digit: ')
    if option == '1':
        peoplet: list = DaoPerson.select()
        for persont in peoplet:
            print(f'\n{persont}')
    elif option == '2':
        name: str = input('Insert the name: ')
        lastname: str = input('Insert the lastname: ')
        email: str = input('Insert the email: ')
        print(f'Registers affedcted: {DaoPerson.insert(Person(name=name, lastname=lastname, email=email))}')
    elif option == '3':
        id_person: int = int(input('Insert the id person: '))
        name: str = input('Insert the name: ')
        lastname: str = input('Insert the lastname: ')
        email: str = input('Insert the email: ')
        print(f'Registers affedcted: {DaoPerson.update(Person(id_person, name, lastname, email))}')
    elif option == '4':
        id_person: int = int(input('Insert the id person: '))
        print(f'Registers affedcted: {DaoPerson.delete(Person(id_person=id_person))}')
    else:
        print('Exit')


# alice = Person(name='Mary', lastname='Smith', email='alicieGe@gmail.com')
# sandra = Person(9, 'Sandra', 'Medardo', 'sandraMe@gmail.com')
# print(DaoPerson.update(sandra))
# peoplet = DaoPerson.select()
# for persont in peoplet:
#     log.debug(f'\n{persont}')

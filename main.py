from DaoPerson.DaoPerson import DaoPerson
from Person.Person import Person


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

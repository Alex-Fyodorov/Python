def initial_notes(): # Этот метод используется только в самый первый раз, чтобы были хоть какие-то записи, с которыми можно работать. Поэтому обращение к этому методу закомментировано.
    write_note('Горбачёв Михаил Сергеевич 11111 \n')
    write_note('Брежнев Леонид Ильич 22222\n')
    write_note('Хрущёв Никита Сергеевич 33333\n')
    write_note('Андропов Юрий Владимирович 44444\n')
    write_note('Черненко Константин Устинович 55555\n')

def write_note(str):
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(str)

def add_note(): # Добавление записи.   
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')    
    patronymic = input('Введите отчество: ')
    phonenumber = input('Введите номер телефона: ')
    while not phonenumber.isdigit():
        phonenumber = input('Введите номер телефона: ')
    str = f'{surname} {name} {patronymic} {phonenumber}\n'
    write_note(str)

def find_note(str): # Данный метод используется и для поиска, и для вывода всего списка. На семинаре весь список не хотел выводиться, но я допилил (при проверке добавил or), и теперь всё работает как надо.     
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if str.lower() in line.lower().split() or str == '':
                print (line, end = '')                

def edit_note(str, edit): # Данный метод служит и для редакции, и для удаления.        
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        lst = data.readlines()
        for i in range(len(lst)):
            if str.lower() in lst[i].lower().split():
                if edit:
                    lst[i] = edit_mode(lst[i])                    
                else:
                    lst[i] = ''                
    with open('phonebook.txt', 'w', encoding='utf-8') as data:
        for line in lst:
            data.write(line)

def edit_mode(str): # Режим изменения записи.
    str = list(str.split())
    while True:
        print()
        for i in range(len(str)):
            print(f'{i + 1}. {str[i]}')
        print('5. Выйти из режима редактирования.')
        num = '0'
        while num == '' or num not in '12345':
            num = input('Введите номер пункта, который хотите отредактировать: ')
        if num == '1':
            str[0] = input('Введите новую фамилию: ')
        if num == '2':
            str[1] = input('Введите новое имя: ')
        if num == '3':
            str[2] = input('Введите новое отчество: ')
        if num == '4':
            str[3] = input('Введите новый номер телефона: ')
            while not str[3].isdigit():
                str[3] = input('Введите номер телефона: ')
        if num == '5':
            break
    return f'{str[0]} {str[1]} {str[2]} {str[3]}\n'
    

# initial_notes()
while True:
    com = input('\nВведите одну из команд:\nadd, all, find, del, edit, stop:  ')
    print()
    if com.lower() == 'stop':
        break
    if com.lower() == 'add':
        add_note()
    if com.lower() == 'find':
        str = input('Какую запись ищете? ')
        find_note(str)
    if com.lower() == 'all':
        find_note('')
    if com.lower() == 'del':
        str = input('Какую запись хотите удалить? ')
        edit_note(str, False)
    if com.lower() == 'edit':
        str = input('Какую запись желаете отредактировать? ')
        edit_note(str, True)
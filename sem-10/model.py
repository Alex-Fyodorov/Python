from copy import deepcopy

class Contact():

    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def full(self):
        return f'{self.name.lower()} {self.phone.lower()} {self.comment.lower()}'

class PhoneBook:

    def __init__(self, phone_book: dict = None, path: str = 'phones.txt'):
        self.path = path
        if phone_book is None:
            self.phone_book: dict[int, Contact] = {}
        else: 
            self.phone_book = phone_book
        self.original_book = {}

    def open_file(self):        
        with open(self.path, 'r', encoding = 'UTF-8') as file:
            data = file.readlines()
        for i, contact in enumerate(data, 1):
            contact = contact.strip().split(';')
            self.phone_book[i] = Contact(*contact)
        self.original_book = deepcopy(self.phone_book)        
        
    def save_file(self):        
        data = []
        for contact in self.phone_book.values():            
            data.append(f'{contact.name};{contact.phone};{contact.comment}')
        data = '\n'.join(data)
        with open(self.path, 'w', encoding = 'UTF-8') as file:
            file.write(data)

    def add_contact(self, new_contact: list[str]):        
        contact_id = max(self.phone_book) + 1
        self.phone_book[contact_id] = new_contact

    def find_contact(self, word: str):        
        result = {}
        for contact_id, contact in self.phone_book.items():            
            if word.lower() in contact.full():
                result[contact_id] = contact
                break
        return PhoneBook(result)

    def edit_contact(self, contact_id: int, new_contact: Contact):        
        current_contact = self.phone_book.get(contact_id)        
        name = new_contact.name if new_contact.name else current_contact.name
        phone = new_contact.phone if new_contact.phone else current_contact.phone
        comment = new_contact.comment if new_contact.comment else current_contact.comment
        self.phone_book[contact_id] = Contact(name, phone, comment)
        return name

    def delete_contact(self, contact_id: int) -> str:        
        return self.phone_book.pop(contact_id).name
    
    def max_len(self, option: str):
        result = []
        for contact in self.phone_book.values():
            if option == "name":
                item = contact.name
            elif option == 'phone':
                item = contact.phone
            else:
                item = contact.comment
            result.append(item)
        return len(max(result, key = len))
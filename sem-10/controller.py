from model import PhoneBook
import text
import view

def search_contact(pb: PhoneBook):
    word = view.input_request(text.input_search_word)
    result = pb.find_contact(word)
    view.show_book(result, text.not_find(word))     
    return result

def input_contact_id(contact_list: PhoneBook) -> int:
    contact_id = int(view.input_request(text.input_edit_contact_id))
    while contact_id not in contact_list.phone_book:
        view.print_message(text.id_not_in_list)
        contact_id = int(view.input_request(text.input_edit_contact_id))
    return contact_id        

def start():  
    pb = PhoneBook()  
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                pb.open_file()                
                view.print_message(text.load_successful)
            case 2:
                pb.save_file()
                view.print_message(text.save_successful)
            case 3:                
                view.show_book(pb, text.empty_book_error)
            case 4:
                new_contact = view.input_contact(text.input_contact())
                pb.add_contact(new_contact)
                view.print_message(text.contact_action(new_contact.name, text.operation[0]))
            case 5:
                search_contact(pb)               
            case 6:
                search_list = search_contact(pb)
                if search_list.phone_book:                                        
                    contact_id = input_contact_id(search_list)
                    new_contact = view.input_contact(text.input_contact(True))
                    name = pb.edit_contact(contact_id, new_contact)
                    view.print_message(text.contact_action(name, text.operation[1]))
            case 7:
                search_list = search_contact(pb)
                if search_list.phone_book:                                        
                    contact_id = input_contact_id(search_list)
                    name = pb.delete_contact(contact_id)
                    view.print_message(text.contact_action(name, text.operation[2]))
            case 8:
                if pb.original_book != pb.phone_book:
                    if view.input_request(text.confirm_changes).lower() == 'y':
                        pb.save_file()
                        view.print_message(text.save_successful)
                view.print_message(text.exit_program)
                break
            
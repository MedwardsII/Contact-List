'''
Application to create, view, and edit contact information
Will be moving CMI to to GUI
'''
class Contact:
    max_name_len = 16 #static variable

    def __init__(self):
        pass

    def set_name(self, first_name = 'NONE', middle_initial = 'NONE', last_name = 'NONE'):
        self.name = dict({'first': first_name,
                         'm_initial': middle_initial,
                         'last': last_name})

    def get_name(self):
        return self.name
    
    def set_phone(self, ph_number):
        self.phone = ph_number

    def get_phone(self):
        return self.phone

    def set_address(self, street_number, streetName, city, st, zip_code):
        self.address = dict({'street_number': street_number,
                            'street_name': streetName,
                            'city': city,
                            'state': st,
                            'zip_code': zip_code})

    def get_address(self):
        return self.address

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

def set_contact():
    '''Function to walk set new contact'''
    try:
        collect_name()
        collect_phone()
        collect_email()
        collect_address()
    except ValueError as e:
        print(e)

def collect_name():
    while(True):
        try:
            print('Please enter requested information. Leave blank if none.')
            f_name = input('FIRST NAME: ')
            m_name = input('MIDDLE INITIAL: ')
            l_name = input('LAST NAME: ')
            break
        except:
            print(e)
    contact = Contact()
    contact.set_name(f_name, m_name, l_name)

def collect_phone():
    while(True):
        try:
            phone_number = int(input('Phone Number: '))
            break
        except ValueError as e:
            print(e)

def collect_address():
    while(True):
        try:
            street_number = int(input('Street Number: '))
            street_name = input('Street Name: ')
            city = input('City: ')
            st = input('State: ')
            zip_code = int(input('ZIP CODE: '))
            break
        except ValueError as e:
            print(e)
    contact = Contact()
    contact.set_address(street_number,street_name,
                                city, st, zip_code)

def collect_email():
    while(True):
        email = input("Email: ")
        break
    contact = Contact()
    Contact.set_email(email)

def set_header_action(header_action):
    '''Function to execute Header action'''
    while(True):
        if header_prompt == '1':
            break
        if header_prompt == '2':
            set_contact()
            break
        elif header_prompt == 'q':
            quit()
    
while(True):
    try:
        header_prompt = input('1: Get contacts\n' +
                              '2: Create New Contact\n' +
                              'q: Quit Application\n')
        assert (header_prompt == '1' or
                header_prompt == '2' or
                header_prompt.lower() == 'q')
    except AssertionError:
        print('Please select from the below!')
        continue
    set_header_action(header_prompt)


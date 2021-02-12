# Application to create, view, and edit contact information

class Contact:
    max_name_len = 16 #static variable
    def __init__(self):
        pass

    def set_name(self, **name):
        self.name = dict({'first': name['f_name'],
                         'm_initial': name['m_name'],
                         'last': name['l_name']})

    def get_name(self):
        return self.name

def set_contact():
    '''
    Function to walk set new contact
    INPUT: String
    OUTPUT: NONE
    '''
    while(True):
        print('Please enter requested information. Leave blank if none.')
        f_name = input('FIRST NAME: ')
        m_name = input('MIDDLE INITIAL: ')
        l_name = input('LAST NAME: ')
        break
    name = dict({'f_name':f_name,
                 'm_name': m_name,
                 'l_name': l_name})
    return name

def set_header_action(header_action):
    '''
    Function to execute Header action
    INPUT: String
    OUTPUT: NONE
    '''
    while(True):
        if header_prompt == '1':
            break
        if header_prompt == '2':
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


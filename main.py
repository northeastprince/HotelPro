import time

time.sleep(3)
print("Welcome to the PMS!")
time.sleep(2)
auth = False
terminal = True
#User Verifacation

while auth == False:
    id = raw_input("Enter User ID: ")
    if id == '519':
        auth = True
    elif id == '769':
        auth = True
else: auth = False

current_user = id

room_status = ['R1 Busy', 'R2 Busy', 'R3 Busy', 'R4 Avalible']

#Command process

while terminal == True:
    entered_command = raw_input('Terminal: ')
    if entered_command == 'room_status':
        print(room_status)
    elif entered_command == 'current_user':
        print('The current user is: ' + id)
    elif entered_command == 'add_room':
        add = raw_input('Enter Room Value: ')
        room_status.append(add)
    elif entered_command == 'customer_edit':
        print(customer_edit)
        cus_edit = raw_input('Enter Full New Value: ')
        customer_edit = cus_edit
        print(customer_edit)
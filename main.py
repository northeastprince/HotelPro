import time

import json



time.sleep(3)

print('Welcome to the PMS!')

time.sleep(2)

auth = False

terminal = True



id = raw_input('Enter User ID: ')

if id == '519':

    auth = True

else: auth = False



while auth == False:

    print('Invalid credentials')

    id = raw_input('Enter User ID: ')

    if id == '519':

        auth = True

    else: auth = False

current_user = id



#Command Process



filename = 'room_status.json'

with open(filename) as f_obj:
  room_status = json.load(f_obj)



while auth == True:

    entered_command = raw_input()

    if entered_command == 'room_status':

        print(room_status)

    elif entered_command == 'current_user':

        print('Current User Is: ' + current_user)

    elif entered_command == 'add_room':

        add = raw_input('Enter Room Value: ')

        room_status.append(add)

    elif entered_command == 'book_room':

        cus_num = raw_input('Enter Customer Number: ')

        room_num = raw_input('Enter Room Num without prefix: ')

        room_status[int(room_num) - 1] = 'R' + room_num + ' Booked to: ' + cus_num
    elif entered_command == 'save':
        with open(filename) as f_obj:
            room_status = json.load(f_obj)
    
    else: print ('Invalid Command')

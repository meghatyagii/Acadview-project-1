from final_details import Spy, spy ,ChatMessage ,friends
#here we have imported the details of the spy
from steganography.steganography import Steganography
#here we import the class Steganography
from datetime import datetime
#here we import datetime
STATUS_MESSAGES = ['My name is megha', 'I am the best spy', 'Lets rock and roll']

print "Hello! Let's get started"
#this is the greeting message
existing = raw_input("Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? ")
#here we ask a question that the spy is a existing user and continue as the same?
#and we print the question using raw_input


def add_status():
# here we create a function which will give the user an opyion to add a status.

    updated_status_message = None

    if spy.current_status_message != None:

        print "Your current status message is %s \n" (spy.current_status_message)
    else:
        print "There is no current status message \n"
#here we define that if the current status message of the spy is not none then we print the current ststus message of the spy.
#but if there is no status message currently,we will print you dont have any status message currently.
#we use a backslash after n in don\'t in order to avoid confusion in the terminantion of the printed message.

    default = raw_input("Do you want to select from the older status (y/n)? ")
#we ask the user if he wants to select a status from his previous status list?
    if default.upper() == "N":
        new_status_message = raw_input("What should be your new status message? ")
# if the answer is N [specifically] then we give him an opion to print a new status message.


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
#to make sure he does not enter an empty status, we check the length.
#and the new status message is appended or added to the list of STATUS MESSAGE.
#now the updated status message is the one the user has entered.

    elif default.upper() == 'Y':
# if he wants to add the status from the STATUS MESSAGE list
        item_position = 1
#initially the value of item position=1
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
#thiswill print the list of messages in STATUS MESSAGE.
        message_selection = int(raw_input("\nChoose from the above messages "))
#now we ask the user to select the item position value from the list.
#we convert it into int as the raw input will consider it as a string.

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
#we check the length to make sure that the selected message exists in the list or is not blank.
    else:
        print "It is not a valid option Press either y or n."
#if the condition is not specified we print this message.
    if updated_status_message:
        print "Your updated status message is: %s" % (updated_status_message)
    else:
        print "There is no current status update"

    return updated_status_message
#if the status message is updated,we print and then return it.
#else we print that you do not have astaus update.

def add_friend():
# here we define a function to add a friend.
    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name
#concatenation of name and salutation of friend's name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)
#conversion of string into int.
    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)
#conversion of string to float.

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
# if the conditions are satisfied,we add or append the new friend to the list of friends.
        print 'Friend Added!'
    else:
        print "Its a Invalid entry. We can not add spy with the details you provided"
#we print this if the conditions are not satisfied.
    return len(friends)
#prints the number of friends

def select_a_friend():
# here we create a function to select a friend.
    item_number = 0

    for friend in friends:
        print "%d. %s %s aged %d with rating %.2f is online" % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1
#this will print the list of the friends with all their details.
    friend_choice = raw_input("Choose from your friends")
#choose the friend from the given list
    friend_choice_position = int(friend_choice) - 1
#convert string to int.
    return friend_choice_position


def send_message():
# here we define a function to send message.

    friend_choice = select_a_friend()

    src ="input.jpg"
    dest = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(src, dest, text)
#we have alreday imported the class Steganography.
#encoding of the text within a image.
    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)
#the chat with the new friend is appended to the new chat.
    print "Your secret message image is ready!"


def read_message():
# here we create a function read message
    sender = select_a_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
#to decode the secret message
    new_chat = ChatMessage(secret_text,False)
    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"


def read_chat_history():
# here we define a function to read the chat history.
    read_for = select_a_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

def start_chat(spy):
# here we define a function to start a chat
    spy.name = spy.salutation + " " + spy.name
#concatenation of spy name and salutation.
    if spy.age > 12 and spy.age < 50:
# conditions for spy age
        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you here"
#concatenation
        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)
# the complete menu list is printed.
            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
 # checking length of the selected menu choice.
                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
#we specify the menu list for each choice.
    else:
        print 'Sorry you are not of the correct age to be a spy'
#if conditions are not specified print this.
if existing.upper() == "Y":
    spy_enter = raw_input("Enter password. ")
    if spy_enter == "hypothetical":
        print "Welcome"
        start_chat(spy)
    else:
        print "Invalid Password. Please restart and try again."
#here we create a condition to access only with a particular password
else:

    spy = Spy('','',0,0.0)

    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input(" are you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
#conditions for a new spy.
    else:
        print 'Please add a valid spy name'
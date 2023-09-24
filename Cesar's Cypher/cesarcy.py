# Cesar's cypher.
import string

message = input("Please enter the message")
count = input("Please enter the count")
letters = list(string.ascii_lowercase)


def encrypt_msg(msg, count):
    print("The message sent to be encrypted is :" + msg)
    # msg_list is the array of all the characters in the message
    msg_list = list(msg)
    count = int(count)
    encrypted = []
    for x in range(0, (len(msg_list))):
        for y in range(0, (len(letters))):
            if msg_list[x] == letters[y]:
                count_final = int(y + count)
                encrypted.append(letters[count_final])
    stringify(encrypted)
    unencryptmsg(encrypted)


def stringify(x):
    message = ""
    for y in x:
        message += y
    print(message)


def unencryptmsg(y):
    print("This is the start of the encryption function")

    # In the previous function, the message was made a string from a list after moving places. We need now is to reset it
    # to a list. so we will list the message from string.

    # Variables
    unencrypted = ""

    lstmsg = list(y)
    # variables in this scope
    for x in range(0, len(lstmsg)):
        for p in range(0, len(letters)):
            if lstmsg[x] == letters[p]:
                lstmsg[x] = letters[p - int(count)]

    # calling stringify
    stringify(lstmsg)


# calling the function
encrypt_msg(message, count)

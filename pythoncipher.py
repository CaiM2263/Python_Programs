import random
alpha='abcdefghijklmnopqrstuvwxyz'
alpha2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
phrase_bank=['hello','good bye','The roof of the A building','applesauce and juicy pear', 'The only thing we have to fear is fear itself',
             'This is your conscience speaking','Love, happiness, and generosity',
             'Reading, Fighting, and Eating','Darkness cannot drive out darkness; only light can do that',
             'She sells sea shells by the sea shore','Life is like a box of chocolate','squishy',
             "It was never the way you looked, it's the way you act","Jim went to the lemonade stand and said, 'Do you have any grapes?'",
             'Pineapples, octopus, and December','sorry not sorry', 'it takes one to know one',"I'm in my room",
             "I love you, I hate you, I am neutral about you","Wow, that's inspirational.",
             "I don't have anything better to do.","Spread ove wherever you go."]
def home():
    print("Hello! Welcome to the Python Cipher! What would you like to do?")
    choice=str(input("1: Encode a message \n2: Decode a message\n3: Random decode \n4: Quit\nEnter your selection here: "))
    if choice=='1':
        message=str(input("Enter your plaintext: "))
        encode(message)
    elif choice=='2':
        message=str(input("Enter your ciphertext: "))
        decode(message)
    elif choice=='3':
        rdecode()
    elif choice=='4':
        exit()
    else:
        print("Error: Please enter 1, 2, or 3.")
        home()

def encode(message):
    shift=int(input("Enter a number shift: "))
    print(f'The new message is: {rot(message,shift)}')
    choice=str(input("What would you like to do next?\n1: Encode another message\n2: Return to the main menu\n3: Quit\nEnter your selection here: "))
    if choice=='1':
        message=str(input("Enter your plaintext: "))
        encode(message)
    elif choice=='2':
        home()
    elif choice=='3':
        exit()
    else:
        print("Error: Please enter 1, 2, or 3.")
        home()
        
def decode(message):
    print('Decoding...')
    for shift in range(0,26):
        print(f'{shift+1}: {rot(message,shift)}')
    choice=str(input("What would you like to do next?\n1: Decode another message\n2: Return to the main menu\n3: Quit\nEnter your selection here: "))
    if choice=='1':
        message=str(input("Enter your ciphertext: "))
        decode(message)
    elif choice=='2':
        home()
    elif choice=='3':
        exit()
    else:
        print("Error: Please enter 1, 2, or 3.")
        home()

def rot(message,shift):
    new_message=''
    for letter in message:
            if letter in alpha2:
                new_message+=alpha2[(alpha2.index(letter)+shift)%len(alpha2)].upper()
            elif letter in alpha:
                new_message+=alpha[(alpha.index(letter)+shift)%len(alpha)].lower()
            else:
                new_message+=letter
    return new_message

def rdecode():
    message=phrase_bank[random.randint(0,20)]
    ciphertext=''
    shift=random.randint(1,26)
    for letter in message:
        if letter in alpha2:
            ciphertext+=alpha2[(alpha2.index(letter)+shift)%len(alpha2)].upper()
        elif letter in alpha:
            ciphertext+=alpha[(alpha.index(letter)+shift)%len(alpha)].lower()
        else:
            ciphertext+=letter  
    shift=int(input(f'Here is the encoded message: {ciphertext}\nEnter a shift: '))
    cipher_check(ciphertext,shift)
def cipher_check(ciphertext,shift):
    print(rot(ciphertext,shift))
    if rot(ciphertext, shift) in phrase_bank:
        print('Congrats! You have succesfully decoded the message!')
        choice=str(input("What would you like to do next?\n1: Decode another message\n2: Return to the main menu\n3: Quit\nEnter your selection here: "))
        if choice=='1':
            rdecode()
        elif choice=='2':
            home()
        elif choice=='3':
            exit()
        else:
            print("Error: Please enter 1, 2, or 3.")
            home()
    else:
        print("Sorry, that's the wrong shift.")
        choice=str(input('1: Try a different shift\n2: Main menu\n3: Quit\nEnter your selection here: '))
        if choice=='1':
            shift=int(input('Enter a shift: '))
            cipher_check(ciphertext,shift)
        elif choice=='2':
            home()
        elif choice=='3':
            exit()
        else:
            print("Error: Please enter 1, 2, or 3.")
            home()
home()

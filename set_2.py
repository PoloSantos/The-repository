'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''
def shift_letter():
    '''letter, shift
    Shift Letter.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = ["A","B","C","D","E","F",'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    letter = str(input("What letter will you shift? "))
    
    if letter == " ":
        print(" ")
    else:
        shift = int(input("By how many positions will you shift it by? "))
        position = alphabet.index(letter)
        position2 = position+shift
        if position2 > 26:
            position2 = position2 - 26
        print(alphabet[position2])

shift_letter()


def caesar_cipher():
    '''message, shift
    Caesar Cipher.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = ["A","B","C","D","E","F",'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    message = str(input("What is the message? "))
    
    if message == " ":
        print(" ")
    else:
        shift = int(input("By how many positions will you shift it by? "))
        messagelist = list(message)
        for letter in messagelist:
            position = alphabet.index(letter)
            position2 = position+shift
            if position2 > 26:
                position2 = position2 - 26
            messagelist[messagelist.index(letter)] = alphabet[position2]

        print("".join(messagelist))

caesar_cipher()


def shift_by_letter():
    '''letter, letter_shift
    Shift By Letter.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = ["A","B","C","D","E","F",'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    letter = str(input("What letter will you shift? "))
    
    if letter == " ":
        print(" ")
    else:
        lettershift = str(input("By how many positions will you shift it by(letter input)? "))
        numshift = alphabet.index(lettershift)
        position = alphabet.index(letter)
        position2 = position+numshift
        if position2 > 26:
            position2 = position2 - 26
        print(alphabet[position2])

shift_by_letter()


def vigenere_cipher():
    '''message, key
    Vigenere Cipher.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the key is extended to match the length of the message.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = ["A","B","C","D","E","F",'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    message = str(input("What is the message? "))
    

    if message == " ":
        print(" ")

    else:
        key = input("input your key: ")
        keylist = list(key)
        messagelist = list(message)
        i = 0
        j = 0
        listamt = len(keylist)
        for var in keylist:
            john = alphabet.index(var)
            keylist[j] = john
            j += 1

        for letter in messagelist:
            position = alphabet.index(letter)

            if listamt <= i:
                i = 0
            ke = keylist[i]
            
            positionfinale = position+ke
            if positionfinale > 26:
                positionfinale = positionfinale - 26

            messagelist[messagelist.index(letter)] = alphabet[positionfinale]
            i += 1

    print("".join(messagelist))
    
vigenere_cipher()


def scytale_cipher(message, shift):
    '''message, shift
    Scytale Cipher.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    messagelist = list(message)
    masglste = list(message)
    i = 0
    j = 1
    while i == 0:
        if (len(messagelist)%shift) == 0:
            for letter in messagelist:
                numlet = messagelist.index(letter)
                masglste[numlet] = messagelist[(numlet//shift)+(len(message)//shift)*(numlet%shift)]
            i = 1

        else:
            messagelist.append("_")
            masglste.append("_")

    finalmsg = "".join(masglste)
    print(finalmsg)
    return finalmsg

scytale_cipher("QWERTYUIOPAS", 3)


def scytale_decipher(message, shift):
    '''Scytale De-cipher.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    messagelist = list(message)
    masglste = list(message)
    i = 0
    j = 1
    while i == 0:
        if (len(messagelist)%shift) == 0:
            for letter in messagelist:
                numlet = messagelist.index(letter)
                messagelist[(numlet//shift)+(len(message)//shift)*(numlet%shift)] = masglste[numlet]
            i = 1

        else:
            messagelist.append("_")
            masglste.append("_")

    finalmsg = "".join(messagelist)
    print(finalmsg)
    return finalmsg

scytale_decipher("QTOWYPEUARIS",3)
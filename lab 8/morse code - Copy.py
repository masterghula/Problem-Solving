codes = {'A': '.-',     'B': '-...',   'C': '-.-.',
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..',

            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.', ' ': 'SPACE'
            }

def encrypt():
    msg=input("Type your message: ")
    msg=msg.upper()
    for n in msg:
        if n in codes:
           print(codes[n], end='/')
    print("\n")

def decrypt():
    msg=input("Enter morse code: ")
    reverse_codes={value:key for key, value in codes.items()}
    tempword = ''
    for n in msg:
        if n!='/':
            tempword+=n
            continue
        str = tempword
        tempword = ''
        print(reverse_codes[str], end='')

encrypt()
decrypt()

'''Well, someone in our lab has setup a seven segment display, it seems to display a message but we can't understand it. Something is related to hexa representation. Don't forget to wrap the flag in FindITCTF{ }

7-segment display sequence:
abc abc abcdg abcdg acdefg adef acdefg abcdg abcdg abcdef acdefg abcdef acdefg acdfg acdfg aefg abc bcfg abcdg abcdef acdfg aefg acdefg acdefg abcdg bc acdefg adefg acdefg bcfg acdfg aefg acdefg abcdfg abc bcfg acdfg aefg acdefg abcdg abc bcfg acdefg acdefg acdfg aefg abcdg bc abcdg abdeg abcdg abcdg abcdg bcfg abcdg acdfg abcdg acdefg abcdg abc abcdg abcdefg'''

# ide pertama:
# Kayaknya itu merepresentasikan digit tiap binary. (Something is related to hexa representation)
# a b c d e f g 
# 6 5 4 3 2 1 0 


char_arr = "abc abc abcdg abcdg acdefg adef acdefg abcdg abcdg abcdef acdefg abcdef acdefg acdfg acdfg aefg abc bcfg abcdg abcdef acdfg aefg acdefg acdefg abcdg bc acdefg adefg acdefg bcfg acdfg aefg acdefg abcdfg abc bcfg acdfg aefg acdefg abcdg abc bcfg acdefg acdefg acdfg aefg abcdg bc abcdg abdeg abcdg abcdg abcdg bcfg abcdg acdfg abcdg acdefg abcdg abc abcdg abcdefg".split(' ')

for i in char_arr:
    x = 0
    for char in i:
        if char == 'a':
            x += 2**6
        elif char == 'b':
            x += 2**5
        elif char == 'c':
            x += 2**4
        elif char == 'd':
            x += 2**3
        elif char == 'e':
            x += 2**2
        elif char == 'f':
            x += 2**1
        elif char == 'g':
            x += 2**0
    print(chr(x), end="")

# ternyata salah, setelah search google nemu seven segment display itu yg kyk gini 
# https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/7_Segment_Display_with_Labeled_Segments.svg/150px-7_Segment_Display_with_Labeled_Segments.svg.png

# oke lebih jelas

print()
seg7dict = {
    'abcdef': 0,
    'bc': 1,
    'abdeg': 2,
    'abcdg': 3,
    'bcfg': 4,
    'acdfg': 5,
    'acdefg': 6,
    'abc': 7,
    'abcdefg': 8,
    'abcdfg': 9,
    'adef': 'C',
    'aefg': 'F',
    'adefg': 'E',
    'abcdfg': 'A',
}

x = ''
for i in char_arr:
    x += str(seg7dict[i])

# sampe sini dapet string, tapi gataw diapain
# karna katanya ini hexadecimal jadi curiga kalo dikelompokin 
# dua dua dan diubah ke ascii

print('FindITCTF{', end="")

for i in range(0, len(x), 2):
    a = x[i] + x[i+1]
    print(chr(int(a,16)), end="")

print('}')



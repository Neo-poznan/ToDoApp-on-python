import random
import string

def hex_to_rgba_02(value):
    value = value.lstrip('#')
    lv = len(value)
    rgb = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    rgba = f'rgba{rgb}'[0:-1]
    rgba += ', 0.2)'
    return rgba

def random_hex():
    color = '#'
    string.ascii_letters = 'ABCDEF'
    for i in range(6):
        next = random.choice(['num', 'let'])
        if next == 'let':
            color += random.choice(string.ascii_letters)
        else:
            color += str(random.randint(0, 9))

    return color



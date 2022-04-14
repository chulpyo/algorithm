"""programmers python code template
"""


args = (
    (('one4seveneight', ), 1478)
    , (('23four5six7', ), 234567)
    , (('2three45sixseven', ), 234567)
    , (('123', ), 123)
)

DIGITS = {
    'ze': (4, '0')
    , 'on': (3, '1')
    , 'tw': (3, '2')
    , 'th': (5, '3')
    , 'fo': (4, '4')
    , 'fi': (4, '5')
    , 'si': (3, '6')
    , 'se': (5, '7')
    , 'ei': (5, '8')
    , 'ni': (4, '9')
}

def solution(s):

    idx = 0
    length = len(s)

    answer = []

    while idx < length:
        code = s[idx:idx+2] if idx + 2 <= length else s[idx:idx+1]
        if code in DIGITS:
            answer.append(DIGITS[code][1])
            idx += DIGITS[code][0]
        else:
            answer.append(s[idx])
            idx += 1
    
    return int(''.join(answer))
    

if __name__ == '__main__':
    for arg in args:
        result = solution(*arg[0])
        print(f'answer is {arg[1]}. your answer is {result}. {"O" if arg[1] == result else "X"}')
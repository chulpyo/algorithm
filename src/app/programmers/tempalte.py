"""programmers python code template
"""


args = (
    ((), )
    , ((), )
)

def solution():
    pass

if __name__ == '__main__':
    for arg in args:
        result = solution(*arg[0])
        print(f'answer is {arg[1]}. your answer is {result}. {"O" if arg[1] == result else "X"}')
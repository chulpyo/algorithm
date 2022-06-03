"""없는 숫자 더하기
"""

args = (
    (([1,2,3,4,6,7,8,0], ), 14),
    (([1,2,3,4,6,7,8,0], ), 14),
    (([5,8,4,0,6,7,9], ), 6),
)

def solution(numbers):
    return 45 - sum(numbers)    

if __name__ == '__main__':
    for arg in args:
        result = solution(*arg[0])
        print(f'answer is {arg[1]}. your answer is {result}. {"O" if arg[1] == result else "X"}')
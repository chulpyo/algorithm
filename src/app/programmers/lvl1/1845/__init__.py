""" 폰켓몬
"""

args = (
    (([3,1,2,3], ), 2),
    (([3,3,3,2,2,4], ), 3),
    (([3,3,3,2,2,2], ), 2),
)

def solution(nums):
    return min(len(set(nums)), len(nums)//2)

if __name__ == '__main__':
    for arg in args:
        result = solution(*arg[0])
        print(f'answer is {arg[1]}. your answer is {result}. {"O" if arg[1] == result else "X"}')
"""
"""

args = (
    (([4,7,12],	[True,False,True]), 9),
    (([1,2,3],	[False,False,True]), 0),
)

def solution(absolutes, signs):
    return sum(map(lambda x: x[0] if x[1] else -1 * x[0]
                , zip(absolutes, signs)))

if __name__ == '__main__':
    for arg in args:
        result = solution(*arg[0])
        print(f'answer is {arg[1]}. your answer is {result}. {"O" if arg[1] == result else "X"}')
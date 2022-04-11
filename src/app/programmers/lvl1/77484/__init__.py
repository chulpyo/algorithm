"""로또의 최고 순위와 최저 순위
"""

args = (
    (([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]), [3, 5] )
    , (([0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25]), [1, 6])
    , (([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]), [1, 1])
)

RANK = [6, 6, 5, 4, 3, 2, 1]

def solution(lottos, win_nums):
    known = sum( lotto > 0 and lotto in win_nums for lotto in lottos )
    unknown = sum( lotto == 0 for lotto in lottos)

    return [RANK[known+unknown], RANK[known]]


if __name__ == '__main__':
    for arg in args:
        result = solution(*arg[0])
        print(f'answer is {arg[1]}. your answer is {result}. {"O" if arg[1] == result else "X"}')
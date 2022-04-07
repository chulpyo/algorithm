"""신고 결과 받기  
"""

args = (
    ((["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2), [2,1,1,0])
    , ((["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3), [0, 0])
)

def solution(id_list, report, k):
    report_set = { user: set() for user in id_list }
    report_result = { user: 0 for user in id_list }
    
    for row in report:
        src, dest = row.split()
        report_set[dest].add(src)
    
    for val in report_set.values():
        if len(val) >= k:
            for user in  val:
                report_result[user] += 1

    return [ report_result[key] for key in id_list ]


if __name__ == '__main__':
    for arg in args:
        result = solution(*arg[0])
        print(f'answer is {arg[1]}. your answer is {result}. {"O" if arg[1] == result else "X"}')
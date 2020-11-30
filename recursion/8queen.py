# 8퀸 문제 알고리즘 구현하기

pos = [0] * 8 # 각 열에서 퀸의 위치
flag_a = [False] * 8 # 각 행에 퀀을 배치했는지 체크
flag_b = [False] * 15 # 대각선 (왼쪽 아래에서 오른쪽 위 방향)으로 퀀을 배치했는지 확인
flag_c = [False] * 15 # 대각선 (오른쪽 아래에서 왼쪽 위 방향)으로 퀸을 배치했는지 확인


def put() -> None:
    """각 열에 배치한 퀸의 위치를 출력"""

    # for i in range(8):
    #     print(f'{pos[i]:2}', end=' ')
    # print()

    for i in range(8):
        for j in range(8):
            print('■' if pos[i] == j else '□', end=' ')
        print()
    print()

def set(i: int) -> None:
    """i열에 퀸을 배치"""
    for j in range(8):
        if (     not flag_a[j] # j행에 퀸을 배치하지 않았으면
            and not flag_b[i+j] # 대각선 방향으로 퀀이 배치되지 않았다면
            and not flag_c[i-j+7]): # 대각선 방향으로 퀸이 배치되지 않았다면
            pos[i] = j # 퀸을 j행에 배치
            if i == 7: # 모든 열에 퀸 배치를 종료
                put()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True
                set(i+1) # 다음 열에 퀸을 배치
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = False

set(0) # 0열에 퀸을 배치
# a = [1,2,3,4,5]
# for i in range(5):
#     print(f'{a[i]:3}',end = '')
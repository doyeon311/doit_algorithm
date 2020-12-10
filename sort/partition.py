# 배열을 두 그룹으로 나누기

from typing import MutableSequence


def partition(a: MutableSequence) -> None:
    """배열을 나누어 출력"""
    n = len(a)
    pl = 0          # 왼쪽 커서
    pr = n - 1      # 오른쪽 커서
    x = a[n // 2]   # 피벗(가운데 원소)

    while pl <= pr:
        while a[pl] < x:    # a[pl]의 값이 피벗보다 클 때까지 인덱스를 옮김(오른쪽으로)
            pl += 1
        while a[pr] > x:    # a[pr]의 값이 피벗보다 작을 때까지 인덱스를 옮김(왼쪽으로)
            pr -= 1

        if pl <= pr:        # pl, pr이 서로 일치하거나 교차하지 않았을 경우 True
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'피벗은 {x}입니다.')

    print('피벗 이하인 그룹입니다.')
    print(*a[0: pl])                    # a[0] ~ a[pl-1]

    if pl > pr + 1:
        print('피벗과 일치하는 그룹입니다.')
        print(*a[pr+1:pl])              # a[pr+1] ~ a[pl-1]

    print('피벗 이상인 그루입니다.')
    print(*a[pr+1:n])                   # a[pr+1] ~ a[n-1]


if __name__ == "__main__":
    print('배열을 나눕니다.')
    num = int(input('원소 수를 입력하세요: '))

    x = [None]*num              # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    partition(x)                # 배열 x를 나누어 출력

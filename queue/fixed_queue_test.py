# 고정 길이 큐 클래스(FixedQueue)를 사용하기

from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['enqueue', 'dequeue', 'peek', 'search', 'dump', 'exit'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ',end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
q = FixedQueue(64) # 최대 64개를 enqueue할 수 있는 큐

while True:
    print(f'현재 데이터 개수: {len(q)} / {q.capacity}')
    menu = select_menu() # 메뉴 선택
    # print(f'test {Menu.enqueue} menu {menu} {type(menu)}')
    if menu == Menu.enqueue: # enqueue
        x = int(input('인큐할 데이터를 입력하세요: '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('큐가 가득 찼습니다.')

    elif menu == Menu.dequeue: # dequeue
        try:
            x = q.deque()
            print(f'디튜한 데이터는 {x}입니다.')
        except FixedQueue.Empty:
            print('큐가 비어 있습니다.')

    elif menu == Menu.peek: # peek
        try:
            x = q.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedQueue.Empty:
            print(f'큐가 비었습니다.')
    
    elif menu == Menu.search: # search
        x = int(input('검색할 값을 입력하세요: '))
        if x in q:
            print(f'{q.count(x)}개 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.')
        else:
            print('검색값을 찾을 수 없습니다.')
    
    elif menu == Menu.dump: # dump
        q.dump()
    
    else:
        break


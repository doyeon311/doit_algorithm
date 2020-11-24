# 고정 길이 스택 클래스(FixedStack)를 사용하기

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['push','pop','peek','search','dump','exit'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64) # 최대 64개를 푸시할 수 있는 스택

while True:
    print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
    menu = select_menu() # 매뉴 선택

    if menu == Menu.push: # push
        x = int(input('데이터를 입력하세요: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('스택이 가득 차 있습니다.')
        
    elif menu == Menu.pop: # pop
        try:
            x = s.pop()
            print(f'pop한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')
    
    elif menu == Menu.peek: # peek
        try:
            x = s.peek()
            print(f'peek한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')

    elif menu == Menu.search: # search
        x = int(input('검색할 값을 입력하세요: '))
        if x in s:
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
        else:
            print('검색값을 찾을 수 없습니다.')
    
    elif menu == Menu.dump: # dump
        s.dump()

    else:
        break



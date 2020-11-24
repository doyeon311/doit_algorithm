# card_conv

def card_conv(x: int, r: int) -> str:

    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 다른 기수로 바꾸기 위한 템플릿

    while x > 0:
        d += dchar[x % r] # 해당하는 문자를 꺼내 결합
        x //= r
    
    return d[::-1] # 역순으로 반환


if __name__ == '__main__':
    print('10진수를 n진수로 반환합니다.')

    while True:
        while True:
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요: '))
            if no > 0:
                break
        
        while True:
            cd = int(input('어떤 진수로 변환할까요?: '))
            if 2 <= cd <= 36:
                break

        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input('한 번 더 변환할까요?(Y ... 예 / N ... 아니요): ')
        if retry in ('N', 'n'):
            break
            
    # print(card_conv(10,3))
counter  = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2): # 홀수민을 대상으로 설정
    for i in range(1, ptr): # 이미 찾은 소수로 나눔
        counter += 1
        if n % prime[i] == 0: # 나누어 떨어지면 소수가 아님
            break
    else: # 끝까지 나누어 떨어지지 않았다면
        prime[ptr] = n # 소수 배열에 등록
        ptr += 1

for i in range(ptr): # ptr의 소수를 출력
    print(prime[i])
print(f'나눗셈을 실행한 횟수: {counter}')
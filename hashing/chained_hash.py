# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key # 키
        self.value = value # 값
        self.next = next # 뒤쪽 노드를 참조
        """
        key: 키(임의의 자료형)
        value: 값(임의의 자료형)
        next: 뒤쪽 노드를 참조(Node형)

        Node 클래스는 키와 값이 짝을 이루는 구조
        키에 해시 함수를 적용하여 해시값을 구한다.

        """

class ChainedHash:
    """체인법으로 해시 클래스 구현"""
    """
    capacity: 해시 테이블의 크기(배열 table의 원소 수)를 나타낸다.
    table: 해시 테이블을 저장하는 list형 배열을 나타낸다.
    """
    def __init__(self, capacity: int) -> None:
        """초기화"""
        '''
        빈 해시 테이블을 생성한다. 
        원소 수가 capacity인 list형의 배열 table을 생성하고 모든 원소를 None으로 한다.
        모든 버킷이 빈 상태
        '''
        self.capacity = capacity # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity # 해시 테이블(라스트)을 선언

    def hash_value(self, key: Any) -> int:
        '''해시값을 구함'''
        '''
        인수 key에 대응하는 해시값을 구한다.
        '''
        if isinstance(key, int):
            '''key가 int형인 경우'''
            return key % self.capacity
        '''key가 정수가 아닌 경우(문자열, 리스트, 클래스형 등) 그 값으론느 바로 나눌 수 없으므로 표준 라이브러리로 형변환을 하여 해시값을 얻는다.'''
        # sha256 알고리즘: hashlib 모듈에서 제공하는 sha256은 RSA의 FIPS 알고리즘을 바탕으로 하며, 주어진 바이트(byte) 문자열의 해시값을 해시값을 구하는
        # 해시 알고리즘의 생성자(constructor)입니다.
        # encode() 함수: hashlib.sha256에는 바이트 문자열의 인수를 전달해야 합니다. 그래서 key를 str형 문자열로 변환한 뒤 그 문자열을 encode() 함수에 전달하여 바이트 문자열을 생성한다.
        # hexdigest() 함수: sha256 알고리즘에서 해시값을 16진수 문자열로 꺼냅니다.
        # int() 함수: hexdigest() 함수로 꺼낸 문자열을 16진수 문자열로 하는 int형으로 변환합니다.
        return (int(hashlib.sha256(str(key.encode()).hexdigest(), 16)) % self.capacity)

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key) # 검색하는 키의 해시 값
        p = self.table[hash] # 노드를 주목

        while p is not None:
            if p.key == key:
                return p.value # 검색 성공
            p = p.next # 뒤쪽 노드를 주목
        
        return None

    def add(self, key: Any, value: Any) -> bool:
        '''키가 key이고 값이 value인 원소를 추가'''
        hash = self.hash_value(key) # 추가하는 key의 해시값
        p = self.table[hash] # 노드를 주목

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp # 노드를 추가
        return True # 추가 
    
    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key) # 삭제할 key의 해시값
        p = self.table[hash] # 노드를 주목
        pp = None # 바로 앞의 노드를 주목
        
        while p is not None:
            if p.key == key: # key를 발견하면 아래를 실행
                if pp is None: 
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True # key 삭제 성공
            pp = p
            p = p.next # 뒤쪽 노드를 주목
        return False # 삭제 실패(key가 존재하지 않음)
                                                                   
    def dump(self) -> None:
        """해시 테이블을 덤프"""
        '''모든 원소를 덤프하는 것, 즉 해시 테이블의 내용을 한꺼번에 통째로 출력한다.'''
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  -> {p.key} ({p.value})', end='')
                p = p.next
            print()
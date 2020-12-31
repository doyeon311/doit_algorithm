# 이진 검색 트리 구현하기

from __future__ import annotations
from typing import Any, Type


class Node:
    """이진 검색 트리의 노드"""

    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        """생성자(constructor)"""
        self.key = key      # 키
        self.value = value  # 값
        self.left = left    # 왼쪽 포인터
        self.right = right  # 오른쪽 포인터


class BinarySearchTree:
    """이진 검색 트리"""

    def __init__(self):
        """초기화"""
        self.root = None    # 루트

    def search(self, key: Any) -> Any:
        """키가 key인 노드를 검색"""
        p = self.root       # 루트에 주목
        while True:
            if p is None:   # 더 이상 진할할 수 없으면
                return None  # 검색 실패
            if key == p.key:  # key와 노드 p의 키가 같으면
                return p.value  # 검색 성공
            elif key < p.key:   # key 쪽이 작으면
                p = p.left      # 왼쪽 서브트리에서 검색
            else:           # key 쪽이 크면
                p = p.right     # 오른쪽 서브 트리에서 검색

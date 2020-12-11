# 정렬을 마친 두 뱅려의 병합(heapq.merge 사용)

import heapq

a = [2, 4, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = list(heapq.merge(a, b))        # 배열 a와 b를 병합하여 c에 저장

#programmers _ https://school.programmers.co.kr/learn/courses/30/lessons/81302?language=python3

# 행렬 문제에 대한 지식이 더 필요해 보인다.
import sys
print(sys)
print(sys.version)
import numpy as np

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

def solution(places):
    matrix1 = np.mat(places) #matrix 함수는 mat으로 축약해서 사용 가능하다.
    
    return matrix1

result = solution(places)
print(result)

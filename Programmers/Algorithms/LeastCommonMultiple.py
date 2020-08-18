from math import gcd
#최소 공배수는 두수의 곱 / 두수의 최대 공약수(gcd) 이다.
def lcm(a,b):
  return a*b//gcd(a,b)

#n개의 최소 공배수는 두 수의 최소 공배수 와 그 다음의 수와의 최소 공배수를 구하는 형식
def solution(arr):
  for i in range(len(arr)):
    arr.append(lcm(arr.pop(),arr.pop()))
    if(len(arr)==1):
      return arr[0]

#재귀함수 사용한 방법
def solution1(arr):
  if(len(arr)==1):
    return arr[0]
  return lcm(arr[0],solution(arr[1:]))

print(solution1([1,2,3,4]))

#참조했습니다.
#https://brownbears.tistory.com/454
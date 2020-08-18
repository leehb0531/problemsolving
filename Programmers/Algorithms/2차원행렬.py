#두 2차원 행렬의 곱을 구하시오
#예시) 
#Input:[[1,4][2,3],[3,2]],[[1,2],[2,3]]
#Output:[[9,14],[8,13],[7,12]]

def func(A,B):
  answer = []
  newB = trans(B)
  for a in A:
    element = []
    for i in range(len(newB)):
      each = 0
      for j in range(len(B[0])):
        each += a[j]*newB[i][j]
      element.append(each)
    answer.append(element)
  return answer

def trans(B):
  answer = []
  for i in range(len(B[0])):
    elements = []
    for j in range(len(B)):
      elements.append(B[j][i])
    answer.append(elements)
  return answer
list1 = [[1,4],[2,3],[3,2]]
list2 = [[1,2],[2,3]]
print(func(list1,list2))
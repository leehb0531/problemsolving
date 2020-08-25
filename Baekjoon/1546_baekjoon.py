#평균

n = int(input())
scoresForNow = sorted(list(map(int,input().split())))
newScores =[]
#newScore = 0
a = 0
for i in range(n):
    newScores.append(scoresForNow[i]/scoresForNow[n-1]*100)
    #newScore += scoresForNow[i]/scoresForNow[n-1]*100
newAvg = sum(newScores)/n
print(newAvg)
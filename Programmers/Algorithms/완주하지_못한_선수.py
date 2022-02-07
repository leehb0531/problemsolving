# 마라톤 참여자 중 한명을 제외한 모두가 완주했다.
# participant는 형식의 참여자들 이름(str) list
# completion은 형식의 완주자들 이름(str) list

def solution(participant, completion):
    # 각 완주자가
    for c in completion:
        # 참여자 명단에 있다면
        if c in participant:
            # 참여자 명단에서 이름을 지운다.
            participant.remove(c)
    # 한명의 참여자만 participant에 남는다.
    return ''.join(participant)  # string 으로 바꾼다

# for in 과 if in 으로 인해 O(n^2)으로 효율성이 떨어진다.

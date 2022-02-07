# 마라톤 참여자 중 한명을 제외한 모두가 완주했다.
# participant는 형식의 참여자들 이름(str) list
# completion은 형식의 완주자들 이름(str) list

# def solution(participant, completion):
#     # 각 완주자가
#     for c in completion:
#         # 참여자 명단에 있다면
#         if c in participant:
#             # 참여자 명단에서 이름을 지운다.
#             participant.remove(c)
#     # 한명의 참여자만 participant에 남는다.
#     return ''.join(participant)  # string 으로 바꾼다

# for in 과 if in 으로 인해 O(n^2)으로 효율성이 떨어진다.

# second try

def solution(participant, completion):
    answer = ''
    # 각 list 를 sort 한다
    participant.sort()
    completion.sort()

    # completion 수만큼 loop를 돌리고
    for i in range(completion):
        # 각 sorted list의 값을 비교하여 다르면
        if participant[i] != completion[i]:
            # sorted participant list 의 값이 완주하지 못한 사람이다.
            answer += ''.join(participant[i])
            # 다른 값을 찾았다면 for loop에서 나가야 한다.
            break
    # completion 사람 수만큼 비교 했는데 전부 두 명단에 있는 것을 확인 했다면
    if not answer:
        # sorted applicant의 마지막 사람이 완주하지 못한 것이다.
        answer += ''.join(participant[-1])
    return answer

# 이 방법은 O(n) 이라 이전 보다는 효율적이다.
# 하지만 이 경우 에외 처리가 필요해보인다.

# 예외는 break 였다. 정답을 찾은 뒤의 값들은 무시해야한다.

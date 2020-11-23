def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for y in range(len(numbers)):
            if i != y:
                sum = numbers[i] + numbers[y]
                print("first if : ", sum)
                answer.append(sum)

    sort_set = set(answer)  # 집합set으로 변환
    sort_list = list(sort_set)  # list로 변환
    sort_list.sort()
    return sort_list

solution([2,1,3,4,1])
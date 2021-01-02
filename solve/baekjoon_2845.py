data = input().split()
article = input().split()

total_people = int(data[0]) * int(data[1])
result_list = ""

for i in range(len(article)):
    if i != len(article) - 1:
        result_list += str(int(article[i]) - total_people) + " "
    else:
        result_list += str(int(article[i]) - total_people)

print(result_list)

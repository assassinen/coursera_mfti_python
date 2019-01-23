main_dict = {}

# for i in range(int(input())):
puts = [
    ['Ваня', '28', 'май'],
    ['Ян', '23', 'май'],
    ['Алиса', '23', 'май'],
    ['Вася', '5', 'май']

]

# for i in range(int(input())):
#     put = input().split()
#     if put[-1] not in main_dict:
#         main_dict[put[-1]] = {put[1]:[put[0]]}
#     else:
#         if put[1] in main_dict[put[-1]]:
#             main_dict[put[-1]][put[1].append(put[0])]
#         else:
#             main_dict[put[-1]][put[1]] = put[0]

for i in range(len(puts)):
    # put = input().split()
    put = puts[i]
    if put[-1] not in main_dict:
        # main_dict[put[-1]] = ' '.join([put[0], put[1]])
        main_dict[put[-1]] = {put[1]: [put[0]]}
    else:
        if put[1] not in main_dict[put[-1]]:
            main_dict[put[-1]][put[1]] = [put[0]]
            # main_dict[put[-1]] = {put[1]: [put[0]]}
        else:
            main_dict[put[-1]][put[1]].append(put[0])
        # pass
        # main_dict[put[-1]].append([put[0], put[1]])

        # main_dict[put[-1]].append(' '.join([put[0], put[1]]))

questions = ['май']
for i in range(len(questions)):
# for i in range(int(input())):
#     question = input()
    question = questions[i]
    # question = input()
    if question in main_dict:

        keys = []
        for k in main_dict[question].keys():
            keys.append(int(k))
        keys.sort()

        answer = []
        for month in keys:
            v = main_dict[question][str(month)]
            for name in v:
                answer.append(name)
                answer.append(str(month))

        print(' '.join(answer))
    else:
        print()

# main_dict = {'январь': {'10': ['Петя']}}
#
# print(main_dict)
# # main_dict['январь']['15'] = 'Коля'
# main_dict['январь']= {'10': 'Валя'}
#
#
# print(main_dict)

s = {2: 8}
print(s[2])
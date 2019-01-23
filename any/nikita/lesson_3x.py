
main_dict = {}
answer = []
for i in range(int(input())):
    put = input().split()
    if put[-1] not in main_dict:
        main_dict[put[-1]] = {put[1]:[put[0]]}
    else:
        if put[1] in main_dict[put[-1]]:
            main_dict[put[-1]][put[1].append(put[0])]
        else:
            main_dict[put[-1]][put[1]] = [put[0]]
for i in range(int(input())):
    question = input()
    if question in main_dict:
        for k, v in sorted(main_dict[question].items()):
            v.sort()
    for name in v:
        answer.append(name)
        answer.append(k)
    print(' '.join(answer))
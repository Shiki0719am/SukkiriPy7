from random import randint as ri
print("3個の数字を当ててください!!")
answer = [ri(1,9)for i in range()]
prediction = []
nam = 3
game = True
hit = 0
out = 0
# :
#     while len(answer) < 3:
#         num = 
#         if num != answer:
#             answer.append()
#             print(answer)
while game:
    prediction = []
    count = 1
    hit = 0
    out = 0
    for i in range(nam):
        prediction.append(int(input(f"{count}桁目の予測を入力してください")))
        print(prediction)
        count += 1
    for i in range(nam):
        for j in range(nam):
            if i == j:
                if answer[i] == prediction[j]:
                    hit += 1
                    continue
            else:
                if answer[i] == prediction[j]:
                    out += 1
                    continue
    if hit == 3:
        print("正解です")
        game = False
    else:
        print(f"{hit}ヒット、{out}ボール")
        ans = int(input("続けますか？１続ける、２やめる"))
        if ans == 2:
            game = False
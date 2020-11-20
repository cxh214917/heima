import random
count_play = 0
count_win = 0
game = {1:'石头',2:'剪刀',3:'布'}
while True:
    pc = random.randint(1,3)
    user = input("请出拳:      石头（1）／剪刀（2）／布（3) 退出（0）")
    if user.isdigit():
        if int(user) in range(1,4):
            count_play += 1
            if int(user) - pc == -1 or int(user) - pc == 2:
                count_win += 1
                print("用户出拳:{}，电脑出拳:{}，用户胜".format(game[int(user)],game[pc]))
            elif int(user) - pc == -2 or int(user) - pc == 1:
                print("用户出拳:{}，电脑出拳:{}，用户败".format(game[int(user)], game[pc]))
            else:
                print("用户出拳:{}，电脑出拳:{}，平局".format(game[int(user)], game[pc]))
        elif int(user) == 0:
            if count_play != 0:
                print("游戏结束!本轮游戏胜率为: {:.2%}".format(count_win / count_play))
            else:
                print("本轮游戏无效!")
            break
        else:
            print("请从数字0-3中选择输入")
    else:
        print("您的输入不正确!请从0-3中选择输入!")
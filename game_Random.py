# 猜拳游戏

import random

print("""
\t\t\t欢迎进入☆☆☆☆☆【剪刀-石头-布】猜拳游戏☆☆☆☆☆
""")

flag = True
while flag:
    play_time = input('尊贵的玩家，你想玩几局呢: ')

    if play_time.isdigit():
        role = {1:'剪刀',2:'石头',3:'布'}

        played_time = 0
        win_time = lose_time = draw_time =0

        while played_time < int(play_time):
            player = input('玩家请出拳: 【1:石头;2:剪刀;3:布;4:不玩了】')
            computer = random.randint(1, 3)
            if player.isdigit():
                if 1 <= int(player) <= 3:
                    played_time += 1
                    if int(player) - computer == -2 or int(player) - computer == 1 :
                        win_time += 1
                        print('电脑出拳:{}，玩家出拳:{}，略胜一筹，承让'.format(role[computer],role[int(player)]))
                    elif int(player) - computer == 0:
                        draw_time += 1
                        print('电脑出拳:{}，玩家出拳:{}，平分秋色，继续'.format(role[computer],role[int(player)]))
                    else:
                        lose_time += 1
                        print('电脑出拳:{}，玩家出拳:{}，甘拜下风，再来'.format(role[computer],role[int(player)]))
                elif int(player) == 4:
                    if played_time == 0:
                        print('哥哥，下次一定要来玩哦ღ( ´･ᴗ･` )比心')
                    elif played_time == 1:
                        if win_time == 1:
                            print('哥哥，厉害୧(๑•̀◡•́๑)૭，玩一把就赢了!!!')
                        elif lose_time == 1:
                            print('哥哥，加油ヾ(◍°∇°◍)ﾉﾞ，你是最棒哒!!!')
                        else:
                            print('哥哥，坚持，坚持就是胜利!!!')
                    else:
                        if win_time == lose_time == 0:
                            print('哥哥，坚持【平局100%】坚持就是胜利!!!')
                        elif win_time == draw_time == 0:
                            print('【不以一时成败论英雄】哥哥，加油ヾ(◍°∇°◍)ﾉﾞ，你是最棒哒!!!')
                        elif lose_time == draw_time == 0:
                            print('哥哥，厉害【胜率100%】!!!')
                        elif win_time == 0:
                            print('哥哥，战况请查收【战败:{}，败率:{:.2%}，平局:{},平局率:{:.2%}】'.format(lose_time,lose_time / played_time,draw_time,draw_time / played_time))
                        elif lose_time == 0:
                            print('哥哥，战况请查收【战胜:{}，胜率:{:.2%}，平局:{},平局率:{:.2%}】'.format(win_time, win_time / played_time,draw_time,draw_time / played_time))
                        elif draw_time == 0:
                            print('哥哥，战况请查收【战胜:{}，胜率:{:.2%}，战败:{}，败率:{:.2%}】'.format(win_time, win_time / played_time,lose_time,lose_time / played_time))
                        else:
                            print('哥哥，战况请查收【战胜:{}，胜率:{:.2%}，战败:{}，败率:{:.2%}，平局:{},平局率:{:.2%}】'.format(win_time, win_time / played_time,lose_time,lose_time / played_time,draw_time,draw_time / played_time))
                    flag = False
                    break
                else:
                    print('别闹！请从【1 - 3】中选择出拳!!!')
            else:
                print('调皮！请从数字 【1 - 3】 中选择出拳!!!')
        else:
            print('哥哥，战况请查收【战胜:{}，胜率:{:.2%}，战败:{}，败率:{:.2%}，平局:{},平局率:{:.2%}】'.format(win_time, win_time / played_time,lose_time,lose_time / played_time,draw_time,draw_time / played_time))
            break
    elif play_time in ('Q','Z','q','z'):
        print('哥哥，早点来哟，等你ღ( ´･ᴗ･` )比心')
        break
    else:
        print('哥哥，别闹！请输入数字❥(^_-)')




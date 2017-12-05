#-*- coding:utf-8 -*-
'''
Heroes World Bate1.0
This is heroes details.

Devin
2017.12.04
Game Introduction:
The game starts with a name, and then in the jungle you may encounter bears,
knives and bosses. Only when you finally kill the boss can you win.
The current game operation has:
m：for view map.
w: for moving.
s: for attack.
'''
import time
board = []
hp = 100
atk = 50

print "Heroes World Bate1.0 Loading....."
time.sleep(3)
print "Wecolme to Heroes World!"
print "Heroes World Map is :"

# 输出游戏地图
for x in range(5):
    board.append(["▧"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

# 获取用户输入的游戏名
hero_name = raw_input('Please input your Hero_Name :')

if not hero_name:
    hero_name = 'player01'


user_msg = [hero_name,hp,atk]

# 输出用户英雄基本信息
print "Your hero name is : %r" %user_msg[0],"hp is : %r" %user_msg[1],"atk is : %r." %user_msg[2]
print "Now you are here : * ▧ ▧ ▧ ▧ | 'm' for view map,'w' for moving,'s'for attack."

# 获取用户输入的操作信息
user_input = raw_input()
if user_input == 'm':
    print "You are here * ▧ ▧ ▧ ▧，Please start your heroic adventure trip."
if user_input == 'w':
    print "You are here ▧ * ▧ ▧ ▧,There's a bear ahead.the black bear attacked you.You hp cut 10."

print "There's a knife in the front.You can pick up the knife and increase the attack by 100."

user_input = raw_input()
if user_input == 'w':
    print "You are here ▧ ▧ * ▧ ▧,you atk is 150.Please keep moving.You have to kill the boss to win the game."

user_input = raw_input()
if user_input == 'w':
    print "Now you've met boss.Boss attacked you, you hp reduced by 50."

user_input = raw_input()
if user_input == 's':
    print "You killed the boss and won the game."

print "Game Loading....."
time.sleep(3)
print "Congratulations! You killed the boss and won the game."

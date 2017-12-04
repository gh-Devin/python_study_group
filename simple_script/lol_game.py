#-*- coding:utf-8 -*-
 
# 获取用户输入的用户名
user_name = raw_input('please input your User_Name : ')
 
# 打印用户名
print "your User_Name is %r." % user_name
 
# 获取用户输入的密码
user_password  = raw_input('please input your User_Password : ')
 
# 获取用户输入的密码
secon_user_password  = raw_input('please input your User_Password : ')

# 验证两次密码准确度
if user_password == secon_user_password:
	print "恭喜注册成功！"

elif user_password != secon_user_password:
	print "您输入的密码不一致，请重新输入"
	user_password  = raw_input('please input your User_Password : ')
	secon_user_password  = raw_input('please input your User_Password : ')
	print "恭喜注册成功！"

print "欢迎进入英雄联盟用户界面"
# 获取用户输入的游戏名
game_name = raw_input('please input your Game_Name :')

# 打印游戏名
print "your Game_Name is %r." % game_name

# 获取用户输入的角色
game_role = raw_input('please input your Role :')

# 打印游戏角色
print "your Game_Role is %r." % game_role

print "选择成功，请开始你的英雄冒险之旅！"

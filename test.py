#coding=gbk
from wxpy import *
import datetime
import time

Ge_name = '葛文欢'
Msg_Num_Lim = 2

# bot = Bot(console_qr = True, cache_path=True, qr_path = "/var/www/wxqr/qr.png")
bot = Bot(qr_path = "/var/www/html/wxqr/qr.png")

# bot.file_helper.send('hello world!')

friends = bot.friends()
groups = bot.groups()
LOL = groups.search("Lol")[0]

friend = friends.search(Ge_name, sex=FEMALE)[0]
Morning = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '7:40', '%Y-%m-%d%H:%M')
Night = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '22:30', '%Y-%m-%d%H:%M')
Msg_Cnt = 0
old_m = now_m = 0
AutoReplyFlagGroup = AutoReplyFlag = 1

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(friend)
def reply_my_friend(msg):
    global Msg_Cnt
    global old_m, now_m , AutoReplyFlag
 
    if msg.text.__contains__('###') : 
        if AutoReplyFlag:
            AutoReplyFlag = 0
            return "收到, 已关闭自动回复。"
        else:
            AutoReplyFlag = 1
            return "收到, 已打开自动回复。"
    if AutoReplyFlag:
        now_time = datetime.datetime.utcnow() + datetime.timedelta(hours = 8)
        now_m = now_time.minute
        if now_m == old_m:
            Msg_Cnt = Msg_Cnt + 1
        else:
            Msg_Cnt = 0
            old_m = now_m
        
        if Msg_Cnt < Msg_Num_Lim:
            if msg.text.__contains__('下班') and not msg.text.__contains__('?'): 
                    return "好的，早点回去吧。"
#                 msg.reply("说： " + msg.text + "[机器人]")
        else:
            Msg_Cnt = Msg_Num_Lim
            
# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(LOL)
def reply_LOL(msg):
    global Msg_Cnt
    global old_m, now_m , AutoReplyFlagGroup
 
    today=int(time.strftime("%w"))
#     print(today)
    if msg.text.__contains__('###') : 
        if AutoReplyFlagGroup:
            AutoReplyFlagGroup = 0
            return "收到, 已关闭自动回复。"
        else:
            AutoReplyFlagGroup = 1
            return "收到, 已打开自动回复。"
    if AutoReplyFlagGroup and ((today is 6) or (today is 7)):
        now_time = datetime.datetime.utcnow() + datetime.timedelta(hours = 8)
        now_m = now_time.minute
        if now_m == old_m:
            Msg_Cnt = Msg_Cnt + 1
        else:
            Msg_Cnt = 0
            old_m = now_m
        
        if Msg_Cnt < Msg_Num_Lim:
            if msg.text.__contains__('搞起') : 
                return "搞起搞起。[Robot]"
            elif msg.text.__contains__('有人') or msg.text.__contains__('来'): 
                return "来啊来啊。[Robot]"
#                 msg.reply("说： " + msg.text + "[机器人]")
        else:
            Msg_Cnt = Msg_Num_Lim

@bot.register()
def reply_all(msg):
    global Msg_Cnt
    global old_m, now_m , AutoReplyFlag

    if AutoReplyFlag:
        now_time = datetime.datetime.utcnow() + datetime.timedelta(hours = 8)
        now_m = now_time.minute
        if now_m == old_m:
            Msg_Cnt = Msg_Cnt + 1
        else:
            Msg_Cnt = 0
            old_m = now_m
        
        if Msg_Cnt < Msg_Num_Lim:
            if msg.text.__contains__('新年快乐') : 
                return "新年快乐！"
            elif msg.text.__contains__('除夕快乐') : 
                return "除夕快乐！"

        else:
            Msg_Cnt = Msg_Num_Lim

#     return 'received: {} ({})'.format(msg.text, msg.type)

# @bot.register(bot.self, except_self=False)
# def reply_self(msg):
#     print(msg.text)
#     global Msg_Cnt
#     global old_m, now_m
#     now_time = datetime.datetime.utcnow() + datetime.timedelta(hours = 8)
#     now_m = now_time.minute
#     if now_m == old_m:
#         Msg_Cnt = Msg_Cnt + 1
#         print("Msg_Cntif: " + str(Msg_Cnt))
#     else:
#         Msg_Cnt = 0
#         old_m = now_m
#         print("Msg_Cntelse: " + str(Msg_Cnt))
#     if Msg_Cnt < Msg_Num_Lim:
#         msg.reply("狗屎刚才说： " + msg.text)
#     else:
#         Msg_Cnt = Msg_Num_Lim
# bot.join()
# bot.self.send("test")

if __name__ == '__main__':

    while True:
#         now_time = datetime.datetime.now()
        now_time = datetime.datetime.utcnow() + datetime.timedelta(hours = 8)
        now_h = now_time.hour
        now_m = now_time.minute
#         print(now_m)
        if Morning.hour == now_h and Morning.minute == now_m:
            friend.send('早上好！')
        if Night.hour == now_h and Night.minute == now_m:
            friend.send('晚上好！')
#         bot.self.send("test")
        time.sleep(50)
         
    bot.join()
             
    pass
    


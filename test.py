#coding=gbk
from wxpy import *
import datetime
import time

Ge_name = '���Ļ�'
Msg_Num_Lim = 5

bot = Bot(console_qr = True, cache_path=True)

# bot.file_helper.send('hello world!')

friends = bot.friends()

friend = friends.search(Ge_name, sex=FEMALE)[0]
Morning = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '7:40', '%Y-%m-%d%H:%M')
Night = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '23:00', '%Y-%m-%d%H:%M')
Msg_Cnt = 0
old_m = now_m = 0
# �ظ� my_friend ����Ϣ (����ƥ���ע��ĺ���!)
@bot.register(friend)
def reply_my_friend(msg):
    global Msg_Cnt
    global old_m, now_m
    now_time = datetime.datetime.utcnow() + datetime.timedelta(hours = 8)
    now_m = now_time.minute
    if now_m == old_m:
        Msg_Cnt = Msg_Cnt + 1
    else:
        Msg_Cnt = 0
        old_m = now_m

    if msg.text.__contains__('�°�'): 
        return "�õģ�����ȥ�ɡ�"
    if Msg_Cnt < Msg_Num_Lim:
        if Msg_Cnt == Msg_Num_Lim - 1:
            msg.reply(" �ϻ�̫�࣬ ����˵�ˣ� 88..." )
        else:
            msg.reply("��ʺ�ղ�˵�� " + msg.text)
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
#         msg.reply("��ʺ�ղ�˵�� " + msg.text)
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
            friend.send('���Ϻã�')
        if Night.hour == now_h and Night.minute == now_m:
            friend.send('���Ϻã�')
#         bot.self.send("test")
        time.sleep(50)
         
    bot.join()
             
    pass
    


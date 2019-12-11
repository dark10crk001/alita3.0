#coding=utf-8
from wxpy import *
import os,uuid,shutil
from alita import Alita

ai = Alita()
bot = Bot(cache_path=True) 
bot.enable_puid()
group = []

group.append(bot.groups().search('中软融通分公司业务群')[0])
group.append(bot.groups().search('自驾游协会')[0])
group.append(bot.groups().search('李桥高中96届妇女联合会')[0])
group.append(bot.groups().search('梦二')[0])
group.append(bot.groups().search('重庆交院汽车系2000届')[0])
group.append(bot.groups().search('同学群')[0])
group.append(bot.groups().search('玩乐帮')[0])
group.append(bot.friends().search('赵立仁')[0])
group.append(bot.friends().search('ALITA')[0])
group.append(bot.mps().search('桂林银行金融服务')[0])
group.append(bot.mps().search('北京中软融通科技有限公司')[0])
group.append(bot.mps().search('重庆农村商业银行直销银行')[0])
group.append(bot.mps().search('每周重庆')[0])


senders = []
for g in group:
    senders.append([g.puid,True])

def setSenderOnOff(puid,OnOff):
    for s in senders:
        if s[0] == puid:
            s[1] = OnOff

def getSenderOnOff(puid):
    for s in senders:
        if s[0] == puid:
            return s[1]
    return False

@bot.register(group,PICTURE, except_self=False)
def face_msg(msg):
    image_name = 'temp/' + msg.file_name
    friend = msg.chat
    print(msg.chat)
    print('接收图片')
    # face(image_name)
    try:
        msg.get_file(image_name)
        faces = face_dlib.detect(image_name)
    except Exception as e:
        print(e)
    if faces[0]==0:
        print(u'未检测到人脸')
        try:
            ret = baidu_ai_obj.detect(image_name)
            message = u"【%s】%s %s" % (ret["name"],ret['desc'],ret['url'])
            print(message)
            msg.reply(message)
        except:
            pass
    else:
        print(u'检测到人脸：',faces[0])
        # msg.reply(u'检测到人脸：%d' % faces[0])
        for f in faces[1]:
            ret = star.whoami(f)      
            if ret['star'] !='404':

                ret2 = baidu_ai.detect(f)
                beauty = 100
                age = 1000
                if ret2!= None:
                    beauty = ret2["beauty"]
                    age = ret2["age"]

                print(beauty,age)

                message = u"AI:%s，嗯，有点像【%s】 相似度:%s%%  颜值:%s 年龄:%s" % (ret['message'],ret['star'],ret['score'],beauty,age)

                print(message)
                msg.reply(message)
                msg.reply_image(f)

                starfile = '../tornado/%s' % ret['star_photo']
                
                print(starfile)

                if os.path.exists(starfile):
                    try:
                        temp_file = "temp/star_%s.jpg" % uuid.uuid4().hex
                        # shutil.copy(starfile,temp_file)
                        photo_tool.star_show(image_name,starfile,ret['star'],str(beauty),"%s%%"%ret['score'],str(age),temp_file)
                        msg.reply_image(temp_file) 
                    except Exception as e:
                        print("发送文件失败:",e)
            else:
                print('404，不做返回')

    #os.remove(image_name)
    #os.remove("face_detected_1.jpg")
 

@bot.register(group,TEXT, except_self=False)
def reply_ai(msg):    
    print(msg.sender.puid)
    print(msg.text)
    if (msg.type!='Text'):
        ret = 'AI:[奸笑][奸笑]'
    else:        
        ret = ai.answer(msg.text)
        print(ret)
        msg.reply(ret)

embed()
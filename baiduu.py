# encoding:utf-8
import requests
import json
import random

class BaiduUnit:
    def __init__(self):
        self.access_token = self.getBaiDuAK()

    def getBaiDuAK(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6KLfuk6DtEryd7vgKy7wBoHR&client_secret=rav13osL6U81jyxaHTCtpmoWdB0U4T0a'
        r = requests.get(host)
        return r.json()['access_token']
    
    def baiduApi(self,text):
        try:
            url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + self.access_token
            query = text
            #下面的log_id在真实应用中要自己生成，可是递增的数字
            log_id ='7758521'
            #下面的user_id在真实应用中要是自己业务中的真实用户id、设备号、ip地址等，方便在日志分析中分析定位问题
            user_id='222333'
            #下面要替换成自己的bot_id，是你的技能ID！！
            bot_id='79293'
            post_data = '{\"bot_session\":\"\",\"log_id\":\"'+log_id+'\",\"request\":{\"bernard_level\":2,\"client_session\":\"{\\\"client_results\\\":\\\"\\\", \\\"candidate_options\\\":[]}\",\"query\":\"' + query + '\",\"query_info\":{\"asr_candidates\":[],\"source\":\"KEYBOARD\",\"type\":\"TEXT\"},\"updates\":\"\",\"user_id\":\"'+user_id+'\"},\"bot_id\":'+bot_id+',\"version\":\"2.0\"}'
            # print (json.loads(post_data))
            headers = {'Content-Type':'application/json'}
            r = requests.post(url, data=post_data.encode('utf-8'),headers=headers)
            # print ()
            result = r.json()
            # print(result['result']['response']['action_list'])
            # print(len(result['result']['response']['action_list']))
            if result['result']['response']['action_list'] :
                return result['result']['response']['action_list'][random.randint(0,len(result['result']['response']['action_list'])-1)]['say']
            else:
                print("action_list none")
        except:
            print(result)
    
    def reply(self,text="你好"):
        if(len(text) > 0):
            result = self.baiduApi(text)
            return result
        else:
            return ""
 
if __name__ == "__main__":
    ai = BaiduUnit()
    ai.reply("你好")
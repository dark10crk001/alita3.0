# 与机器人对话：调用的是图灵机器人
import requests
import json
class TuLing:
    def __init__(self):
        # 图灵机器人的API_KEY、API_URL
        self.turing_api_key = "79c2d3a26034446ba043485404a79524"
        self.api_url = "http://openapi.tuling123.com/openapi/api/v2" # 图灵机器人api网址
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}
  
  
    # 图灵机器人回复
    def reply(self,text_words=""):
        req = {
            "reqType": 0,
            "perception": {
            "inputText": {
                "text": text_words
            },
        
            "selfInfo": {
                "location": {
                "city": "北京",
                "province": "北京",
                "street": "车公庄西大街"
                }
            }
            },
            "userInfo": {
            "apiKey": self.turing_api_key, # 你的图灵机器人apiKey
            "userId": "Nieson" # 用户唯一标识(随便填, 非密钥)
            }
        }
        
        req["perception"]["inputText"]["text"] = text_words
        response = requests.request("post", self.api_url, json=req, headers=self.headers)
        response_dict = json.loads(response.text)
        
        result = response_dict["results"][0]["values"]["text"]
        print("AI Robot said: " + result)
        return result

if __name__ == "__main__":
    tuling = TuLing()
    tuling.reply("你是谁")
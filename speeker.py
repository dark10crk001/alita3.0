import pyttsx3

class Speaker:
    def __init__(self): 
        print('初始化语音库')
        self.engine = pyttsx3.init() # 初始化语音库
        print('设置语速')
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', self.rate-10)
         
    def say(self,text):
        if text and len(text) > 0:
            print("ALITA:",text)
            self.engine.say(text) # 合成语音
            self.engine.runAndWait()

if __name__ == "__main__":
    sp = Speaker()
    sp.say("请插入你的银行卡")
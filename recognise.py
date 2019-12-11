# 音频文件转文字：采用百度的语音识别python-SDK
# 百度语音识别API配置参数
from aip import AipSpeech

class Recognition:
  def __init__(self):
    self.__APP_ID = '7023633'
    self.__API_KEY = 'liyMCxLhEsmQZ10TIXBwC2M5'
    self.__SECRET_KEY = '5c96379c38029b266ffadd93c005b481'
    self.client = AipSpeech(self.__APP_ID, self.__API_KEY, self.__SECRET_KEY)
    self.error = "ERROR"
  def recognise(self,filename="voices.wav"): # 将语音转文本STT
    # 读取录音文件
    with open(filename, 'rb') as fp:
      voices = fp.read()
    try:
      # 参数dev_pid：1536普通话(支持简单的英文识别)、1537普通话(纯中文识别)、1737英语、1637粤语、1837四川话、1936普通话远场
      result = self.client.asr(voices, 'wav', 16000, {'dev_pid': 1537, })
      # result = client.asr(get_file_content(path), 'wav', 16000, {'lan': 'zh', })
      # {'err_msg': 'speech quality error.', 'err_no': 3301, 'sn': '9495426851568098183'}
      # {'corpus_no': '6734930332586954481', 'err_msg': 'success.', 'err_no': 0, 'result': ['哼哼哼哼哼哼哼哼哼哼哼哼哼哼哼哼哼哼 哼哼哼哼哼哼哼。'], 'sn': '307171910251568098164'}
      # print(result)
      if result['err_no'] == 0:
        # print(result["result"][0])
        return result["result"][0]
      else:
        return self.error
    except KeyError:
      print("KeyError")
      return self.error

if __name__ == "__main__":
  reg = Recognition()
  ret = reg.recognise()
  print("result:",ret)
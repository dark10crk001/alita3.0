import speech_recognition as sr
  
class Recorder:
    def record(self,rate=16000,filename="voices.wav"):
        r = sr.Recognizer()
        with sr.Microphone(sample_rate=rate) as source:
            print("正在聆听...")
            audio = r.listen(source)
        
        with open(filename, "wb") as f:
            f.write(audio.get_wav_data())
        print("..........")

if __name__ == "__main__":
    rec = Recorder()
    rec.record()
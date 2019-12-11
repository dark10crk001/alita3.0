
import recognise,recorder,speeker,tuling,baiduu,fenci
from alita import Alita

class Nimani:
    def __init__(self):
        self.rec = recorder.Recorder()
        self.reg = recognise.Recognition()
        self.sp = speeker.Speaker()
        self.ai = Alita()
        self.fenci = fenci.Fenci()

    def run(self):
        while True:
            self.rec.record()
            text = self.reg.recognise()
            if text != self.reg.error:
                print("你:",text)
                result = self.ai.reply(text)
                self.sp.say(result)


if __name__ == "__main__":
    Nimani().run()
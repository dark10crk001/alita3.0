import sys
import fenci

class StopWord:
    def __init__(self):
        self.fc = fenci.Fenci()
        self.__filename = "stopwords/哈工大停用词表.txt"
        self.words = []
        for line in open(self.__filename,encoding='utf-8'): 
            self.words.append(line.strip('\n')) 

    def show_words(self):
        print(self.words)
    
    def cut(self,text):
        result = []
        ts = self.fc.cut(text)        
            # print(ts)
        for t in ts:
            if len(t) > 0:
                result.append(t)          
        return result

    def clean(self,text):
        result = []
        # ts = self.fc.cut_for_search(text)        
        ts = self.fc.cut(text)        
        # print(ts)
        for t in ts:
            if t not in self.words:
                if len(t) > 0:
                    result.append(t)   
        
        return result


if __name__ == "__main__":
    sw = StopWord()
    

    text = "你怎么听不懂普通话呢？"

    ret = sw.clean(text)
    print(ret)
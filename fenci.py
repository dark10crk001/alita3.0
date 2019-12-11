import jieba
import jieba.posseg as pseg #词性标注
import jieba.analyse as anls #关键词提取

class Fenci:
    def __init__(self):
        pass

    #全模式和精确模式
    def cut(self,word,cut_all=True):
        return jieba.cut(word, cut_all=True)

    #搜索引擎模式
    # def cut_for_search(self,word):
    #     return jieba.cut_for_search(word)

if __name__ == "__main__":
    seg_list = Fenci().cut("你一点也不好看")
    print("【cut】：" + "/ ".join(seg_list)) 

    seg_list = Fenci().cut_for_search("你一点也不好看")
    print("【cut for search】：" + "/ ".join(seg_list))  
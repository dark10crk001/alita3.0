import os
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.sorting import FieldFacet
from jieba.analyse import ChineseAnalyzer  
from stopwords import StopWord
from whoosh import scoring
########################################################################################################################################
from whoosh.qparser import QueryParser
from whoosh.index import open_dir
import random
from collections import Counter
####################################
import xlrd
import glob
from plugins import plugin

class Alita:
    def __init__(self):
        #创建知识库索引
        self.curpos_files = ["curpos/alita.xls","curpos/bank.xlsx"]
        context = self.read_context()
        self.create_index(context)
        self.plugin = plugin.Plugin()
        

    def read_context(self): #读取知识库
        context = []
        for curpos in self.curpos_files:
            workbook = xlrd.open_workbook(curpos)
            print("corpus %s loading..." % curpos)
            sheet = workbook.sheets()[0]
            id = 1
            for x in range(2,sheet.nrows):
                question = (sheet.cell(x,0).value)#.encode('utf-8')
                answer = (sheet.cell(x,1).value)#.encode('utf-8')
                context.append({"id":id,"question":question,"answer":answer,'category':'ai'})
                id = id + 1
        return context

    def create_index(self,context): #创建索引
        _analyser = ChineseAnalyzer()    #导入中文分词工具
        schema = Schema(id=NUMERIC(int,64,stored=True),category=TEXT(stored=True), answer=TEXT(stored=True),question=TEXT(stored=True,analyzer=_analyser))

        if not os.path.exists("index"):
            os.mkdir("index")
        ix = create_in("index", schema)

        writer = ix.writer()
        for cont in context:
            writer.add_document(id=cont['id'], question=cont['question'],answer=cont['answer'], category=cont['category'])
        writer.commit()

    def reply(self,question):
        ix = open_dir("index")
        with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
            
            keywords = StopWord().clean(question)            
            keywords.append(question)
            print("question keywords:",keywords)
            answers = []
            answers_ids = []
            for k in keywords:
                query = QueryParser("question", ix.schema).parse(k)
                print("query:",query)
                results = searcher.search(query, terms=True)
                # print(results)
                for hit in results:
                    answers.append({"id":hit['id'],"question":hit['question'],"answer":hit['answer'],'category':hit['category']})
                    answers_ids.append(hit['id'])
                # print("="*100)

            print("answers:")            
            for a in answers:
                print("id:" + str(a["id"]) + " q:" + a["question"] + " a:" + a["answer"])

            print("answers_ids",answers_ids)

            aws_ids = Counter(answers_ids).most_common(10)
            print("aws_ids:",aws_ids)

            a=[]
            for k,v in aws_ids:            
                for i in range(0,v*v): #增加答案权重
                    a.append(k)
            print("a:",a)

            if len(a) > 0:
                id = a[random.randint(0,len(a)-1)]

                for awer in answers:
                    if awer['id'] == id:
                        result = awer['answer']
                        if(result.startswith("cmd")):                           
                            return self.plugin.exec(result,keywords)
                        else:
                            return result

            return "我不知道该怎么回答你，看来我还要在学习。"

        
   
if __name__ == "__main__":

    a = Alita()
    while True:
        question = input("Please say somthing(Q for quit):")
        if question == "q":
            break
        else:
            rets = a.reply(question)                                                                                          
            print("Alita:",rets)

    
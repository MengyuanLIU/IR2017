import jieba
import jieba.analyse
import math
from numpy import  *
jieba.initialize()
docs=1000

def init():
    n=1
    words=[]
    num = 0
    myset=set()
    docnum=[]
    all=0
    while n<=docs:
        docname='F:\IR/0-'+str(n)+'.txt'
        allnum = 0
        with open(docname,'r') as f:
            date=f.readlines()
        nowdate=''
        for i in range(len(date)):
            if i>=6:
                nowdate=nowdate+date[i]
        result=jieba.lcut(nowdate,HMM=True)
        for i in result:
            if i !='，' and i!='、' and i!='“' and i!='”'and i!=']'and i!='［'and i !='；'and  i!='们' and i!='+':
                if i!='。' and i!='：' and i.strip() and i!='的' and i!=''and i!='是'and i!='在' and i!='地' and i!='得' :
                    if i!='了' and i!='《'  and i!='》' and i!='-' and i!='—' and i!='\u3000'and i!='（'and i!='）':
                        all = all + 1
                        allnum = allnum + 1
                        if i not in myset:
                            myset|={i}
                            words.append(i)
                            num=num+1
        docnum.append(allnum)
        n = n + 1
    return num,all,docnum,words

def tfidf1():
    wordnum,all,doc,word=init()
    avgdl=all/docs
    td = zeros((wordnum,docs))
    score = zeros((wordnum, docs))
    # print(all)
    i=0
    term=[]
    for w in word:
        term.append(w)
        i=i+1
    dindex=1
    idf={}
    tf={}
    for i in word:
        idf[i]=0
        tf[i]=None
    while dindex<=docs:
        docname = 'F://IR/0-' + str(dindex) + '.txt'
        dindex = dindex + 1
        with open(docname,'r') as f:
            data=f.readlines()
        nowdate = ''
        for i in range(len(data)):
            if i >= 6:
                nowdate = nowdate + data[i]
        wordlist=jieba.lcut(nowdate,HMM=True)
        visited={}
        for i in wordlist:
            if i in word:
                visited[i]=0
        for w in wordlist:
            if w in word:
                loc=term.index(w)
                td[loc][dindex-2]=td[loc][dindex-2]+1
                if visited[w] == 0:
                    idf[w]=idf[w]+1
                    visited[w]=1
                if tf[w]==None:
                    tf[w]=str(dindex-1)+'\t'
                else:
                    tf[w]=tf[w]+str(dindex-1)+'\t'
    
    for i in word:
        if idf[i]!=0:
            idf[i] = math.log(docs/idf[i])
        else:
            print(i)
    for i in range(wordnum):
        for j in range(docs):
            temp0=2*(0.25+0.75*(doc[j]/avgdl))
            temp=(td[i][j]*3)/(td[i][j]+temp0)
            score[i][j]=idf[term[i]]*temp
    # print(doc)
    with open ('C://Users/MayoL/Desktop/信息检索/test/score.txt','w')as f:
        s=''
        for i in range(wordnum):
            for j in range(docs):
                s=s+str(str(round(score[i][j],5))+'\t')
            s=s+'\n'
        f.write(s)
    with open ('C://Users/MayoL/Desktop/信息检索/test/word.txt','w')as f:
        for i in range(wordnum):
            s=term[i]
            f.write(s+'\n')
    with open ('C://Users/MayoL/Desktop/信息检索/test/TF.txt','w')as f:
        for i in word:
            s=str(i+'\t'+str(tf[i])+'\n')
            f.write(s)
    with open ('C://Users/MayoL/Desktop/信息检索/test/IDF.txt','w')as f:
         for i in word:
             s=str(i+'\t'+str(round(idf[i],2))+'\n')
             f.write(s)
tfidf1()





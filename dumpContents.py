#!/usr/local/bin/python3.6

import time
import requests
from bs4 import BeautifulSoup
SPACE=[' ','\xa0']
url=r'https://cjjc.weblio.jp/sentence/content/アスファルトルーフィング'
WHITE_LIST=['\xa0-\xa0中国語会話例文集', '\xa0-\xa0白水社 中国語辞典']

def dumpPageContents(url):
    try:
        print('Dump contents from:'+url)
        content=requests.get(url)
        soup=BeautifulSoup(content.text,'lxml')
        data=soup.select('#main > div.kijiWrp > div > div.qotC')
        with open('o','a') as w:
            for item in data :
                if 'class' not in item.contents[0].attrs or item.contents[0]['class'][0][-1]=='C':
                    #print(item.contents[0]['class'])
                    continue
                ans=''
                ans=ans+item.contents[0].text+'\t'
                if item.contents[1].contents[-1].text not in WHITE_LIST:
                    #WHITE_LIST.append(item.contents[1].contents[-1].text)
                    continue
                for it in item.contents[1].contents:
                    if it.name=='span':
                        continue
                    ans=ans+it.string
                w.write(ans+'\n')
        time.sleep(1)
    except Exception as e:
        with open('ErrorInfo','a') as f:
            f.write('Error occurs when dumping from '+url+' : '+str(e)+'\n')
        time.sleep(600)
#            print(str(WHITE_LIST))
#            print(ans)
#            print(item.contents[1].contents[-1].name)
                
#            w.write('\t'+item.contents[0]['class'][0][-1]+'\n')

def dumpContents(url):
    for i in range(1,6):
        dumpPageContents(url+'/'+str(i))
        
if __name__=='__main__':
    dumpContents(url)
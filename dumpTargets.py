import requests
import time
from bs4 import BeautifulSoup
from dumpContents import dumpContents

URL_ROOT=r'https://cjjc.weblio.jp/sentence/category/'
CONTENT_URL_ROOT='https://cjjc.weblio.jp/sentence/content/'

KANA_LIST=[
    'aa','ii','uu','ee','oo',
    'ka','ki','ku','ke','ko',
    'sa','shi','su','se','so',
    'ta','chi','tsu','te','to',
    'na','ni','nu','ne','no',
    'ha','hi','fu','he','ho',
    'ma','mi','mu','me','mo',
    'ya','yu','yo',
    'ra','ri','ru','re','ro',
    'za','zi','zu','ze','zo',
    'da','di','du','de','do',
    'ba','bi','bu','be','bo',
    'pa','pi','pu','pe','po'    
]



def dumpTargets(url):
    try:
        print('Dump Targets from :'+url)
        site=requests.get(url)
        soup=BeautifulSoup(site.text,'lxml')
    #  weblio life   
    # data=soup.select('#main > div.mainBoxB > div.CtgryLink > ul.CtgryUlL > li > a') 

    # weblio C-J
        data=soup.select('#main > div > div.CtgryLink > ul.CtgryUlL > li > a')
        ans=[]
        for item in data :
            ans.append(item.text)
        time.sleep(1)
        return ans
        with open('ErrorInfo','a') as f:
            f.write('Error occurs when dumping from '+url+' : '+str(e)+'\n')
        time.sleep(600)
        return []
    except Exception as e:
        with open('ErrorInfo','a') as f:
            f.write('Error occurs when dumping from '+url+' : '+str(e)+'\n')
        time.sleep(600)        

def dumpAllTargets():
    ans=[]
    for item in KANA_LIST :
        ans = dumpTargets(URL_ROOT+item)

        with open('targets','a') as f:
            for it in ans :
                dumpContents(CONTENT_URL_ROOT+it)
                f.write(item+'\n')
        for item2 in KANA_LIST :
            ans = dumpTargets(URL_ROOT+item+'-'+item2)
            with open('targets','a') as f:
                for it in ans :
                    dumpContents(CONTENT_URL_ROOT+it)
                    f.write(item+'\n')
    return ans


if __name__=='__main__':
    print(dumpTargets(URL_ROOT+'aa'))

    


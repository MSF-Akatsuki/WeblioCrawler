import pymysql
import requests
from sqlConfig import USER_NAME,PASSWORD
from dumpTargets import dumpAllTargets
from dumpContents import dumpContents

CONTENT_URL_ROOT='https://cjjc.weblio.jp/sentence/content/'

if __name__=='__main__':
    dumpAllTargets()
###
 #   with open('targets','a') as f:
#        for item in dumpAllTargets() :
#            dumpContents(CONTENT_URL_ROOT+item)
#            f.write(item+'\n')
###

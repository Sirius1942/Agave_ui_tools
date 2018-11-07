#encoding=utf-8
import sys
sys.path.append("..")
import json
import lib.log
import time
from lib.Draw import DrawClass
import csv
import json
import lib.log
import time
import ast
import os
import shutil
#参数初始化函数
def load():
    f=open("../conf.json")
    s=json.load(f)

    return s
#日志初始化
conf=load()
dlog=lib.log.getlogger(conf['log']['level'],conf['log']['filename']);



def getSymbol(ostype):
    if ostype =="windows":
        return "\\"
    if ostype =="linux":
        return "/"
        
symbol=getSymbol(conf['default']['os_type'])

save_f=conf['default']['img_type']

#参数检测函数
def printConf():

	for fdata in conf:
		for sa in conf[fdata]:
			dlog.info( "config data [%s], %s is: %s ",fdata,sa,conf[fdata][sa])

def getTime(num):

	# 按分钟计算减少的时间
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()-num*60)) 

def getDate():

	return time.strftime("%Y%m%d", time.localtime(time.time())) 

cvsimgfrom_path = conf['default']['cvsimgfrom_path']  #输出符合要求的图片路径
csvdata_path = conf['default']['csvdata_path']  #需要检查csv服务器
new_save_path = conf['default']['new_save_path']

# dlog.info("cvsto_path:%s",cvsto_path)
# dlog.info("csvdata_path:%s",csvdata_path)

suffix = ['.jpg']

def resizeImage(dir, suffix):

    #dir='..\result'
    for root, dirs, files in os.walk(dir):

        for file in files:
            filepath = os.path.join(root, file)
            #dlog.info("read data cvs is: %s",filepath)
            countnum = 0
            with open(filepath,encoding='UTF-8') as f:
                f_csv = csv.reader(f)
                headers = next(f_csv)

                for row in f_csv:
                    countnum=countnum+1
                    filename = row[0]
                    filepath = cvsimgfrom_path + symbol + filename + suffix[0]
                    dlog.debug('pic path: %s',filepath)


                    new_img_path = new_save_path
                    #drawpath=new_img_path+ symbol + filename + suffix[0]
                    d_start_time = time.time()
                    dc = DrawClass(filepath)
                    d_end_time = time.time()
                    dlog.info("Great dc time is: %d",d_end_time-d_start_time)

                    dc.drawSharp(int(row[4]), int(row[5]), int(row[6]), int(row[7]), row[8])
                    d_draw_time = time.time()
                    dlog.info("Great draw time is: %d", d_draw_time - d_end_time)
                    save_imge(filepath, new_img_path)

            dlog.info("read data cvs is: %s,num is %d", filepath,countnum)

def save_imge(filepath,new_path):
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(new_path)
    # print(isExists)
    # print("filepath: %s"+filepath)
    # print("new_path:%s"+new_path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录

        # 创建目录操作函数
        os.makedirs(new_path)
    try:

        shutil.copy(filepath,new_path)

    except FileNotFoundError as e:
        pass

if __name__ == '__main__':
    # start_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    start_time = time.time()
    dlog.info(start_time)
    resizeImage(csvdata_path, suffix)
    # end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    end_time = time.time()
    dlog.info(end_time-start_time)

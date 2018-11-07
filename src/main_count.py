#encoding=utf-8
import json
import lib.log
import time
import ast
import os
import shutil
from lib.MaJson import MaJsonReader
from lib.Draw import DrawClass
from lib.dexcel import DExcleClass

#参数初始化函数
def load():
    f=open("conf.json")
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

save_path = conf['default']['save_path']  #输出符合要求的图片路径
draw_path = conf['default']['draw_path']  #需要检查的图片路径

dlog.info("save_path:%s",save_path)
dlog.info("draw_path:%s",draw_path)

suffix = ['json']

def resizeImage(dir, suffix):
    #print('resizeImage')
    num = 0
    all_files=0
    allfalse_folder=0

    for root, dirs, files in os.walk(dir):
        s=root.split(symbol)[-1]#截取路径
        new_path = draw_path + symbol + s
        save_num=0
        dlog.info(s)
        dlog.info(u"图片保存目录： %s"+root)
        num=num+1
        

        for file in files:
            shapes_num=0
            filepath = os.path.join(root, file)
            filesuffix = os.path.splitext(filepath)[1][1:]
            right_num=0
            file_name=filepath.split(symbol)[-1]#截取路径
            # dlog.info("filename: %s",file_name)
            #print(filepath)
            if filesuffix in suffix:  # 遍历找到指定后缀的文件名['json']
                
                dec=DExcleClass()
                json_file=MaJsonReader(filepath)
                shapes_num=shapes_num+len(json_file.getShapes())

                
                #save_imge(new_file,new_path)

                    #print("")
                    #save_imge(file,new_path_error)
                dlog.info(u"目录中的框数目:%s",shapes_num)

if __name__ == '__main__':
    # start_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    start_time = time.time()
    dlog.info(start_time)
    resizeImage(save_path, suffix)
    # end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    end_time = time.time()
    dlog.info(end_time-start_time)


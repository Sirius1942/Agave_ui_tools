#encoding=utf-8
import json
import lib.log
from lib.MaJson import MaJsonClass


if __name__ == '__main__':
    # start_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #start_time = time.time()
    from_path="D:\\work\\labelimg\\data\\data4\\000100.json"
    save_path="D:\\work\\labelimg\\data\\data4\\data6"
    #dlog.info(start_time)
    
    MJ=MaJsonClass()
    new_file=MJ.get("t2.json",from_path,save_path,"\\")

    # print MJ.getdict()
    # end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #end_time = time.time()
   # dlog.info(end_time-start_time)


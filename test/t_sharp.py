#encoding=utf-8
import json
import lib.log
from lib.MaJson import MaJsonReader


if __name__ == '__main__':
    # start_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #start_time = time.time()
    from_path="D:\\work\\labelimg\\data\\data4\\data5\\000002.json"
    #save_path="D:\\work\\labelimg\\data\\data4\\data6"
    #dlog.info(start_time)
    
    MJ=MaJsonReader(from_path)
    shapes=MJ.getShapes()

    for shape in shapes:
        print shape[0]
        print shape[1][0]

    # end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #end_time = time.time()
   # dlog.info(end_time-start_time)
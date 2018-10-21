import os 
from datetime import datetime 
import shutil 

# 创建文件夹
def create_folder(parent_folder,sub_folder=None):
    if not os.path.exists(parent_folder):
        os.mkdir(parent_folder)
    if sub_folder != None:
        os.chdir(parent_folder)
        if not os.path.exists(sub_folder):
            print('子文件夹{}不存在, 创建中...'.format(sub_folder))
            os.mkdir(sub_folder)
        else:
            shutil.rmtree(sub_folder)
            os.mkdir(sub_folder)
        os.chdir('../')


if __name__ == "__main__":
    create_folder('reports','2018-10-21')


  

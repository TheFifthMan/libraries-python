# 寻找给定路径下的所有py文件
# os.walk(top, topdown=True, onerror=None, followlinks=False)
import os
'''
top: 给定的路径
topdown: 自上而下搜索
onerror: 函数，调用需要传一个参数，OSError实例，出现错误后执行
followelinks: 通过软连接进行访问


dirname: 返回文件夹的相对路径
dirpath: 返回的是一个集合，是当前遍历到的所有文件夹的集合
filenames: 返回的也是一个集合，文件名集合
'''
def walk_folder(top,extension,absolute=False,relative=False,topdown=True, onerror=None, followlinks=False):
    '''
    top: 给定路径进行搜索
    extension: 给定搜索文件的后缀
    absolute: 返回绝对路径
    relative: 返回先对路径
    如果absolute和relative均为False，则返回找到的文件名
    '''
    files = []
    for dirname,dirpath,filenames in os.walk(top,topdown=topdown,onerror=onerror,followlinks=followlinks):
        for file in filenames:
            if os.path.splitext(file)[1] == extension:
                if absolute and relative:
                    print('Chose absolute or relative')
                    return 

                elif absolute:
                    absolute_path = os.path.join(os.getcwd(),os.path.join(dirname,file))
                    print(absolute_path)
                    files.append(absolute_path)

                elif relative:
                    absolute_path = os.path.join(dirname,file)
                    print(absolute_path)
                    files.append(absolute_path)
                else:
                    print(file) 
                    files.append(file)

    return files


if __name__ == "__main__":
    walk_folder('.','.py',True,False)
    walk_folder('.','.py',False,True)
    walk_folder('.','.py',True,True)
    walk_folder('.','.py',False,False)

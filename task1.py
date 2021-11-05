import os
import hashlib
import functools

#输出文件的存储路径
def savepath():
    global savepath
    savepath=input('please input the target path:')
    return savepath

#判断子文件夹
def judge(path):
    if os.path.isdir(path)==True:
        list_files = os.listdir(path)
        return list_files

# 合并
def add(x, y):
    return x + y

#合成文件路径
def addpath(file):
    path = dir_root+'\\'+file
    return path

#获得文件的绝对路径
def getpath(path):
    os.chdir(path)
    global dir_root
    dir_root=os.getcwd()
    list_files=os.listdir(path)
    list_files=list(map(addpath,list_files))
    return list_files

def getfile(path):
    os.chdir(path)
    list_items = list( map(os.path.abspath,list(os.listdir(path))))
    list_files = list(filter(os.path.isfile, list_items))
    if list_files!=None:
        list(map(compute_hash,list_files))
    list_dirs = list(filter(os.path.isdir, list_items))
    if list_dirs!=None:
        if list(map(judge,list_dirs))!=None:
            list(map(getfile,list_dirs))
        else:
            list_dirs = list(map(getpath, list_dirs))
            list_dirs = list(functools.reduce(add,list_dirs))
            list(map(compute_hash,list_dirs))

# 计算文件的md5和sha256值并写入文件
def compute_hash(file):
    with open(file,'rb') as f:
        data = f.read()
        filepath=os.path.abspath(file)
        file_md5 = hashlib.md5(data).hexdigest()
        file_sha256 = hashlib.sha256(data).hexdigest()
        result = filepath + '     ' + file_md5 + '      ' + file_sha256 + '\n'
    with open(savepath, 'a') as fp:
        fp.write(result)

if __name__=='__main__':
    thepath=input('input a path:')
    savepath()
    getfile(thepath)


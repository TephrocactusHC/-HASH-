'''
#coding : utf-8
#@Time : 2021/10/723:48
#@Author : myc
#@File : 5yery.py
#@Software : PyCharm
import hashlib
f = open(r'D:\Thursday\demo1\停词表.txt','rb')
fr = f.read()
sha256obj = hashlib.sha256(fr).hexdigest()
md5obj = hashlib.md5(fr).hexdigest()
f.close()
result = open(r'D:\Thursday\demo1\result.txt','a')
result.write(md5obj+'\n'+sha256obj+'\n')
result.close()
'''

#coding : utf-8
#@Time : 2021/10/723:48
#@Author : myc
#@File : 5yery.py
#@Software : PyCharm

import hashlib,os
# 获取文件的地址
def GetPath():
    file_path = input('please input the path:')
    return file_path

# 生成文件的MD5值
def file_md5(content):
    md5gen = hashlib.md5()
    with open(content, 'rb') as fd:
        data = fd.read()
        md5gen.update(data) #通过update方法传入生成器
        md5code = md5gen.hexdigest()
        return md5code

# 生成文件的SHA256值
def file_sha256(content):
    sha256gen = hashlib.sha256()
    with open(content, 'rb') as fd:
        data = fd.read()
        sha256gen.update(data)
        sha256code = sha256gen.hexdigest()
        return sha256code

if __name__=='__main__':
    thePath=GetPath()
    sha256obj = file_sha256(thePath)
    md5obj = file_md5(thePath)
    with open(r'D:\Thursday\demo1\result.txt','a') as result:      #将结果写入新的文件
        result.write(md5obj+'\n'+sha256obj+'\n')


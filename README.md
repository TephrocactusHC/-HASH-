# -HASH-
Output all files and their HASH
输出一个文件夹内所有文件的文件名和他们的哈希值（MD5、SHA256），包括子文件夹。
不能用在C盘，或者其他盘里有禁止读取的文件时，也会报错。
没有使用try/except，可以自己写来解决上述问题\t
面向函数编程，不使用或少使用for循环。如果用for循环，这个程序会大大简化,通过os.path.join来实现

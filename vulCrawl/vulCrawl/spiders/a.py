import os

test_report="./vul-file/"
lists = os.listdir(test_report)
print(list)
#按时间排序
lists.sort(key=lambda fn:os.path.getmtime(test_report+fn))
#获取最新的文件保存到file_new
file_new = os.path.join(test_report,lists[-1])                    
print(file_new)

os.system('echo python3 a.py >2.txt')

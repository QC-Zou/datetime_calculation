import datetime
import os
'''
if os.path.exists("dest.txt"):
    os.remove("dest.txt")
'''
f = open('time.txt', 'r')
for line in f.readlines():
    line = line.strip()
    line = line.split("	")
    #print(line)
    d1 = line[0]
    d2 = line[1]
    program_name = line[2]
    dd1 = datetime.datetime.strptime(d1, '%Y-%m-%d %H:%M:%S')
    dd2 = datetime.datetime.strptime(d2, '%Y-%m-%d %H:%M:%S')
    print(program_name, ":", dd2 - dd1)

'''
    duration = dd2-dd1
    duration.strftime('%Y-%m-%d %H:%M:%S')
    str = name+d1+d2+duration

    file_write_obj = open("dest.txt", 'w')
    file_write_obj.writelines(str)
    file_write_obj.write('\n')
    file_write_obj.close()
'''





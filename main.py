# -*- coding: utf-8 -*-
import shutil
import datetime
#import os
from time import sleep

cur_filename = "/Users/huangyunpeng/tmp/test.txt"
sleep(10)
for i in range(1,100):
    cur_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    back_filename = "backfile/" + cur_time + ".txt"
    print(back_filename)
    shutil.copy(cur_filename,back_filename)
    sleep(10)
# import threading
# import time
# def print_num():
#     for i in range(6):
#         print(i)
#         time.sleep(1)
# def print_let():
#     for j in 'abcd':
#         print(j)
#         time.sleep(2)
# thread1=threading.Thread(target=print_num)
# thread2=threading.Thread(target=print_let)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("completed successfully")

##

import threading
import time
def msg(masg1,inter):
    for _ in range(3):
        
        time.sleep(inter)
        print (masg1)
thread1=threading.Thread(target=msg,args=("hello !",1))
thread2=threading.Thread(target=msg,args=("world",3 ))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

    
import threading
from datetime import datetime
import time
def add():
    sum1=0;
    for i in range(10):
        sum1=sum1+1;
        print("sum=2",sum1);
        while True:
            time.sleep(1);
            print('i love you ');
            print("time1=\n",datetime.now());
            time.sleep(1);
def mult():
    prod=1;
    for i in range(10):   
        prod=prod*i;
        while True:
            time.sleep(1);
            print("i love you too");
            print("time2=\n",datetime.now());
            time.sleep(1);
t1=threading.Thread(target=add,name="first",kwargs=None);
t2=threading.Thread(target=mult,name="second",kwargs=None);
t1.start()
t2.start()



    

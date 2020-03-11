import threading as th;
import time
#申请一把锁
lock = th.Lock()


def main(count=None):
    print(time.time())
    #加锁
    #lock.acquire();

    print(count);
    time.sleep(1);
    #释放锁
    #lock.release();



if __name__ == '__main__':
    for i in range(10):
        m=th.Thread(target=main(i));
        m.start();
    print(1);


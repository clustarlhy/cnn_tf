import time
import os

pre_step = 0
step = 0

def do_file_exists(pre_step,step):
    t0 = time.time()
    while True: 
      time.sleep(1)
      with open("data.txt", 'r') as file:
        list = file.readlines()
        data = list[len(list)-1]
        data_new = data.strip('[]')
        data_list = data_new.split(',')
        step = int(data_list[0])
        if (step > pre_step) and step > 0:
            t0 = time.time()
            print(data)
            pre_step = step
        elif time.time() - t0 > 20:
            break
        file.close()

if __name__ == '__main__':
    t = time.time()
    while os.path.exists('data.txt') == False:
        if time.time() - t > 100:
            raise RuntimeError('no file created!')
    do_file_exists(pre_step=pre_step,step=step)
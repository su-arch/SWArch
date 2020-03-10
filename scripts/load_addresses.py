import json
import sys
sys.path.append('/Users/xxx0624/SWArch/5200_flask_app/app')
from db_functions import *
import threading  
import logging


logger = logging.getLogger('5200_flask_app')
hdlr = logging.FileHandler('/var/tmp/5200_flask_app.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)                                                          


def process(items, start, end):
    for index in range(start, end, 1):
        print (index)
        item = items[index]
        try:
            create(item)
        except Exception:
            print ('error with item: ', index)
            logger.error(index + item)


if __name__ == '__main__':
    file_path = sys.argv[1]
    all_data = None
    with open(file_path) as f:
        all_data = json.load(f)
    threads = []
    threads_num = 50
    per_share_size = len(all_data) / threads_num
    start_index = 0
    while start_index < len(all_data):
        end_index = start_index + per_share_size
        threads.append(threading.Thread(
            target=process, args=(all_data, int(start_index), int(end_index))))       
        threads[-1].start() # start the thread we just created
        start_index = end_index
    
    # wait for all threads to finish                                            
    for t in threads:                                                           
        t.join()
    print ('done')
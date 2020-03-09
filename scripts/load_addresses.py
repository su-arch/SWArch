import json
import sys
sys.path.append('/Users/xxx0624/SWArch/5200_flask_app/app')
from db_functions import *

if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path) as f:
        data = json.load(f)
    print (len(data))
    index = 0
    for d in data:
        print (index, ': ', d)
        create(d)
        index += 1
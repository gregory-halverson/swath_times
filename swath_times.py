import os
from glob import glob

base_path = '/nobackup0/omega/halverso/evapotranspiration_data/sources/MOD07_L2'

date_list = glob(os.path.join(base_path, '*'))

for directory in date_list:
    date_string = os.path.basename(directory)
    print(date_string)
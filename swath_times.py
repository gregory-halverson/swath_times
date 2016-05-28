import os
from glob import glob

base_path = '/nobackup0/omega/halverso/evapotranspiration_data/sources/MOD07_L2'

date_list = glob(os.path.join(base_path, '*'))

date_list.sort()

for directory in date_list:
    date_string = os.path.basename(directory)
    print(date_string)

    swath_list = glob(os.path.join(directory, '*.hdf'))

    swath_list.sort()

    for filename in swath_list:
        filename_base = os.path.basename(filename)
        swath_name = filename_base.split('.')[2]
        print(swath_name)

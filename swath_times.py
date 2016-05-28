from glob import glob

base_path = '/nobackup0/omega/halverso/evapotranspiration_data/sources/MOD07_L2'

date_list = glob(base_path)

print(date_list)
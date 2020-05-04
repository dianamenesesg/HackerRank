
# Example Python program that creates a hierarchy of groups
# and datasets in a HDF5 file using h5py
# https://pythontic.com/hdf5/h5py/create_group

import h5py
import random
import numpy.random

# Create a HDF5 file
hierarchicalFileName = "Hierarchical.hdf5"
hierarchicalFile = h5py.File(hierarchicalFileName, "w")

# Create a group under root
grp1 = hierarchicalFile.create_group("Group1")
grp2 = grp1.create_group("Group2")
grp3 = grp2.create_group("Group3")

# Use dictionary notation to create a dataset inside a group
grp3["numbers"] = [1, 2, 3]
grp3["letters"] = [b'a', b'b']
# Print the groups
print(hierarchicalFile["/"])
print(grp1)
print(grp2)
print(grp3)
hierarchicalFile.close()

hf = h5py.File(hierarchicalFileName, "r")
print('aqui keys', hf.keys())
for i in hf['Group1']['Group2']['Group3'].keys():
    print(hf['Group1']['Group2']['Group3'][i].value)



import numpy as np
import h5py
import os

def save_dict_to_hdf5(dic, filename):

    with h5py.File(filename, 'w') as h5file:
        recursively_save_dict_contents_to_group(h5file, '/', dic)

def load_dict_from_hdf5(filename):

    with h5py.File(filename, 'r') as h5file:
        return recursively_load_dict_contents_from_group(h5file, '/')



def recursively_save_dict_contents_to_group( h5file, path, dic):

    # argument type checking
    if not isinstance(dic, dict):
        raise ValueError("must provide a dictionary")        

    if not isinstance(path, str):
        raise ValueError("path must be a string")
    if not isinstance(h5file, h5py._hl.files.File):
        raise ValueError("must be an open h5py file")
    # save items to the hdf5 file
    for key, item in dic.items():
        #print(key,item)
        key = str(key)
        if isinstance(item, list):
            item = np.array(item)
            #print(item)
        if not isinstance(key, str):
            raise ValueError("dict keys must be strings to save to hdf5")
        # save strings, numpy.int64, and numpy.float64 types
        if isinstance(item, (np.int64, np.float64, str, np.float, float, np.float32,int)):
            #print( 'here' )
            h5file[path + key] = item
            if not h5file[path + key].value == item:
                raise ValueError('The data representation in the HDF5 file does not match the original dict.')
        # save numpy arrays
        elif isinstance(item, np.ndarray):            
            try:
                h5file[path + key] = item
            except:
                item = np.array(item).astype('|S9')
                h5file[path + key] = item
            if not np.array_equal(h5file[path + key].value, item):
                raise ValueError('The data representation in the HDF5 file does not match the original dict.')
        # save dictionaries
        elif isinstance(item, dict):
            recursively_save_dict_contents_to_group(h5file, path + key + '/', item)
        # other types cannot be saved and will result in an error
        else:
            #print(item)
            raise ValueError('Cannot save %s type.' % type(item))

def recursively_load_dict_contents_from_group( h5file, path): 

    ans = {}
    for key, item in h5file[path].items():
        if isinstance(item, h5py._hl.dataset.Dataset):
            ans[key] = item.value
        elif isinstance(item, h5py._hl.group.Group):
            ans[key] = recursively_load_dict_contents_from_group(h5file, path + key + '/')
    return ans            

d1 = [1,2,3]
d2 = ['a', 'b']
data = {'numbers':d1, 'letters':d2}
#print('esta eh a data', data)
filename = 'test.h5'
save_dict_to_hdf5(data, filename)
dd = load_dict_from_hdf5(filename)
#print(dd)
#print('keys', dd.keys())

hf = h5py.File('foo.hdf5','w')
hf.create_group("somegroup", )
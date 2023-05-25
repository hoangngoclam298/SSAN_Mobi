import random
import os
import csv
import pandas as pd
import numpy as np

def re_list(base):
    train_live = os.listdir(os.path.join(base, 'live'))
    train_not_live = os.listdir(os.path.join(base, 'not_live'))
    list_info = []
    for x in train_live:
        list_info.append([x, 1])
    for x in train_not_live:
        list_info.append([x, 0])
    random.shuffle(list_info)

    with open(os.path.join(base, 'list.csv'), mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(list_info)

# re_list(r'C:\Users\LAMHN\Documents\Mobifone\small_dataset\small_dataset\train1')
# re_list(r'C:\Users\LAMHN\Documents\Mobifone\small_dataset\small_dataset\train2')
# re_list(r'C:\Users\LAMHN\Documents\Mobifone\small_dataset\small_dataset\train3')
# re_list(r'C:\Users\LAMHN\Documents\Mobifone\small_dataset\small_dataset\val')

# df = pd.read_csv(r'C:\Users\LAMHN\Documents\Mobifone\small_dataset\small_dataset\train1\list.csv', delimiter=",", header=None)

a = np.ones((3,3))
b[1,:,:] = a
print(a)
print(b)
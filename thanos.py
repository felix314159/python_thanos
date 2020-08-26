"""If you repeatedly run this only thanos.py himself survives"""
from random import shuffle
import os


def snap(path):
    arr = os.listdir(path)
    shuffle(arr)
    for i in arr[:int(len(arr)/2)]:
        weakling = path + "\\" + i
        os.remove(weakling)


# be brave and spice it up be picking a random folder from c:
snap(os.getcwd())
from libs.seg import Seg
from time import sleep

my_seg=Seg(15,21,4,22,23,5,18,19)

while True:
    for i in range(9):
        my_seg.display_number(i)
        sleep(0.5)


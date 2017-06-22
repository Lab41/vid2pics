import numpy as np
import cv2
import os
import sys


def find_work(topdir,filetypes):
    retval = []
    for dirpath, dirnames, files in os.walk(topdir):
        for name in files:
            if name.lower().split('.')[-1] in filetypes:
                retval.append(name)
    return retval


def write_frame(img,work_item, outdir, frame_number):
    file_name = os.path.join(outdir,'{0}-{1:06}.png'.format(work_item,frame_number)) 
    cv2.imwrite(file_name,img)

def process(in_dir,out_dir):
    print('Examining input dir for work')
    work_items = find_work(in_dir,['avi','mov','mp4'])
    print ('Found {0} work items'.format(len(work_items)))
    for work_item in work_items:
        print('Working on: {0}'.format(work_item))
        frame_num = 0
        cap = cv2.VideoCapture(os.path.join(in_dir,work_item))
        while (cap.isOpened()):
            ret,frame = cap.read()
            print('frame: {0} ret:{1}'.format(frame_num,ret)) 
            if ret == True:
                write_frame(frame,work_item,out_dir,frame_num)
               
            frame_num += 1 
            

if __name__ == "__main__":
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    process(in_dir,out_dir)

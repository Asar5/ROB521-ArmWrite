#!/usr/bin/python3
# coding=utf8

from Segmentation import Segmentation
import time
import numpy as np


def letter_H(start_point, height, width):
    seg1 = Segmentation()
    seg1.code_initialize()
    set_pts = []
    # result1 = AK.setPitchRangeMoving(start_point, -90, -90, 0, 100)
    time.sleep(1)
    end_pt1 = (start_point[0], start_point[1] - height, start_point[2])
    set_pts.append(list(end_pt1))
    point_list1 = seg1.straight_line(start_point, end_pt1)
    set_pts.extend(point_list1)
    #AK.setPitchRangeMoving((end_pt1[0], end_pt1[1], end_pt[2]+5), -90, -90, 0, 100)
    #time.sleep(0.5)
    #AK.setPitchRangeMoving((end_pt1[0], end_pt1[1], end_pt[2]+5), -90, -90, 0, 100)
    end_pt2 = (end_pt1[0], end_pt1[1] + height/2, end_pt1[2])
    set_pts.append(list(end_pt2))
    # AK.setPitchRangeMoving(end_pt2, -90, -90, 0, 100)
    end_pt3 = (end_pt2[0] - width, end_pt2[1], end_pt2[2])
    set_pts.append(list(end_pt3))
    point_list2 = seg1.straight_line(end_pt2, end_pt3)
    set_pts.extend(list(point_list2))
    end_pt4 = (end_pt3[0], end_pt3[1] - height/2, end_pt3[2])
    set_pts.append(list(end_pt4))
    # AK.setPitchRangeMoving(end_pt4, -90, -90, 0, 100)
    end_pt5 = (end_pt4[0], end_pt4[1] + height, end_pt4[2])
    set_pts.append(list(end_pt5))
    point_list3 = seg1.straight_line(end_pt4, end_pt5)
    set_pts.extend(point_list3)
    return np.asarray(set_pts)

def letter_B(start_point, height, width):
    seg1 = Segmentation()
    seg1.code_initialize()
    set_pts = []
    # result1 = AK.setPitchRangeMoving(start_point, -90, -90, 0, 100)
    time.sleep(1)
    
    end_pt1 = (start_point[0], start_point[1] - height, start_point[2])
    set_pts.append(list(end_pt1))
    point_list1 = seg1.straight_line(start_point, end_pt1)
    set_pts.extend(point_list1)
    
    end_pt2 = (end_pt1[0] - 1, end_pt1[1], end_pt1[2])
    point_list2 = seg1.straight_line(end_pt1, end_pt2)
    set_pts.extend(list(point_list2))
    
    end_pt3 = (end_pt2[0], end_pt2[1] + height/2, end_pt2[2])
    point_list3 = seg1.small_sem_cir(end_pt2, end_pt3,1)
    set_pts.extend(list(point_list3))
    
    end_pt4 = (end_pt3[0] + 1, end_pt3[1], end_pt3[2])
    point_list4 = seg1.straight_line(end_pt3, end_pt4)
    set_pts.extend(list(point_list4))
    
    # AK.setPitchRangeMoving(end_pt3, -90, -90, 0, 100)
    time.sleep(0.5)
    
    end_pt5 = (end_pt3[0], end_pt3[1] + height/2, end_pt3[2])
    point_list5 = seg1.small_sem_cir(end_pt3, end_pt5, 1)
    set_pts.extend(list(point_list5))
    
    point_list6 = seg1.straight_line(end_pt5,start_point)
    set_pts.extend(list(point_list6))
    
    return np.asarray(set_pts)

def letter_O(start_point, height, width):
    seg_o = Segmentation()
    set_pts = []
    set_pts.append(list(start_point))
    z = start_point[2]

    end_pt1 = (start_point[0], start_point[1] - height, z)
    end_pt2 = (end_pt1[0] - width, end_pt1[1], z)
    end_pt3 = (end_pt2[0],  end_pt2[1] + height, z)

    line1 = seg_o.straight_line(start_point, end_pt1)
    set_pts.extend(list(line1))

    line2 = seg_o.straight_line(end_pt1, end_pt2)
    set_pts.extend(list(line2))

    line3 = seg_o.straight_line(end_pt2, end_pt3)
    set_pts.extend(list(line3))

    line4 = seg_o.straight_line(end_pt3, start_point)
    set_pts.extend(list(line4))

    return np.asarray(set_pts)

def letter_R(start_point, height, width):
    seg_r = Segmentation()
    set_pts = []
    set_pts.append(list(start_point))
    z = start_point[2]

    end_pt1 = (start_point[0], start_point[1] - height, z)
    end_pt2 = (end_pt1[0] - width, end_pt1[1], z)
    end_pt3 = (end_pt2[0],  end_pt2[1] + height/2, z)
    end_pt4 = (end_pt3[0] + width, end_pt3[1], z)
    end_pt5 = (end_pt4[0] - width, end_pt4 + height/2, z)

    line1 = seg_r.straight_line(start_point, end_pt1)
    set_pts.extend(list(line1))

    line2 = seg_r.straight_line(end_pt1, end_pt2)
    set_pts.extend(list(line2))

    line3 = seg_r.straight_line(end_pt2, end_pt3)
    set_pts.extend(list(line3))

    line4 = seg_r.straight_line(end_pt3, end_pt4)
    set_pts.extend(list(line4))

    line5 = seg_r.straight_line(end_pt4, end_pt5)
    set_pts.extend(list(line5))

    return np.asarray(set_pts)

    
if __name__ == '__main__':
    height = 5.8
    width = 3.5
    letter_origin = (0, 20, 8)
    #set_pts_H = letter_H((0, 20, 8), height, width)
    #set_pts_B = letter_B((0, 20, 8), height, width)
    #letter_files = {"H": set_pts_H}
    #a_file = open("letter_data.json", "w")
    #a_file = json.dump(letter_files, a_file)
    #print(set_pts_B)
    # seg1 = Segmentation()
    # seg1.code_initialize()
    # AK.setPitchRangeMoving((0, 20, 8), -90, -90, 0, 100)
    # point_listx, point_listy = seg1.generate_semicircle(0, 20, 8, 3, 1)
    # print(point_listy)
    O = letter_O(letter_origin, height, width)
    print(O)
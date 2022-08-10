import numpy as np
import itertools as it
from collections import defaultdict


def preproc_array(array, start, end):
    return [tuple([int(x) for x in line.split(',')]) for line in array[start:end]]


def l1_dist(x, y):
    return [a-b for a,b in zip(x,y)]


def get_orientation(point, i):
    point = [point[abs(x)-1] for x in orientations[i]]
    signs = np.divide(orientations[i],np.abs(orientations[i]))
    x, y, z = np.multiply(point, signs)
    return x, y, z


rotations = list(it.product([-1, 1], repeat=3)) 
permutations = list(it.permutations([1, 2, 3]))
orientations = [np.multiply(rot, per) for rot, per in it.product(rotations, permutations)]

def main():
    f = open('input.txt', 'r').read().splitlines()
    scanners = []
    beacons_dict = {}
    count = 0
    for i, line in enumerate(f):
        
        if i==len(f) -1:
            count+=1
            array = preproc_array(f, prev+1, i+1)
            scanners.append(array)
        
        elif len(line) == 0:
            count += 1
            array = preproc_array(f, prev+1, i)
            scanners.append(array)
   
        elif line[:3] == '---':
            prev  = i

    beacons_map = set(scanners.pop(0))
    coords_list = []
    coords_list.append([0, 0, 0])
    while scanners:
        not_found = False
        scanner = scanners.pop(0)
        for j in range(len(orientations)):
            offsets = defaultdict(int)
            for other_beacon in beacons_map:
                for this_beacon in scanner:
                    point = get_orientation(this_beacon, j)
                    offset = tuple([x-y for x,y in zip(point, other_beacon)])
                    offsets[offset] +=1
            for offset in offsets.keys():
                if offsets[offset] >=12:
                    not_found = True
                    for beacon in scanner:
                        oriented_point = tuple([x-y for x,y in zip(get_orientation(beacon, j), offset)])
                        beacons_map.add(oriented_point) 
        if not_found:
            scanners.append(scanner)
    print(len(beacons_map)) 
    



if __name__ == '__main__':
    main()
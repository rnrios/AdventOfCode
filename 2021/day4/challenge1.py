import numpy as np


def return_num_vec(txt_list, start, end, sep):
    foo = ['', ' ']
    num_vec = []
    for i in range(start, end):
        num_vec.append([int(x) for x in txt_list[i].split(sep) if x not in foo])
    return np.array(num_vec)


def create_grids(f):
    grids = []
    masks = []
    file_len = int((len(f)-1)/6)
    for i in range(file_len):
        grid, mask = create_grid(f, 6*i+2, 6*i+7, ' ')
        masks.append(mask)
        grids.append(grid)
    return grids, masks


def create_grid(txt_list, start, end, sep):
    grid = return_num_vec(txt_list, start, end, sep)
    mask = np.zeros(grid.shape)
    return grid, mask


def update_masks(num, grid, mask):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if num == grid[i][j]:
                mask[i][j] = 1
    return mask


def check_line(mask):
    total = mask.shape[0]
    for i in range(total):
        if np.sum(mask[i, :]) == total:
            return True
    return False


def check_column(mask):
    total = mask.shape[1]
    for i in range(total):
        if np.sum(mask[:, i]) == total:
            return True
    return False


def main():
    f = open('input.txt', 'r').read().splitlines()
    window = np.squeeze(return_num_vec(f, 0, 1, ','))
    grids, masks = create_grids(f)
    for num in window:
        for mask,grid in zip(masks, grids):
            mask = update_masks(num, grid, mask)
            if check_line(mask) or check_column(mask):
                unmarked = np.sum(grid) - np.sum(mask*grid)
                print('Winning number: {}\t Answer: {}'.format(num, num*unmarked))
                break
        else:
            continue
        break


if __name__ == '__main__':
        main()
import numpy as np


def fun(p):
    arr = np.zeros((4, 4))

    for i in range(4):

        for j in range(4):

            center_right_down_i = i
            center_right_down_j = j
            center_left_down_i = i
            center_left_down_j = j

            center_straight_down = i
            center_straight_up = i
            center_straight_right = j
            center_straight_left = j

            center_right_up_i = i
            center_right_up_j = j
            center_left_up_i = i
            center_left_up_j = j
            z1 = 0
            if(i == 0 and j == 0):
                j=p

            while (center_straight_down < 4):
                if (arr[center_straight_down][j] != 0):
                    z1 = 1
                center_straight_down += 1

            while (center_straight_up >= 0):
                if (arr[center_straight_up][j] != 0):
                    z1 = 1
                center_straight_up -= 1

            while (center_straight_right < 4):
                if (arr[i][center_straight_right] != 0):
                    z1 = 1
                center_straight_right += 1

            while (center_straight_left >= 0):
                if (arr[i][center_straight_left] != 0):
                    z1 = 1
                center_straight_left -= 1

            while (center_right_down_i < 4 and center_right_down_j < 4):
                if (arr[center_right_down_i][center_right_down_j] != 0):
                    z1 = 1
                center_right_down_i += 1
                center_right_down_j += 1

            while (center_left_down_i < 4 and center_left_down_j >= 0):
                if (arr[center_left_down_i][center_left_down_j] != 0):
                    z1 = 1
                center_left_down_i += 1
                center_left_down_j -= 1

            while (center_left_up_i >= 0 and center_left_up_j >= 0):
                if (arr[center_left_up_i][center_left_up_j] != 0):
                    z1 = 1
                center_left_up_i -= 1
                center_left_up_j -= 1

            while (center_right_up_i >= 0 and center_right_up_j < 4):
                if (arr[center_right_up_i][center_right_up_j] != 0):
                    z1 = 1
                center_right_up_i -= 1
                center_right_up_j += 1

            if (z1 == 0):
                arr[i][j] = 1
    l = 0
    for a in range(4):
        for b in range(4):

            if (arr[a][b] != 0):
                l += 1
    if (l == 4):
        print(arr)
        print()

for x in range(4):
    fun(x)


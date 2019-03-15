import numpy as np
from scipy import stats


def suck_csv(file_name):
    """suck_csv
    Params:

    Return:
    """

    list = np.loadtxt(open(file_name, "rb"), dtype="string", delimiter=",", skiprows=1)

    return list.tolist()


def sort_1Dslice(slice1D, criteria):
    """sort_1Dslice
    Params:

    Return:
    """

    if criteria == "max":
        return slice1D.sort()
    elif criteria == "min":
        return slice1D.sort(reverse=True)
    else:
        # TODO return error in order to handle it.
        print("a is greater than b")


def median_1Dslice(slice1D):
    """median_1Dslice
    Params:

    Return:
    """
    np_median = np.median(slice1D)
    median = np_median.item()
    return median


# Reference: https://stackoverflow.com/questions/16330831/
# most-efficient-way-to-find-mode-in-numpy-array
def mode_1Dslice(slice1D):
    a = np.array(slice1D)
    np_m = stats.mode(a)
    m = np_m[0].item()
    return m


# test_slice [5] int = [4,3,1,7,0]
# double ans = avg(test_slice) # will spit => 3
def avg(slice1D):
    """avg
    Params:

    Return:
    """
    np_avg = np.average(slice1D)
    avg = np_avg.tolist()

    return avg


def multiply_1Dslice(list, num):
    """avg
    Params:

    Return:
    """
    np_arr = np.array(list) * num
    a = np_arr.tolist()
    return a


def find_min(slice1D, min):
    """find_min
    Params:

    Return:
    """
    np_arr = np.array(slice1D)
    find = np.where(np_arr > min)
    return find[0]


def find_max(slice1D, max):
    """find_max
    Params:

    Return:
    """
    np_arr = np.array(slice1D)
    find = np.where(np_arr < max)
    return find[0]


def zeros(num_of_zeros):
    np_arr = np.zeros(num_of_zeros)
    arr = np_arr.tolist()
    return arr


def randoms(num_of_randoms, max):
    np.random.seed(0)  # seed for reproducibility
    np_arr = np.random.randint(max, size=num_of_randoms)  # One-dimensional array
    arr = np_arr.tolist()
    return arr


if __name__ == "__main__":

    """
    suck_csv
    """
    print("\nsuck_csv".upper())
    file_name = "cars.csv"
    a = suck_csv(file_name)
    print(type(a))
    print(a)

    """
    to_table
    will create table to html_table (TODO)
    """
    # print("\nto_table".upper())
    #
    # for value in a:
    #     for index in slice:
    #         print index

    """
    sort_slice
    """
    print("\nsort_slice".upper())
    test_slice = [4, 3, 1, 7, 0]
    print("unsorted_slice")
    print(test_slice)
    print("sorted_slice (max)")
    sort_1Dslice(test_slice, "max")
    print(test_slice)
    print("sorted_slice (min)")
    sort_1Dslice(test_slice, "min")
    print(test_slice)

    """
    median
    """
    print("\nmedian".upper())
    slice1D = [20, 2, -1, 1, 34]
    print("slice1D : ", slice1D)
    median = median_1Dslice(slice1D)
    print("median of slice1D: {}".format(median))

    """
    mode
    """
    print("\nmode".upper())
    slice1D = [5, 2, 2, 1, 1, 4, 1, 4, 4]
    print("slice1D : {}".format(slice1D))
    mode = mode_1Dslice(slice1D)
    print("Mode: {}".format(mode))

    """
    AVG
    test_slice [5] int = [4,3,1,7,0]
    double ans = avg(test_slice) # will spit => 3
    """

    print("\navg".upper())
    slice1D = [4, 3, 1, 7, 0]
    avg = avg(slice1D)
    print("Average: {}".format(avg))

    """
    POW
    pow(2,3) # will spit => 8
    """
    print("\npow".upper())
    a = 2
    b = 3
    ans = pow(a, b)
    print(ans)

    """
    Multiplies each element of a slice by a factor
    """
    print("\nMultiply slice".upper())
    slice = [1, 2, 3]
    factor = 2
    print("Slice {}".format(slice))
    slice = multiply_1Dslice(slice, factor)
    print("Slice multiplied by {}: {}".format(factor, slice))
    print(slice)

    """
    find_min
    returns the indexes
    """
    print("\nfind_min".upper())
    slice = [10, 20, 30, 40, 50, 60, 70, 80]
    print("Slice {}".format(slice))

    filter_num = 40

    slice_max_5 = find_max(slice, filter_num)
    print("Slice max {}".format(slice_max_5))

    slice_min_5 = find_min(slice, filter_num)
    print("Slice min {}".format(slice_min_5))
    """
    zeros
    """
    print("\nzeros".upper())
    slice = zeros(10)
    print(slice)
    """
    randoms
    """
    print("\nrandoms".upper())
    slice = randoms(10, 100)
    print(slice)

import numpy as np
from scipy import stats


def suck_csv(file_name):

    list = np.loadtxt(open(file_name, "rb"), dtype="string", delimiter=",", skiprows=1)

    return list.tolist()


def sort_1Dslice(slice1D, criteria):
    if criteria == "max":
        return slice1D.sort()
    elif criteria == "min":
        return slice1D.sort(reverse=True)
    else:
        # TODO return error in order to handle it.
        print("a is greater than b")


def median_1Dslice(slice1D):
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
    np_avg = np.average(slice1D)
    avg = np_avg.tolist()

    return type(avg)

def multiply_1Dslice(list, num):
    np_arr = np.array(list) * num
    a = np_arr.tolist()
    return a


def find_min(slice1D, min):
    np_arr = np.array(slice1D)
    find = np.where(np_arr > min)
    return find[0]


def find_max(slice1D, max):
    np_arr = np.array(slice1D)
    find = np.where(np_arr < max)
    return find[0]


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
    print("\nsort_slice".upper())
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
    slice1D = [4,3,1,7,0]
    avg = avg(slice1D)
    print("Average: {}".format(avg))


    """
    POW
    pow(2,3) # will spit => 8
    """
    print("\npow".upper())
    a = 2
    b = 3
    ans = pow(a,b)
    print(ans)


    # # slice = multiply_1Dslice([1,2,3], 2)
    # # print(slice)
    #
    # a_slice1D = [1, 2, 3, 4, 5, 6, 7, 9, 8]
    #
    # numbers = [1, 3, 4, 2]
    #
    # # Sorting list of Integers in ascending
    # # numbers.sort()
    # #
    # # print(numbers)
    #
    # sorted_slice1D = sort_1Dslice(a_slice1D)
    # print(a_slice1D)
    #
    # b_slice1D = find_max(sorted_slice1D, 5)
    # c_slice1D = find_min(sorted_slice1D, 5)
    #
    # print(sorted_slice1D)
    # print(b_slice1D)
    # print(c_slice1D)

    # aux = np.array(a)
    #
    #
    # dtype = [('brand', 'S10'), ('name', 'S10'), ('model', 'S10')]
    #
    # aux = np.array(aux, dtype=dtype)       # create a structured array
    # np.sort(aux, order='brand')
    # print("\n")
    # print(type(aux))
    # print(aux)
    # dtype = [('name', 'S10'), ('height', float), ('age', int)]
    # dtype2 = [['name', 'S10'], ['height', float], ['age', int]]
    # print(type(dtype))
    # print(type(dtype2))
    # values = [('ArthurArthur', 1.8, 41), ('Lancelot', 1.9, 38),('Galahad', 1.7, 38)]
    # a = np.array(values, dtype=dtype)       # create a structured array
    # result = np.sort(a, order='height')
    # print(result)

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

import random
unique_arr = []
arr_two = []

class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        lst = []
        return lst

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        global unique_arr
        for i in range(20):
            unique_arr.append(random.randint(0, 100))
        unique_arr = list(set(unique_arr))
        return list(unique_arr)
        # complete this function


    @staticmethod
    def get_expected_result():
        global unique_arr
        return unique_arr.index(min(unique_arr))
        # complete this function

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        # complete this function
        global arr_two
        for i in range(20):
            arr_two.append(random.randint(0, 100))
        arr_two.append(min(arr_two))
        return arr_two


    @staticmethod
    def get_expected_result():
        # complete this function
        global arr_two
        return arr_two.index(min(arr_two))


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")

import random
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime, timedelta

MIN_ARRAY_LENGTH = 30
MAX_ARRAY_LENGTH = 100
NUMBER_OF_POINTS = 10
ARRAY_LENGTH_STEP = (MAX_ARRAY_LENGTH - MIN_ARRAY_LENGTH) // NUMBER_OF_POINTS
COUNT_OF_PASSES = 10
MIN_VALUE = 1
MAX_VALUE = MAX_ARRAY_LENGTH
PLOT_2D = True
PLOT_3D = True
MODE = 'log'


def array_mean(array):
    return [array[i].mean() for i in range(len(array))]


def array_std(array):
    return [array[i].std() for i in range(len(array))]


def polyfit(x, y, order, evaluation):
    return np.poly1d(np.polyfit(x, y, order))(evaluation)


def main():
    # 1D
    native_times_1d = np.zeros((NUMBER_OF_POINTS, COUNT_OF_PASSES))
    numpy_times_1d = np.zeros((NUMBER_OF_POINTS, COUNT_OF_PASSES))

    for array_length_index in range(NUMBER_OF_POINTS):
        for pass_index in range(COUNT_OF_PASSES):
            # Obtain random data for array and list
            length = array_length_index * ARRAY_LENGTH_STEP + MIN_ARRAY_LENGTH
            test_list_1 = random.sample(range(MIN_VALUE, MAX_VALUE), length)
            test_list_2 = random.sample(range(MIN_VALUE, MAX_VALUE), length)

            test_numpy_array_1 = np.random.rand(length) * (MAX_VALUE - MIN_VALUE) + MIN_VALUE
            test_numpy_array_2 = np.random.rand(length) * (MAX_VALUE - MIN_VALUE) + MIN_VALUE

            # Multiply lists and arrays and measure timing
            time_1 = datetime.now()
            test_list = [test_list_1[i] * test_list_2[i] for i in range(length)]
            time_2 = datetime.now()
            result_numpy_array = test_numpy_array_1 * test_numpy_array_2
            time_3 = datetime.now()

            native_times_1d[array_length_index, pass_index] = (time_2 - time_1) / timedelta(microseconds=1)
            numpy_times_1d[array_length_index, pass_index] = (time_3 - time_2) / timedelta(microseconds=1)

    # 2D
    native_times_2d = np.zeros((NUMBER_OF_POINTS, COUNT_OF_PASSES))
    numpy_times_2d = np.zeros((NUMBER_OF_POINTS, COUNT_OF_PASSES))

    for array_length_index in range(NUMBER_OF_POINTS):
        for pass_index in range(COUNT_OF_PASSES):
            # Obtain random data for array and list
            length = array_length_index * ARRAY_LENGTH_STEP + MIN_ARRAY_LENGTH
            test_list_1 = [random.sample(range(MIN_VALUE, MAX_VALUE), length) for i in range(length)]
            test_list_2 = [random.sample(range(MIN_VALUE, MAX_VALUE), length) for i in range(length)]

            test_numpy_array_1 = np.random.rand(length, length) * (MAX_VALUE - MIN_VALUE) + MIN_VALUE
            test_numpy_array_2 = np.random.rand(length, length) * (MAX_VALUE - MIN_VALUE) + MIN_VALUE

            # Multiply lists and arrays and measure timing
            time_1 = datetime.now()
            test_list = [[test_list_1[i][j] * test_list_2[i][j] for j in range(length)] for i in range(length)]
            time_2 = datetime.now()
            result_numpy_array = test_numpy_array_1 * test_numpy_array_2
            time_3 = datetime.now()

            native_times_2d[array_length_index, pass_index] = (time_2 - time_1) / timedelta(microseconds=1)
            numpy_times_2d[array_length_index, pass_index] = (time_3 - time_2) / timedelta(microseconds=1)

    # 3D
    native_times_3d = np.zeros((NUMBER_OF_POINTS, COUNT_OF_PASSES))
    numpy_times_3d = np.zeros((NUMBER_OF_POINTS, COUNT_OF_PASSES))

    for array_length_index in range(NUMBER_OF_POINTS):
        for pass_index in range(COUNT_OF_PASSES):
            # Obtain random data for array and list
            length = array_length_index * ARRAY_LENGTH_STEP + MIN_ARRAY_LENGTH
            test_list_1 = [[random.sample(range(MIN_VALUE, MAX_VALUE), length) for i in range(length)] for i in
                           range(length)]
            test_list_2 = [[random.sample(range(MIN_VALUE, MAX_VALUE), length) for i in range(length)] for i in
                           range(length)]

            test_numpy_array_1 = np.random.rand(length, length, length) * (MAX_VALUE - MIN_VALUE) + MIN_VALUE
            test_numpy_array_2 = np.random.rand(length, length, length) * (MAX_VALUE - MIN_VALUE) + MIN_VALUE

            # Multiply lists and arrays and measure timing
            time_1 = datetime.now()
            test_list = [[[test_list_1[i][j][k] * test_list_2[i][j][k] for k in range(length)] for j in range(length)]
                         for i in range(length)]
            time_2 = datetime.now()
            result_numpy_array = test_numpy_array_1 * test_numpy_array_2
            time_3 = datetime.now()

            native_times_3d[array_length_index, pass_index] = (time_2 - time_1) / timedelta(microseconds=1)
            numpy_times_3d[array_length_index, pass_index] = (time_3 - time_2) / timedelta(microseconds=1)

    # Plot results

    figure, (axis1, axis2) = plt.subplots(2)
    axis1.set_title('Native lists performance')
    axis2.set_title('Numpy arrays performance')

    lengths = range(MIN_ARRAY_LENGTH, MAX_ARRAY_LENGTH, ARRAY_LENGTH_STEP)
    lengths_polyfit = range(MIN_ARRAY_LENGTH, MAX_ARRAY_LENGTH - ARRAY_LENGTH_STEP)

    axis1.errorbar(lengths, array_mean(native_times_1d), yerr=array_std(native_times_1d), label='1 Dimension',
                   color='red')
    axis1.plot(lengths_polyfit, polyfit(lengths, array_mean(native_times_1d), 1, lengths_polyfit), color='black')
    axis2.errorbar(lengths, array_mean(numpy_times_1d), yerr=array_std(numpy_times_1d), label='1 Dimension',
                   color='red')
    axis2.plot(lengths_polyfit, polyfit(lengths, array_mean(numpy_times_1d), 1, lengths_polyfit), color='black')

    if PLOT_2D:
        axis1.errorbar(lengths, array_mean(native_times_2d), yerr=array_std(native_times_2d), label='2 Dimension',
                       color='green')
        axis1.plot(lengths_polyfit, polyfit(lengths, array_mean(native_times_2d), 2, lengths_polyfit), color='indigo')
        axis2.errorbar(lengths, array_mean(numpy_times_2d), yerr=array_std(numpy_times_2d), label='2 Dimension',
                       color='green')
        axis2.plot(lengths_polyfit, polyfit(lengths, array_mean(numpy_times_2d), 2, lengths_polyfit), color='indigo')

    if PLOT_3D:
        axis1.errorbar(lengths, array_mean(native_times_3d), yerr=array_std(native_times_3d), label='3 Dimension',
                       color='blue')
        axis1.plot(lengths_polyfit, polyfit(lengths, array_mean(native_times_3d), 3, lengths_polyfit), color='salmon')
        axis2.errorbar(lengths, array_mean(numpy_times_3d), yerr=array_std(numpy_times_3d), label='3 Dimension',
                       color='blue')
        axis2.plot(lengths_polyfit, polyfit(lengths, array_mean(numpy_times_3d), 3, lengths_polyfit), color='salmon')

    axis1.legend(loc='upper left')
    axis2.legend(loc='upper left')

    axis1.set(xlabel='Size', ylabel='Time, Microseconds')
    axis2.set(xlabel='Size', ylabel='Time, Microseconds')

    axis1.set_yscale(MODE)
    axis2.set_yscale(MODE)

    figure.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()

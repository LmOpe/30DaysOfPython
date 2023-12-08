from classes_and_objects import Statistics

if __name__ == "__main__":
    ages = [31, 26, 34, 37, 27, 26, 32, 32, 26,\
         27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31,\
             34, 24, 33, 29, 26]

    data = Statistics(ages)

    print('Count:', data.count())
    print('Sum: ', data.sum_stats())
    print('Min: ', data.min_stats())
    print('Max: ', data.max_())
    print('Range: ', data.range_stats())
    print('Mean: ', data.mean())
    print('Median: ', data.median())
    print('Mode: ', data.mode())
    print('Standard Deviation: ', data.std())
    print('Variance: ', data.variance())
    print('Percentile: ', data.percentile(75))
    print('Frequency Distribution: ', data.freq_dist())
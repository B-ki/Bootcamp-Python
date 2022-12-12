from Tinystatistician import mean, median, quartile, var, std, percentile

a = [1, 42, 300, 10, 59]
print(mean(a))
print(median(a))
print(median([6, 5, 9, 4, 2]))
print(quartile(a))
print(quartile([1, 11, 15, 19, 20, 24, 28, 34, 37, 47, 50, 61, 68]))
print(quartile([1, 11, 15, 19, 20, 24, 28, 34, 37, 47, 50, 61]))
print(var(a))
print(std(a))
print(percentile(a, 10))
print(percentile(a, 15))

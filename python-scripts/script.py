import numpy
import scipy.stats as stats
import scipy
import matplotlib.pyplot as pyplot

thing = [0, 8, 16]#, 24, 32, 40, 48, 56, 64, 72, 80, 88]
x_vals = numpy.array(thing);

arr = numpy.genfromtxt("lambda-h.csv", delimiter=",")
print(arr)
# 0=min, 1=max
err = (numpy.ndarray(len(arr)), numpy.ndarray(len(arr)))
mean = numpy.ndarray(len(arr))
for i in range(len(arr)):
    mean[i] = numpy.mean(arr[i])
    err[0][i], err[1][i] = stats.t.interval(0.95, df=len(arr[i])-1, loc=mean[i], scale=stats.sem(arr[i]))

print(f"error: {err}\nmean: {mean}")

figure, subplots = pyplot.subplots()
subplots.plot(x_vals, mean)
pyplot.title(r"Emission Wavelengths w/95% confidence interval")
pyplot.xlabel("Galactic Longitude")
pyplot.ylabel("Peak Wavelength of Most Redshifted Emission (nm)")
subplots.fill_between(x_vals, err[0], err[1], color="b", alpha=.1)

for index, val in enumerate(x_vals):
    x_arr = numpy.ndarray(len(arr[index]))
    x_arr.fill(val)
    pyplot.scatter(x_arr, arr[index])
figure.savefig('graph-err-bars.png')
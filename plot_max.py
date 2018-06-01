from matplotlib import pyplot
import numpy

x = numpy.linspace(-1, 1, 1000)
y1 = numpy.exp(-x**2 * 10) * (1 + 0.05 * numpy.random.rand(len(x)))
y2 = (numpy.exp(10*(-(x-0.3)**2 - 0.75*x**4 - 0.25*x**6)) + numpy.piecewise(x, [x < 0.3, x >= 0.3], [lambda x: -(x-0.3)*numpy.sqrt(1+x), 0])) * (1 + 0.05 * numpy.random.rand(len(x)))

def plot_max(x, y):
    x_c = numpy.argmax(y) / len(x)
    ax_lim = (x_c - 0.1, 0.2, 0.2, 0.2)
    f = pyplot.plot(x, y)
    pyplot.xlim(-1, 1)
    pyplot.arrow(2 * x_c - 1, 0.4, 0, 0.5, head_width=0.025, head_length=0.05)
    ax = pyplot.axes(ax_lim)
    ax.plot(x, y)
    ax.set_xlim(2 * (x_c - 0.56), 2 * (x_c - 0.44))
    ax.set_ylim(0.9, 1.1)
    return f

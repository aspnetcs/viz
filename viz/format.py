from . import stats
from . import terminal
from .text import format_float


def quantiles(xs, qs=None, step=25, width=None, cellspacing=3):
    """
    Use stats.quantiles to get quantile-value pairs, and then print them to fit.
    >>> import numpy as np
    >>> quantiles(np.random.normal(size=10000), qs=[0, 5, 50, 95, 100])
     0% < -3.670    5% < -1.675   50% < -0.002   95% < 1.6500   100% < 3.4697
    (Or something like that)
    """

    if width is None:
        width = terminal.width()

    qs_values = stats.quantiles(xs, qs=qs, step=step)

    ncells = len(qs_values)
    cellspacing_total = (ncells - 1) * cellspacing
    cell_width = int((width - cellspacing_total) / ncells)
    max_width = cell_width - 6

    cells = (f"{q:2d}% < {format_float(value, max_width)}" for q, value in qs_values)
    print(*cells, sep=" " * cellspacing)

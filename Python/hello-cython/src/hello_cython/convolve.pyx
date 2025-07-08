import cython
import numpy as np

@cython.boundscheck(False)
@cython.wraparound(False)
def naive_convolve(f, g):
    """
    Pure Python Cython version. Arguments:
    f: numpy.ndarray
    g: numpy.ndarray
    Returns: numpy.ndarray
    """
    if g.shape[0] % 2 != 1 or g.shape[1] % 2 != 1:
        raise ValueError("Only odd dimensions on filter supported")
    vmax: cython.int = f.shape[0]
    wmax: cython.int = f.shape[1]
    smax: cython.int = g.shape[0]
    tmax: cython.int = g.shape[1]
    smid: cython.int = smax // 2
    tmid: cython.int = tmax // 2
    xmax: cython.int = vmax + 2 * smid
    ymax: cython.int = wmax + 2 * tmid
    h = np.zeros([xmax, ymax], dtype=f.dtype)
    x: cython.int
    y: cython.int
    s: cython.int
    t: cython.int
    for x in range(xmax):
        for y in range(ymax):
            s_from: cython.int = max(smid - x, -smid)
            s_to: cython.int = min((xmax - x) - smid, smid + 1)
            t_from: cython.int = max(tmid - y, -tmid)
            t_to: cython.int = min((ymax - y) - tmid, tmid + 1)
            value: cython.double = 0
            for s in range(s_from, s_to):
                for t in range(t_from, t_to):
                    v: cython.int = x - smid + s
                    w: cython.int = y - tmid + t
                    if 0 <= v < vmax and 0 <= w < wmax:
                        value += f[v, w] * g[smid - s, tmid - t]
            h[x, y] = value
    return h


from typing import Tuple
from collections import namedtuple
import numpy as np

Line = namedtuple("Line", ["from_", "to"])

def line_to_line(a: Line, b: Line) -> Tuple[float, float]:
    A = np.vstack([a.to - a.from_, b.from_ - b.to])
    A = A.T
    b = b.from_ - a.from_
    try:
        t = np.linalg.solve(A, b)
        return (t[0], t[1])
    except np.linalg.LinAlgError:
        return None

def ray_to_segment(a: Line, b: Line) -> Tuple[float, np.array]:
    t = line_to_line(a, b)
    if t is None:
        return None

    t0, t1 = t
    if t1>1.0 or t1<0.0 or t0<0.0:
        return None

    point = a.from_ + (a.to - a.from_)*t0
    dist = np.linalg.norm(point - a.from_)
    return dist, point

def segment_to_segment(a: Line, b: Line) -> np.array:
    t = line_to_line(a, b)
    if t is None:
        return None

    t0, t1 = t
    if t1>1.0 or t1<0.0 or t0<0.0 or t0>1.0:
        return None

    point = a.from_ + (a.to - a.from_)*t0
    return point



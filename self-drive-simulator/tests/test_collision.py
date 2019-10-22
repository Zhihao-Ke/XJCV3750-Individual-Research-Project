from pytest import approx
import numpy as np
from avsim.collision import *

point_a = np.array([0.0,1.0])
point_b = np.array([1.0,1.0])
point_c = np.array([0.0,0.0])
point_d = np.array([1.0,0.0])
point_e = np.array([0.5,0.5])
point_f = np.array([0.2, 0.3])

def test_line_line_1():
    a = Line(point_a, point_b)
    b = Line(point_c, point_e)
    t = line_to_line(a, b)
    assert t == (approx(1.0), approx(2.0))

def test_line_line_2():
    a = Line(point_a, point_b)
    b = Line(point_d, point_e)
    t = line_to_line(a, b)
    assert t == (approx(0.0), approx(2.0))

def test_line_line_3():
    a = Line(point_a, point_b)
    b = Line(point_e, point_d)
    t = line_to_line(a, b)
    assert t == (approx(0.0), approx(-1.0))

def test_line_line_4():
    a = Line(point_a, point_b)
    b = Line(point_c, point_d)
    t = line_to_line(a, b)
    assert t == None

def test_ray_segment_1():
    a = Line(point_a, point_b)
    b = Line(point_c, point_f)
    dist, p = ray_to_segment(b, a)
    assert dist == approx(1.20185, 0.0001)
    assert (p[0], p[1]) == (approx(0.666666, 0.0001), approx(1))

def test_ray_segment_2():
    a = Line(point_a, point_b)
    b = Line(point_c, point_d)
    assert ray_to_segment(a, b) is None

def test_ray_segment_3():
    a = Line(point_c, point_f)
    b = Line(point_f, point_c)
    c = Line(point_a, point_d)
    assert ray_to_segment(a, c) is not None
    assert ray_to_segment(b, c) is None
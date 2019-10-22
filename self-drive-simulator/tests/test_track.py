
from pytest import approx
import numpy as np
from avsim.track import RacingTrack
from avsim.collision import Line

a = np.array([0.0,0.0])
b = np.array([1.0,0.5])
c = np.array([0.5,-1.0])
d = np.array([-1.0,-0.5])
e = np.array([-0.5,-1.0])

def test_ray_trace():
    track = RacingTrack(None)
    track.build_test_track()
    assert track.raytrace(Line(a, b))[0] == approx(111.8, 0.1)
    assert track.raytrace(Line(a, c))[0] == approx(111.8, 0.1)
    assert track.raytrace(Line(a, d))[0] == approx(111.8, 0.1)
    assert track.raytrace(Line(a, e))[0] == approx(111.8, 0.1)

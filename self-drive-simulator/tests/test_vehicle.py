import numpy as np
from pytest import approx
from avsim.vehicle import Vehicle
from avsim.track import RacingTrack

def test_vehicle_strait_x():
    veh = Vehicle()
    veh.v = 1.0

    for i in range(100):
        veh.update(0.02)

    assert veh.x == approx(2.0)

def test_vehicle_left_turn():
    veh = Vehicle()
    veh.v = 1.0
    veh.theta = 0.2

    for i in range(100):
        veh.update(0.02)

    assert veh.x == approx(1.96, 0.01)
    assert veh.y > 0.0

def test_vehicle_right_turn():
    veh = Vehicle()
    veh.v = 1.0
    veh.theta = -0.2

    for i in range(100):
        veh.update(0.02)

    assert veh.x == approx(1.96, 0.01)
    assert veh.y < 0.0

def test_vehicle_sense():
    veh = Vehicle()
    track = RacingTrack(None)
    track.build_test_track()
    del track.segments[2]
    veh.detect(track)
    assert veh.detector_distances == [approx(115.4, 0.1), np.inf, np.inf, np.inf,
                            np.inf, np.inf, approx(115.4, 0.1)]
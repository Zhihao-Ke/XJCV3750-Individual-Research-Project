import numpy as np
from typing import Tuple
from avsim.collision import Line, ray_to_segment

class RacingTrack:
    def __init__(self, filename):
        self.load(filename)

    def load(self, filename):
        self.segments = []

    def build_test_track(self):
        self.segments = [
            Line(np.array([-100.0, -100.0]), np.array([100.0, -100.0])),
            Line(np.array([-100.0, 100.0]), np.array([100.0, 100.0])),
            Line(np.array([100.0, 100.0]), np.array([100.0, -100.0])),
            Line(np.array([-100.0, 100.0]), np.array([-100.0, -100.0]))
        ]

    def raytrace(self, ray: Line) -> Tuple[float, np.array]:
        dist = np.inf
        point = None

        for segment in self.segments:
            r = ray_to_segment(ray, segment)
            if r is None:
                continue
            d, p = r
            if d < dist:
                dist = d
                point = p
        
        return dist, point

    def collide(self, vehicle) -> bool:
        pass


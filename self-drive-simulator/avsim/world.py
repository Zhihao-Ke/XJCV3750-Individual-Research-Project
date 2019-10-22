import numpy as np
from typing import List
from avsim.track import RacingTrack
from avsim.vehicle import Vehicle
from avsim.collision import Line

class World:
    def __init__(self, filename):
        self.track = RacingTrack(filename)
        self.vehicle_alive = []
        self.vehicle_dead = []

    def add_vehicle(self, vehicle):
        pass

    def update(self, dt):
        pass

    def get_center(self) -> float:
        pass

    def get_direction(self) -> float:
        pass

    def get_vehicles(self, scale) -> List[Vehicle]:
        return self.vehicle_alive

    def get_segments(self, scale) -> List[Line]:
        return self.track.segments

class TestWorld(World):
    def __init__(self):
        super().__init__(None)
        self.track.build_test_track()
        self.vehicle_alive.append(Vehicle(np.pi*0.333, 20, 20))
        self.vehicle_alive[0].detect(self.track)

    def get_center(self) -> float:
        return (-20, -20)

    def get_direction(self) -> float:
        return -60

test_world = TestWorld()
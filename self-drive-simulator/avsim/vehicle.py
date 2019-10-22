import numpy as np
from PySide2.QtCore import QRectF
from avsim.track import RacingTrack
from avsim.collision import Line

class Vehicle:
    def __init__(self, theta=0.0, x=0.0, y=0.0):
        # kinematic state
        self.x = x
        self.y = y # position of center of gravity
        self.theta = theta # head direction

        # control parameters
        self.v = 0.0 # linear speed
        self.acc = 0.0 # linear acceleration
        self.delta = 0.0 # stearing angle
        self.phi = 0.0 # change rate of stearing angle

        # geomery shape of car
        self.lf = 2.0 # length of front axel
        self.lr = 2.0 # length of real axel

        # laser detetors
        self.detector_angles = [ang/180.0*np.pi for ang in [60, 40, 20, 0, -20, -40, 60]]
        self.detector_distances = [np.inf]*len(self.detector_angles)
        self.detector_points = [None]*len(self.detector_angles)

    def get_rotate(self):
        return self.theta / np.pi * 180.0

    def get_position(self):
        return self.x, self.y

    def get_bbox(self):
        bbox = QRectF(-self.lr, -1, self.lr+self.lf, 2).adjusted(-0.5, 0, 0.5, 0)
        return bbox

    def detect(self, track: RacingTrack):
        self.detector_distances = []
        self.detector_points = []

        for ang_car in self.detector_angles:
            ang_world = self.theta + ang_car
            ray = Line(
                np.array([self.x, self.y]),
                np.array([self.x+np.cos(ang_world), self.y+np.sin(ang_world)])
            )
            dist, point = track.raytrace(ray)
            self.detector_distances.append(dist)
            self.detector_points.append(point)
    
    def stear(self, acc, phi):
        self.acc = acc
        self.phi = phi

    def update(self, dt):
        if abs(self.delta) < 0.00001:
            r = np.inf
            beta = 0.0
        else:
            r = (self.lr+self.lf)/np.tan(self.delta)
            beta = np.arctan(self.lr / r)
        
        v_cg = self.v / np.cos(beta)
        self.x += np.cos(self.theta+beta)*v_cg*dt
        self.y += np.sin(self.theta+beta)*v_cg*dt

        self.theta += np.arctan(self.v*dt/r)

        self.v += self.acc*dt
        self.delta += self.phi*dt

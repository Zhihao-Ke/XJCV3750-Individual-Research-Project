import numpy as np
from PySide2 import QtGui, QtWidgets, QtCore
from avsim.world import World

class SimView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.world = None

    def paintEvent(self, event):
        if self.world:
            painter = QtGui.QPainter()
            painter.begin(self)
            # initialize painter state
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.scale(1, -1)
            painter.translate(self.width()/2.0, -self.height()/2.0)
            painter.scale(3, 3)
            painter.drawLine(-100, 0, 200, 0)
            painter.drawLine(0, -100, 0, 200)

            self.paint_world(painter, self.world)
            
            #painter.drawText(200, 200, "aaaa")
            #painter.save()
            #painter.rotate(30)
            #painter.setPen(QtGui.QColor(255,100,100))
            #painter.drawRect(-10, -10, 30, 30)
            #painter.restore()
            #painter.rotate(90)
            #painter.setPen(QtGui.QColor(100,255,100))
            #painter.drawRect(-10, -10, 30, 30)
            painter.end()

        super().paintEvent(event)

    def paint_world(self, painter: QtGui.QPainter, world: World):
        painter.rotate(world.get_direction())
        painter.translate(*world.get_center())
        painter.drawLine(-100, 0, 200, 0)
        painter.drawLine(0, -100, 0, 200)

        # paint road
        painter.setPen(QtGui.QColor(0,0,0))
        for seg in world.get_segments(None):
            x1, y1 = seg.from_
            x2, y2 = seg.to
            painter.drawLine(x1, y1, x2, y2)

        # paint car
        painter.setPen(QtGui.QColor(100,100,200))
        for veh in world.get_vehicles(None):
            painter.save()
            painter.translate(*veh.get_position())
            painter.rotate(veh.get_rotate())
            painter.drawRect(veh.get_bbox())

            # draw detector rays
            angles = [rad/np.pi*180.0 for rad in veh.detector_angles]
            dists = veh.detector_distances

            for angle, dist in zip(angles, dists):
                painter.save()
                painter.rotate(angle)
                if dist is np.inf:
                    painter.drawLine(0.0, 0.0, 1000.0, 0.0)
                else:
                    painter.drawLine(0.0, 0.0, dist, 0.0)
                    painter.drawEllipse(QtCore.QPointF(dist, 0.0), 5.0, 5.0)
                painter.restore()

            painter.restore()



if __name__ == "__main__":
    import sys
    from avsim.world import test_world

    app = QtWidgets.QApplication(sys.argv)
    view = SimView()
    view.world = test_world
    view.show()
    sys.exit(app.exec_())
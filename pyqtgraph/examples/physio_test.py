import pyqtgraph as pg
import numpy as np
from pyqtgraph.Qt import QtGui, QtWidgets


# Initialize the Qt Application
# app = QtGui.QGuiApplication([])

lines = 3
Lx = 34
xs_short = np.arange(Lx)
h_fill = np.zeros(lines)
ys_short = np.zeros((lines,Lx))
for i in np.arange(lines):
    ys_short[i,:] = np.sin(xs_short) + i*1
    h_fill[i] = i*1.0

win1 = pg.plot()

pen = pg.mkPen(color=(255, 0, 0))
pen1 = pg.mkPen('b', width=5)
win1.addLegend()
win1.plot(xs_short, ys_short, pen=['r','g','b','r'])
# win1.plot(xs_short, ys_short,fillLevel=h_fill,brush=(255, 0, 0),fillOutline=False)
# win1.plot(xs_short, ys_short,fillLevel=h_fill,brush=(255, 0, 0),fillOutline=True)
# win1.plot(xs_short, ys_short[0,:],fillLevel=h_fill[0],brush=(255, 0, 0))
# win1.plot(xs_short, ys_short)
# p = win1.plot(xs_short, ys_short, pen=pen, symbol='+',)
# p = win1.plot(xs_short, ys_short, pen=pen, symbol='+',fillLevel=h_fill,brush=(255, 0, 0),fillOutline=False)
# p = win1.plot(xs_short, ys_short[0,:], pen = pen, symbol ='o', symbolPen ='b', symbolBrush = 0.2, name ='blue')
# p = win1.plot(xs_short, ys_short, pen = pen, symbol ='o', symbolPen ='b', symbolBrush = 0.2, name ='blue')
# p.setShadowPen(pen1)

# fillopts = dict(pen=pen, fillLevel=0, fillOutline=True, brush='b')
# win1.plot(xs_short, ys_short[0,:], **fillopts)
# fillopts = dict(pen=pen, fillLevel=h_fill, fillOutline=True, brush='b')
# win1.plot(xs_short, ys_short, **fillopts)

# Start the Qt application loop
QtGui.QGuiApplication.instance().exec()

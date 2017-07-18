# EAN Planner Tool application
# used for easy routing of autonomous robot paths
# Copyright (c) 2016 Aedan Cullen


from PyQt4 import QtGui, QtCore
from pyqtgraph import opengl
from plannerUi import Ui_plannerTool

class PlannerTool(QtGui.QWidget, Ui_plannerTool):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)
		grid = opengl.GLGridItem()
		self.pathGraphics.addItem(grid)
		axis = opengl.GLAxisItem()
		axis.setSize(10,10,10)
		axis.translate(0,0,0.1)
		self.pathGraphics.addItem(axis)



if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	planner = PlannerTool()
	planner.showMaximized()
	sys.exit(app.exec_())
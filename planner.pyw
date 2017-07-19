# EAN Planner Tool application
# used for easy routing of autonomous robot paths
# Copyright (c) 2016 Aedan Cullen


from PyQt4 import QtGui, QtCore
from pyqtgraph import opengl
from plannerUi import Ui_plannerTool

import numpy
from stl import mesh

class PlannerTool(QtGui.QMainWindow, Ui_plannerTool):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)
		grid = opengl.GLGridItem()
		self.pathGraphics.addItem(grid)
		axis = opengl.GLAxisItem()
		axis.setSize(10,10,10)
		axis.translate(0,0,0.1)
		self.pathGraphics.addItem(axis)

		#field = mesh.Mesh.from_file('field.stl')
		#data = field.points
		#data = data.reshape(-1, 3, 3)
		#md = opengl.MeshData(vertexes = data)

		#fieldModel = opengl.GLMeshItem(meshdata = md, shader='shaded', glOptions='opaque')
		#self.pathGraphics.addItem(fieldModel)



if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	planner = PlannerTool()
	planner.showMaximized()
	sys.exit(app.exec_())
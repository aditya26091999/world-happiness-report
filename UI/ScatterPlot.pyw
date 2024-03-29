# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScatterPlot.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import UI.DataFrames as d

class Ui_Relation(object):

    def plot_scatterplot(self):
        buttons = ['EC', 'FA', 'HE', 'FR', 'TR', 'GN']

        features1 = [self.EC.isChecked(), self.FA.isChecked(), self.HE.isChecked(), self.FR.isChecked(),
                     self.TR.isChecked(), self.GN.isChecked()]

        features2 = [self.EC2.isChecked(), self.FA2.isChecked(), self.HE2.isChecked(), self.FR2.isChecked(),
                     self.TR2.isChecked(), self.GN2.isChecked()]

        which = []

        for i in range(len(features1)):
                if features1[i]:
                        which.append(buttons[i])

        for i in range(len(features2)):
                if features2[i]:
                        which.append(buttons[i])

        if self.y2015.isChecked():
                fig, axs = d.plt.subplots(1,1)
                fig.canvas.set_window_title('2015 %s vs %s'%(which[0],which[1]))
                d.plt.scatter(d.var_2015[which[0]], d.var_2015[which[1]])
                d.plt.xlabel("%s" % which[0])
                d.plt.ylabel("%s" % which[1])
                d.plt.title("%s VS %s" % (which[0], which[1]))
                d.plt.show()

        elif self.y2016.isChecked():
                fig, axs = d.plt.subplots(1, 1)
                fig.canvas.set_window_title('2016 %s vs %s' % (which[0], which[1]))
                d.plt.scatter(d.var_2016[which[0]], d.var_2016[which[1]])
                d.plt.xlabel("%s" % which[0])
                d.plt.ylabel("%s" % which[1])
                d.plt.title("%s VS %s" % (which[0], which[1]))
                d.plt.show()
        elif self.y2017.isChecked():
                fig, axs = d.plt.subplots(1, 1)
                fig.canvas.set_window_title('2017 %s vs %s' % (which[0], which[1]))
                d.plt.scatter(d.var_2017[which[0]], d.var_2017[which[1]])
                d.plt.xlabel("%s" % which[0])
                d.plt.ylabel("%s" % which[1])
                d.plt.title("%s VS %s" % (which[0], which[1]))
                d.plt.show()

    def setupUi(self, Relation):
        Relation.setObjectName("Relation")
        Relation.resize(1920, 1080)
        Relation.setMinimumSize(QtCore.QSize(1920, 1080))
        Relation.setMaximumSize(QtCore.QSize(1920, 1080))
        Relation.showMaximized()
        Relation.setStyleSheet("\n"
"background-color: rgb(219, 205, 166);")
        self.centralwidget = QtWidgets.QWidget(Relation)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 380, 1201, 671))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/regression.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 110, 631, 101))
        self.label_2.setStyleSheet("font: 90pt \"Kokila\";")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1200, 50, 51, 941))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1510, 440, 111, 101))
        self.label_3.setStyleSheet("font: 72pt \"Kokila\";")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1310, 620, 531, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.EC2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.EC2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/Economy.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EC2.setIcon(icon)
        self.EC2.setIconSize(QtCore.QSize(120, 120))
        self.EC2.setObjectName("EC2")
        self.horizontalLayout_4.addWidget(self.EC2)
        self.FA2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.FA2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/Family.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FA2.setIcon(icon1)
        self.FA2.setIconSize(QtCore.QSize(120, 120))
        self.FA2.setObjectName("FA2")
        self.horizontalLayout_4.addWidget(self.FA2)
        self.HE2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.HE2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/Health.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HE2.setIcon(icon2)
        self.HE2.setIconSize(QtCore.QSize(120, 120))
        self.HE2.setObjectName("HE2")
        self.horizontalLayout_4.addWidget(self.HE2)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.FR2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.FR2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Images/Freedom.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FR2.setIcon(icon3)
        self.FR2.setIconSize(QtCore.QSize(120, 120))
        self.FR2.setObjectName("FR2")
        self.horizontalLayout_5.addWidget(self.FR2)
        self.TR2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.TR2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Images/Trust.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TR2.setIcon(icon4)
        self.TR2.setIconSize(QtCore.QSize(120, 120))
        self.TR2.setObjectName("TR2")
        self.horizontalLayout_5.addWidget(self.TR2)
        self.GN2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.GN2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Images/Generosity.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GN2.setIcon(icon5)
        self.GN2.setIconSize(QtCore.QSize(120, 120))
        self.GN2.setObjectName("GN2")
        self.horizontalLayout_5.addWidget(self.GN2)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.Plot = QtWidgets.QPushButton(self.centralwidget)
        self.Plot.setGeometry(QtCore.QRect(1560, 950, 281, 61))
        self.Plot.setStyleSheet("background-color: rgb(50, 197, 17);\n"
"font: 36pt \"Kokila\";\n"
"border-radius: 30px")
        self.Plot.setObjectName("Plot")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(320, 260, 651, 81))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.horizontalLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.y2015 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.y2015.setStyleSheet("font: 24pt \"Kokila\";")
        self.y2015.setObjectName("y2015")
        self.gridLayout_3.addWidget(self.y2015, 0, 0, 1, 1)
        self.y2016 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.y2016.setStyleSheet("font: 24pt \"Kokila\";")
        self.y2016.setObjectName("y2016")
        self.gridLayout_3.addWidget(self.y2016, 0, 1, 1, 1)
        self.y2017 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.y2017.setStyleSheet("font: 24pt \"Kokila\";")
        self.y2017.setObjectName("y2017")
        self.gridLayout_3.addWidget(self.y2017, 0, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1310, 50, 531, 321))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EC = QtWidgets.QRadioButton(self.widget)
        self.EC.setText("")
        self.EC.setIcon(icon)
        self.EC.setIconSize(QtCore.QSize(120, 120))
        self.EC.setObjectName("EC")
        self.horizontalLayout.addWidget(self.EC)
        self.FA = QtWidgets.QRadioButton(self.widget)
        self.FA.setText("")
        self.FA.setIcon(icon1)
        self.FA.setIconSize(QtCore.QSize(120, 120))
        self.FA.setObjectName("FA")
        self.horizontalLayout.addWidget(self.FA)
        self.HE = QtWidgets.QRadioButton(self.widget)
        self.HE.setText("")
        self.HE.setIcon(icon2)
        self.HE.setIconSize(QtCore.QSize(120, 120))
        self.HE.setObjectName("HE")
        self.horizontalLayout.addWidget(self.HE)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FR = QtWidgets.QRadioButton(self.widget)
        self.FR.setText("")
        self.FR.setIcon(icon3)
        self.FR.setIconSize(QtCore.QSize(120, 120))
        self.FR.setObjectName("FR")
        self.horizontalLayout_2.addWidget(self.FR)
        self.TR = QtWidgets.QRadioButton(self.widget)
        self.TR.setText("")
        self.TR.setIcon(icon4)
        self.TR.setIconSize(QtCore.QSize(120, 120))
        self.TR.setObjectName("TR")
        self.horizontalLayout_2.addWidget(self.TR)
        self.GN = QtWidgets.QRadioButton(self.widget)
        self.GN.setText("")
        self.GN.setIcon(icon5)
        self.GN.setIconSize(QtCore.QSize(120, 120))
        self.GN.setObjectName("GN")
        self.horizontalLayout_2.addWidget(self.GN)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        Relation.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Relation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        Relation.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Relation)
        self.statusbar.setObjectName("statusbar")
        Relation.setStatusBar(self.statusbar)

####
        self.Plot.clicked.connect(self.plot_scatterplot)
####

        self.retranslateUi(Relation)
        QtCore.QMetaObject.connectSlotsByName(Relation)

    def retranslateUi(self, Relation):
        _translate = QtCore.QCoreApplication.translate
        Relation.setWindowTitle(_translate("Relation", "Relational Mapping"))
        self.label_2.setText(_translate("Relation", "Scatter Plots"))
        self.label_3.setText(_translate("Relation", "<html><head/><body><p><span style=\" font-style:italic;\">VS</span></p></body></html>"))
        self.EC2.setToolTip(_translate("Relation", "Economy"))
        self.FA2.setToolTip(_translate("Relation", "Family"))
        self.HE2.setToolTip(_translate("Relation", "Health"))
        self.FR2.setToolTip(_translate("Relation", "Freedom"))
        self.TR2.setToolTip(_translate("Relation", "Trust"))
        self.GN2.setToolTip(_translate("Relation", "Generosity"))
        self.Plot.setText(_translate("Relation", "PLOT"))
        self.y2015.setText(_translate("Relation", "2015"))
        self.y2016.setText(_translate("Relation", "2016"))
        self.y2017.setText(_translate("Relation", "2017"))
        self.EC.setToolTip(_translate("Relation", "Economy"))
        self.FA.setToolTip(_translate("Relation", "Family"))
        self.HE.setToolTip(_translate("Relation", "Health"))
        self.FR.setToolTip(_translate("Relation", "Freedom"))
        self.TR.setToolTip(_translate("Relation", "Trust"))
        self.GN.setToolTip(_translate("Relation", "Generosity"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Relation = QtWidgets.QMainWindow()
    ui = Ui_Relation()
    ui.setupUi(Relation)
    Relation.show()
    sys.exit(app.exec_())


from PyQt5 import sip
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
import sys

PARAMETERS = [1,2,3]

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MyLabelSlider(QVBoxLayout):
    def __init__(self, value, paramidx):
        if paramidx not in [0, 1, 2]:
            raise Exception
        super(MyLabelSlider, self).__init__()
        self.paramidx = paramidx
        self.label = QLabel(f"Parameter {paramidx + 1} has value {PARAMETERS[paramidx]}")
        self.label.setFont(QFont("Arial", 16))

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(-10)
        self.slider.setMaximum(10)
        self.slider.setValue(value)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.valueChanged.connect(self.change_parameter_value)

        self.addWidget(self.label)
        sliderLayout = QHBoxLayout()
        sliderLayout.addWidget(QLabel("-10"))
        sliderLayout.addWidget(self.slider)
        sliderLayout.addWidget(QLabel("10"))
        self.addLayout(sliderLayout)
        # self.setSpacing(100)
    
    def change_parameter_value(self, ):
        value = self.slider.value()
        PARAMETERS[self.paramidx] = value
        update_display()



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle("Simulation GUI Demo")

        layout1 = QHBoxLayout()
        layout1.setSpacing(10)
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        spacing_str = " " * 80
        self.myLabelSliders = [MyLabelSlider(i+1, i) for i in range(3)]
        layout2.addLayout(self.myLabelSliders[0])
        layout2.addWidget(QLabel(spacing_str))
        layout2.addLayout(self.myLabelSliders[1])
        layout2.addWidget(QLabel(spacing_str))
        layout2.addLayout(self.myLabelSliders[2])
        # layout2.setSpacing(10)

        layout1.addLayout( layout2 )

        self.chart = MplCanvas(self, width=10, height=8, dpi=100)
        self.chart.axes.bar([0, 1, 2], PARAMETERS)
        self.chart.axes.set_title("Parameter Values")
        self.chart.axes.set_xticks([0, 1, 2])
        self.chart.axes.set_xticklabels(["p1", "p2", "p3"])
        self.chart.axes.set_ylim(-10, 10)
        
        layout3.addWidget(self.chart)
        self.meanValueLabel = QLabel(f"Mean of parameters: {int(np.mean(PARAMETERS) * 100) / 100.}")
        self.meanValueLabel.setAlignment(Qt.AlignCenter)
        self.meanValueLabel.setFont(QFont("Arial", 20))
        layout3.addWidget(self.meanValueLabel, Qt.AlignCenter)

        layout1.addLayout( layout2 )
        layout1.addLayout( layout3 )

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
        self.show()

    def update_display(self):
        self.chart.axes.cla()
        self.chart.axes.bar([0, 1, 2], PARAMETERS)
        self.chart.axes.set_ylim(-10, 10)
        self.chart.axes.set_title("Parameter Values")
        self.chart.axes.set_xticks([0, 1, 2])
        self.chart.axes.set_xticklabels(["p1", "p2", "p3"])
        self.chart.draw()
        self.meanValueLabel.setText(f"Mean of parameters: {int(np.mean(PARAMETERS) * 100) / 100.}")
        for ls in self.myLabelSliders:
            ls.label.setText(f"Parameter {ls.paramidx + 1} has value {PARAMETERS[ls.paramidx]}")


app = QApplication(sys.argv)
window = Window()

def update_display():
    window.update_display()

sys.exit(app.exec_())
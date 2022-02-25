from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import sys

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

class MySlider(QSlider):
    def __init__(self, value, paramidx):
        super(MySlider, self).__init__(Qt.Horizontal)
        self.setMinimum(-10)
        self.setMaximum(10)
        self.setValue(value)
        self.setTickPosition(QSlider.TicksBelow)
        self.setTickInterval(5)

class MyLabelSlider(QVBoxLayout):
    def __init__(self, value, paramidx):
        if paramidx not in [1, 2, 3]:
            raise Exception
        self.label = QLabel(f"Parameter {paramidx}")
        self.label.setFont(QFont("Arial", 16))

        self.slider = QSlider()
        self.slider.setMinimum(-10)
        self.slider.setMaximum(10)
        self.slider.setValue(value)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)

        self.addWidget(self.label)
        self.addWidget(self.slider)



class Window(QMainWindow):
   def __init__(self):
    super().__init__()

    self.setGeometry(300, 300, 600, 400)
    self.setWindowTitle("Simulation GUI Demo")

    layout1 = QHBoxLayout()
    layout2 = QVBoxLayout()

    layout2.addWidget(Color('red'))
    layout2.addWidget(Color('yellow'))
    layout2.addWidget(Color('purple'))

    layout1.addLayout( layout2 )

    chart = MplCanvas(self, width=5, height=4, dpi=100)
    chart.axes.bar([0, 1, 2], parameters)
    chart.axes.set_title("Your parameters")
    chart.axes.set_xticks([0, 1, 2])
    chart.axes.set_xticklabels(["p1", "p2", "p3"])
    
    layout1.addWidget(chart)


    widget = QWidget()
    widget.setLayout(layout1)
    self.setCentralWidget(widget)
    self.show()

parameters = [3,2,1]
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
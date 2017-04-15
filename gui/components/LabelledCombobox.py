from PyQt5.QtWidgets import QWidget, QComboBox, QLabel, QHBoxLayout
from PyQt5 import QtCore

class LabelledCombobox(QWidget):

    def __init__(self, parent, text, items=None):

        QWidget.__init__(self, parent)

        layout = QHBoxLayout()
        self.setLayout(layout)
        label = QLabel(text)
        self.fields = QComboBox()
        if items:
            self.fields.addItems(items)

        self.layout().addWidget(label)
        self.layout().addWidget(self.fields)

    def select(self, text):
        index = self.fields.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.fields.setCurrentIndex(index)
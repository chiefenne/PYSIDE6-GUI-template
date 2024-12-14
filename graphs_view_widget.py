from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class GraphsViewWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        label = QLabel("Graphs will be displayed here.")
        layout.addWidget(label)
        self.setLayout(layout)

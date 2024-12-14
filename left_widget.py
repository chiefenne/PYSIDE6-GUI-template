from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel

class LeftWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Step through options:")
        layout.addWidget(self.label)

        self.list_widget = QListWidget()
        self.list_widget.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from PySide6.QtGui import QPen, QBrush
from PySide6.QtCore import Qt

from graphics_items import CustomRectItem, CustomEllipseItem

class GraphicsViewWidget(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.init_graphics_items()

    def init_graphics_items(self):
        # Add rectangles and circles
        rect_item = CustomRectItem(10, 10, 100, 50)
        rect_item.setPen(QPen(Qt.black))
        rect_item.setBrush(QBrush(Qt.blue))
        self.scene.addItem(rect_item)

        ellipse_item = CustomEllipseItem(150, 50, 80, 80)
        ellipse_item.setPen(QPen(Qt.black))
        ellipse_item.setBrush(QBrush(Qt.red))
        self.scene.addItem(ellipse_item)

from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsEllipseItem, QMenu, QGraphicsItem
from PySide6.QtGui import QContextMenuEvent, QMouseEvent
from PySide6.QtCore import Qt

class CustomRectItem(QGraphicsRectItem):
    def __init__(self, *args, z_value=0):
        super().__init__(*args)
        flags = QGraphicsItem.GraphicsItemFlag.ItemIsSelectable | QGraphicsItem.GraphicsItemFlag.ItemIsMovable
        self.setFlags(flags)
        self.setAcceptHoverEvents(True)
        self.setZValue(z_value)
        self.setCacheMode(QGraphicsItem.CacheMode.DeviceCoordinateCache)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Bring item to top when clicked
            all_items = self.scene().items()
            max_z = max([i.zValue() for i in all_items])
            self.setZValue(max_z + 1)
            self.update()
            self.scene().update()
        super().mousePressEvent(event)

    def contextMenuEvent(self, event):
        context_menu = QMenu()
        zoom_action = context_menu.addAction("Zoom to Fit")
        # Add other actions as needed
        action = context_menu.exec(event.screenPos())
        if action == zoom_action:
            # Implement "Zoom to Fit" functionality
            self.scene().views()[0].fitInView(self, Qt.KeepAspectRatio)


class CustomEllipseItem(QGraphicsEllipseItem):
    def __init__(self, *args, z_value=0):
        super().__init__(*args)
        flags = QGraphicsItem.GraphicsItemFlag.ItemIsSelectable | QGraphicsItem.GraphicsItemFlag.ItemIsMovable
        self.setFlags(flags)
        self.setAcceptHoverEvents(True)
        self.setZValue(z_value)
        self.setCacheMode(QGraphicsItem.CacheMode.DeviceCoordinateCache)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Bring item to top when clicked
            all_items = self.scene().items()
            max_z = max([i.zValue() for i in all_items])
            self.setZValue(max_z + 1)
            self.update()
            self.scene().update()
        super().mousePressEvent(event)

    def contextMenuEvent(self, event):
        context_menu = QMenu()
        zoom_action = context_menu.addAction("Zoom to Fit")
        # Add other actions as needed
        action = context_menu.exec(event.screenPos())
        if action == zoom_action:
            # Implement "Zoom to Fit" functionality
            self.scene().views()[0].fitInView(self, Qt.KeepAspectRatio)

from PySide6.QtWidgets import (
    QMainWindow, QDockWidget, QToolBar, QMenu, QTabWidget, QMenuBar, QStyle,
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from menu_loader import load_menus_from_json
from left_widget import LeftWidget
from status_window import StatusWindow
from graphics_view_widget import GraphicsViewWidget
from graphs_view_widget import GraphsViewWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dynamic Menu GUI Template")
        self.resize(1200, 800)

        # Initialize storage for actions
        self.actions = {}

        self.menu_bar = QMenuBar(self)
        self.menu_bar.setNativeMenuBar(False)  # Force menu bar into the window
        self.setMenuBar(self.menu_bar)

        # Load menus from JSON file
        self.init_menus()

        # Create toolbar
        self.init_toolbar()

        # Create status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")  # Optional initial message

        # Create status window before initializing dock windows
        self.status_window = StatusWindow()

        # Create the central widget (tabbed widget with graphics and graphs views)
        self.init_central_widget()

        # Create dockable windows
        self.init_dock_windows()

    def init_menus(self):
        menus = load_menus_from_json('menu.json')
        for menu_name, submenus in menus.items():
            menu = QMenu(menu_name, self)
            self.menu_bar.addMenu(menu)
            self.add_menu_items(menu, submenus)

    def add_menu_items(self, menu, items):
        for item in items:
            if 'submenu' in item:
                submenu = QMenu(item['name'], self)
                menu.addMenu(submenu)
                self.add_menu_items(submenu, item['submenu'])
            else:
                action = QAction(item['name'], self)
                menu.addAction(action)
                # Store actions for use in toolbar
                self.actions[item['name']] = action

    def init_toolbar(self):
        self.tool_bar = QToolBar("Main Toolbar", self)
        self.addToolBar(self.tool_bar)

        # use QT built-in icons
        names = ['SP_DialogOpenButton', 'SP_DialogSaveButton', 'SP_DialogHelpButton']

        # add icons to toolbar
        for name in names:
            pixmapi = getattr(QStyle, name)
            icon = self.style().standardIcon(pixmapi)
            action = QAction(icon, "", self)
            self.tool_bar.addAction(action)
            action.setToolTip(name[3:])  # Add tooltip
        
    def init_central_widget(self):
        # Create a tab widget as the central widget
        self.tabs = QTabWidget()
        # Graphics View tab
        self.graphics_view_widget = GraphicsViewWidget()
        self.tabs.addTab(self.graphics_view_widget, "Graphics View")
        # Graphs View tab
        self.graphs_view_widget = GraphsViewWidget()
        self.tabs.addTab(self.graphs_view_widget, "Graphs View")
        self.setCentralWidget(self.tabs)

    def init_dock_windows(self):
        # Left dock widget
        self.left_dock = QDockWidget("Options", self)
        self.left_widget = LeftWidget()
        self.left_dock.setWidget(self.left_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.left_dock)

        # Bottom dock widget (status message window with scrolling)
        self.bottom_dock = QDockWidget("Status Messages", self)
        self.bottom_dock.setWidget(self.status_window)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.bottom_dock)

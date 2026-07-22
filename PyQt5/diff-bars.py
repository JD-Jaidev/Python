import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction,
    QLabel, QPushButton
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MenuBar, ToolBar & StatusBar")
        self.resize(700, 500)

        # Central Widget
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        # ==================================================
        # STATUS BAR
        # ==================================================

        status = self.statusBar()              # Creates/Returns the status bar
        status.showMessage("Application Ready")  # Displays a temporary message

        label = QLabel("Logged In")
        status.addPermanentWidget(label)       # Permanent widget (right side)

        button = QPushButton("Help")
        status.addWidget(button)               # Temporary widget (left side)

        # ==================================================
        # ACTIONS
        # ==================================================

        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)
        copy_action = QAction("Copy", self)
        paste_action = QAction("Paste", self)

        # ---------- QAction Methods ----------

        open_action.setShortcut("Ctrl+O")          # Keyboard shortcut
        save_action.setShortcut("Ctrl+S")
        copy_action.setShortcut("Ctrl+C")
        paste_action.setShortcut("Ctrl+V")

        open_action.setStatusTip("Open a File")
        save_action.setStatusTip("Save Current File")

        open_action.setCheckable(True)             # Makes action checkable
        open_action.setChecked(False)

        copy_action.setEnabled(True)               # Enable Action
        paste_action.setEnabled(True)

        # ---------- QAction Signals ----------

        open_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)
        exit_action.triggered.connect(self.close)

        copy_action.triggered.connect(self.editor.copy)
        paste_action.triggered.connect(self.editor.paste)

        # ==================================================
        # MENU BAR
        # ==================================================

        menubar = self.menuBar()              # Returns MenuBar

        # ---------- addMenu() ----------

        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")
        help_menu = menubar.addMenu("Help")

        # ---------- addAction() ----------

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        # ---------- addSeparator() ----------

        file_menu.addSeparator()

        file_menu.addAction(exit_action)

        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)

        # ---------- addMenu() (Submenu) ----------

        recent_menu = file_menu.addMenu("Recent Files")

        recent1 = QAction("Python.txt", self)
        recent2 = QAction("Notes.docx", self)

        recent_menu.addAction(recent1)
        recent_menu.addAction(recent2)

        # ==================================================
        # TOOL BAR
        # ==================================================

        toolbar = self.addToolBar("Main Toolbar")

        # ---------- Toolbar Methods ----------

        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

        toolbar.addSeparator()

        toolbar.addAction(copy_action)
        toolbar.addAction(paste_action)

        toolbar.addSeparator()

        toolbar.addWidget(QPushButton("Login"))

        toolbar.setMovable(True)          # Toolbar can be moved
        toolbar.setFloatable(True)        # Toolbar can float
        toolbar.setVisible(True)          # Show toolbar

    # ==================================================
    # Slots
    # ==================================================

    def open_file(self):
        self.statusBar().showMessage("Open Clicked", 3000)

    def save_file(self):
        self.statusBar().showMessage("Save Clicked", 3000)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())
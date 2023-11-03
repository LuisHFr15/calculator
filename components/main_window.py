from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs,) -> None:
        
        # setting the initial layout
        super().__init__(parent, *args, **kwargs,)
        self._cw = QWidget()
        self._v_layout = QVBoxLayout()
        self._cw.setLayout(self._v_layout)
        self.setCentralWidget(self._cw)
        
        # window title
        self.setWindowTitle('Calculator')
        
        
    def adjust_fixed_size(self,) -> None:
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        
    def add_to_v_layout(self, widget: QWidget,) -> None:
        self._v_layout.addWidget(widget)
        
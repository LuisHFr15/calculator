from PySide6.QtWidgets import QLabel, QWidget
from .variables import SMALL_FONT_SIZE
from PySide6.QtCore import Qt

# left + operator + right 
class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None,) -> None:
        super().__init__(text, parent)  
        self.__config_style() 
        
    def __config_style(self,) -> None:
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
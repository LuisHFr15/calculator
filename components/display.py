from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from .variables import (BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN)
from .utils import is_empty

class Display(QLineEdit): 
    def __init__(self, *args, **kwargs,) -> None:
        super().__init__(*args, **kwargs)
        
        self.__config_style()
        
        
    def __config_style(self,) -> None:
        self.setStyleSheet(f'font-size:{BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setTextMargins(*margins)
        
    
        
        
        
    
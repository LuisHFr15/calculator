from typing import TYPE_CHECKING

from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from .variables import MEDIUM_FONT_SIZE
from .utils import is_valid_number
from .operations import (two_operator_eq_, one_operator_eq_, operator_clicked, inverse)
# avoiding circular imports
if TYPE_CHECKING:
    from .info import Info
    from .display import Display


class Button(QPushButton):
    def __init__(self, *args, **kwargs,) -> None:
        super().__init__(*args, **kwargs)
        self.__config_style()
        
    def __config_style(self,) -> None:
        # same thing as setStyleSheet
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setBold(True)
        self.setMinimumSize(60, 60)
        self.setFont(font)
        
    
class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs,) -> None:
        super().__init__(*args, **kwargs)
        
        self._grid_ = [
            ['|x|', 'CE', 'C', '◀'],
            ['1/x', '^', '√', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-',  '0', '.', '='],
        ]

        self._display = display
        self._info = info
        self._equation_value = ''
        self._left = None
        self._right = None
        self._op = None
        self._display.insert('0')
        self._make_grid()
        
    
    @property
    def _equation(self) -> str:
        return self._equation_value
    

    @_equation.setter
    def _equation(self, string: str) -> None:
        self._equation_value = string
        self._info.setText(string)
        
        
    def _make_grid(self,) -> None:
        for row_number, row in enumerate(self._grid_):
            for column_number, text in enumerate(row):
                button = Button(text)
                
                if row_number == 0 or row_number == 1 or column_number == 3 or (row_number == 5 and column_number == 0):
                    if button.text() != '+/-':
                        button.setProperty('cssClass', 'specialButton')
                    else:
                        button.setProperty('cssClass', 'commonButton')
                        
                    self._config_special_button(button)
                    
                else:
                    button.setProperty('cssClass', 'commonButton')
                
                self.addWidget(button, row_number, column_number)
                
                button_slot = self._make_slot(self._insert_button_text_to_display, button,)
                self._connect_clicked(button, button_slot)
                
                
    def _connect_clicked(self, button: Button, slot) -> None:
        button.clicked.connect(slot)         
    
    
    # show in the display the button clicked
    def _make_slot(self, func, *args, **kwargs,) -> None:
        @Slot()
        def real_slot():
            func(*args, **kwargs)
            
        return real_slot
    
    
    def _config_special_button(self, button: Button) -> None:
        text = button.text()
        
        if text == 'CE':
            self._connect_clicked(button, self._clear_display,)
            
        elif text == 'C':
            self._connect_clicked(button, self._clear_all,)
            
        elif text == '=':
            self._connect_clicked(button, self._make_slot(two_operator_eq_, self))
            
        elif text == '◀':
            self._connect_clicked(button, self._display.backspace)
            
        elif text == '+/-':
            self._connect_clicked(button, self._make_slot(inverse, self))
            
        elif text == '1/x' or text == '|x|' or text == '√':
            self._connect_clicked(button, self._make_slot(one_operator_eq_, self, button))
            
        else:
            self._connect_clicked(button, self._make_slot(operator_clicked, self, button))
        
                
    def _insert_button_text_to_display(self, button: Button,) -> None:
            
        text = button.text()
        new_display_value = self._display.text() + text
        
        if not is_valid_number(new_display_value):
            return
            
        if self._display.text() != '0' and '=' in self._equation:
            self._clear_all()
            
        if self._display.text() == '0':
            self._display.clear()
        
        self._display.insert(button.text())
        
    
    def _clear_display(self) -> None:
        self._display.clear()
        self._display.insert('0')
        if self._op == None:
            self._left = None
        else:
            self._right = None
        
        
    def _clear_all(self) -> None:
        self._display.clear()
        self._display.insert('0')
        self._left = None
        self._right = None
        self._op = None
        self._equation = ''
        
        
    
            

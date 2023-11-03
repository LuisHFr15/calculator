from typing import TYPE_CHECKING

from .utils import is_valid_number
import math
if TYPE_CHECKING:
    from .buttons import Button, ButtonsGrid


def inverse(buttonsg: 'ButtonsGrid') -> None:
    display_text = buttonsg._display.text()
    buttonsg._display.clear()
        
    if not is_valid_number(display_text):
        return
    
    
    if '.' not in display_text:
        new_display_value = -1 * int(display_text)
    else:
        new_display_value = -1 * float(display_text)
        
    if display_text != '0' and '=' in buttonsg._equation:
        buttonsg._clear_all()
            
    if display_text == '0':
        buttonsg._display.clear()
      
    buttonsg._display.insert(str(new_display_value))
        
        
def operator_clicked(buttonsg: 'ButtonsGrid', button: 'Button') -> None:
    display_text = buttonsg._display.text()
    buttonsg._clear_display()
        
    if buttonsg._left == None:
        if '.' not in display_text:
            buttonsg._left = int(display_text)
        else:
            buttonsg._left = float(display_text)
        
    buttonsg._op = button.text()
    buttonsg._equation = f'{buttonsg._left} {buttonsg._op}'
        
    
def two_operator_eq_(buttonsg: 'ButtonsGrid') -> None:
    display_text = buttonsg._display.text()
    buttonsg._clear_display()
        
    if buttonsg._right == None:
        if '.' not in display_text:
            buttonsg._right = int(display_text)
        else:
            buttonsg._right = float(display_text)
                
    buttonsg._equation = f'{buttonsg._left} {buttonsg._op} {buttonsg._right} ='
    result = 0.0
            
    try:
        if buttonsg._op == '+':
            result = buttonsg._left + buttonsg._right
        elif buttonsg._op == '-':
            result = buttonsg._left - buttonsg._right
        elif buttonsg._op == '×':
            result = buttonsg._left * buttonsg._right
        elif buttonsg._op == '÷':
            result = buttonsg._left / buttonsg._right
            if buttonsg._left % buttonsg._right == 0:
                result = int(result)
        elif buttonsg._op == '^':
            result = math.pow(buttonsg._left, buttonsg._right)
            if '.' in str(result):
                if result.is_integer():
                    result = int(result)
    except ZeroDivisionError:
        result = ''
            
    if result == '':
        buttonsg._clear_all()
    else:
        if '.' in str(result):
            if result.is_integer():
                result = int(result)
        buttonsg._display.setText(str(result))
        buttonsg._info.setText(f'{buttonsg._equation} {result}')
        buttonsg._left = result
        buttonsg._right = None
            
    
def sqrt(buttonsg: 'ButtonsGrid', result) -> int | float:
    buttonsg._equation = f'{buttonsg._op}{buttonsg._left} ='
    result = math.sqrt(buttonsg._left)
    if '.' in str(result):
        if result.is_integer():
            return int(result)
        
    return result
    
    
def division_one(buttonsg: 'ButtonsGrid', result) -> float:
    buttonsg._equation = f'1/{buttonsg._left} ='
    result = 1 / buttonsg._left
        
    return result
  
  
def one_operator_eq_(buttonsg: 'ButtonsGrid', button: 'Button') -> None:
    display_text = buttonsg._display.text()
    buttonsg._clear_display()
        
    if buttonsg._left == None:
        if '.' not in display_text:
            buttonsg._left = int(display_text)
        else:
            buttonsg._left = float(display_text)
        
    buttonsg._op = button.text()
                
    result = 0
    if buttonsg._op == '√':
        if buttonsg._left < 0:
            buttonsg._clear_all()
            return
        result = sqrt(buttonsg, result)
                
    elif buttonsg._op == '1/x':
        if buttonsg._left == 0:
            buttonsg._clear_all()
            return
        result = division_one(buttonsg, result)
                
    else:
        buttonsg._equation = f'abs({buttonsg._left}) ='
        result = abs(buttonsg._left)
            
    if result == '':
        buttonsg._clear_all()
    else:
        buttonsg._display.setText(str(result))
        buttonsg._info.setText(f'{buttonsg._equation} {result}')
        buttonsg._left = result
        buttonsg._right = None
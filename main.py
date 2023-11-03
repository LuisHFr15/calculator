from PySide6.QtWidgets import QApplication
import sys
from components.main_window import MainWindow
from components.variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from components.display import Display
from components.info import Info
from components.styles import setup_theme
from components.buttons import ButtonsGrid



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    setup_theme()
    # changing the app and window icon
    icon = QIcon()
    icon.addFile(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    

    # info (last math result)
    info = Info('')
    window.add_to_v_layout(info)
    
    # creating display
    display = Display()
    window.add_to_v_layout(display)
    
    # buttons grid
    buttons_grid = ButtonsGrid(display, info)
    window._v_layout.addLayout(buttons_grid)
    
    

    window.adjust_fixed_size()
    window.show()
    app.exec()
    
# https://doc.qt.io/qtforpython-6/tutorials/basictutorial/widgetstyling.html
# QSS -> Qt Style Sheet

import qdarktheme
from .variables import (SPECIAL_PRIMARY_COLOR, SPECIAL_DARKER_PRIMARY_COLOR,
                        SPECIAL_DARKEST_PRIMARY_COLOR, PRIMARY_COLOR,
                        DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR)


qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {SPECIAL_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {SPECIAL_DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {SPECIAL_DARKEST_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="commonButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="commonButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="commonButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setup_theme() -> None:
    qdarktheme.setup_theme(theme='dark', corner_shape='rounded',
                           custom_colors={"dark" : {"primary" : f"{PRIMARY_COLOR}",},
                                          "light" : {"primary" : f"{PRIMARY_COLOR}"},},
                           additional_qss=qss,)

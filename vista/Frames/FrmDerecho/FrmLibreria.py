from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class FrmLibreria(QTabWidget):
    def __init__(self, p):
        super().__init__(parent=p)
        self.alta = QWidget()
        self.layout = QGridLayout(self.alta)

    def setupUi(self, Form):
        verticalSpacer = QSpacerItem(20, 71, QSizePolicy.Minimum, QSizePolicy.Expanding)
        horizontalSpacer = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout.addItem(verticalSpacer, 0, 1)
        self.layout.addItem(horizontalSpacer, 1, 0)

        self.pnl_alta = QWidget(self.alta)
        self.pnl_alta.setObjectName(u"pnl_alta")
        self.pnl_alta.setMinimumSize(QSize(400, 250))

        self.layout.addWidget(self.pnl_alta, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout.addItem(self.horizontalSpacer_2, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 71, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.tabWidget.addTab(self.alta, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alta), QCoreApplication.translate("Form", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tab 2", None))
    # retranslateUi


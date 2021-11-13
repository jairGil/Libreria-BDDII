from vista.App import App

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    frm = App()
    sys.exit(app.exec_())
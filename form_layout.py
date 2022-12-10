import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Adding a title
        self.setWindowTitle(
            "Financial Support For Attending International Conference")
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)
        heading = qtw.QLabel(
            "Financial Support For Attending International Conference")
        heading.setFont(qtg.QFont("Helvetica", 24))
        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)
        # Adding rows to the app
        form_layout.addRow(heading)
        form_layout.addRow("First Name", f_name)
        form_layout.addRow("Last Name ", l_name)
        form_layout.addRow(qtw.QPushButton(
            "Click Me!   ", clicked=lambda: press_it()))
        # Show the app
        self.show()

        def press_it():
            heading.setText(
                f'You clicked the button {f_name.text()} {l_name.text()}')
            print(f'First name: {f_name.text()} {l_name.text()}')


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())

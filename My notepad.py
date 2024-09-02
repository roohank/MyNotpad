from PyQt6.QtWidgets import  QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QPlainTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence, QShortcut

from spacesToTab import replace_spaces_with_tabs, replace_tabs_with_spaces


file_name = 'Output.txt'


class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Notepad')
        self.resize(300, 260)
        
        # self.text_edit = QTextEdit()
        self.text_edit = QPlainTextEdit()
        self.text_edit.setTabChangesFocus(True)
        self.save_btn = QPushButton('Save')
        self.save_btn.setEnabled(False)
        self.change_btn = QPushButton('Spaces To Tab')
        self.change_btn.setEnabled(False)

        self.change_btn_2 = QPushButton('Tab To Spaces')
        self.change_btn_2.setEnabled(False)


        self.open_btn = QPushButton('Open')


        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.change_btn)
        btn_layout.addWidget(self.change_btn_2)
        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.open_btn)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.text_edit)
        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)

        self.open_btn.clicked.connect(self.on_open)
        self.save_btn.clicked.connect(self.on_save)
        self.change_btn.clicked.connect(self.on_change_to_tabs)
        self.change_btn_2.clicked.connect(self.on_change_to_spaces)
        self.text_edit.textChanged.connect(self.on_edit)

        QShortcut(QKeySequence('Ctrl+S'),self, self.on_save)
        QShortcut(QKeySequence('Ctrl+O'), self, self.on_open)
        QShortcut(QKeySequence('Ctrl+Delete'), self, self.clear)
        QShortcut(QKeySequence('Ctrl+X'), self, self.close)

        self.show()
        self.open_btn.setFocus()
        # print(self.size())
        
    def on_open(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, 'r', encoding= 'utf-8') as f:
                # print(f.read()) # اگر این خط کامنت نباشد چون یک بار متد read اجرا می شود  برای بار دوم که قرار است مقدار آن در text قرار بگیرد این مقدار خالی خواهد بود
                text = f.read()
                # print(type(text))
                self.text_edit.setPlainText(text)
            self.text_edit.setFocus()

    def on_change_to_tabs(self):
        # دریافت متن از QTextEdit
        text = self.text_edit.toPlainText()
        txt_format = "'''" + text + "'''"
        
        lines = txt_format.split('\n')
        processed_lines = [replace_spaces_with_tabs(line) for line in lines]
        output_code = '\n'.join(processed_lines)

        output_code = output_code[3:-3]
        self.clear()
        self.text_edit.setPlainText(output_code)
        self.text_edit.setFocus()

    def on_change_to_spaces(self):
        # دریافت متن از QTextEdit
        text = self.text_edit.toPlainText()
        txt_format = "'''" + text + "'''"
    
        lines = txt_format.split('\n')
        processed_lines = [replace_tabs_with_spaces(line) for line in lines]
        output_code = '\n'.join(processed_lines)

        output_code = output_code[3:-3]
        self.clear()
        self.text_edit.setPlainText(output_code)
        self.text_edit.setFocus()

    def on_save(self):
        file_name, x = QFileDialog.getSaveFileName(self, "Save File", "test.txt", "Text Files (*.txt);;All Files (*.*)")
        #print(file_name)
        #print(x)
        # return
        if file_name:
            # print(file_name)
            with open(file_name, 'w', encoding= 'utf-8') as f:
                f.write(self.text_edit.toPlainText())
            self.text_edit.setFocus()

    def on_edit(self):
        self.save_btn.setEnabled(bool(self.text_edit.toPlainText().strip()))
        self.change_btn.setEnabled(bool(self.text_edit.toPlainText().strip()))
        self.change_btn_2.setEnabled(bool(self.text_edit.toPlainText().strip()))



        
    def clear(self):
        self.text_edit.clear()
app = QApplication([])
window = Notepad()
window.show()
app.exec()

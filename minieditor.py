# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:59:43 2019

@author: seiic
"""
import sys
from PyQt5 import QtWidgets
from minieditor_window import Ui_MainWindow

class minieditor(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(minieditor, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectSignal()
    
    # Qt Designerで実装していないシグナルをコネクト
    def connectSignal(self):
        self.ui.actionSave_as.triggered.connect(self.save_text)
        self.ui.actionFont.triggered.connect(self.font_select)
        self.ui.actionsave_as_html.triggered.connect(self.save_html)
      
    # フォントダイアログを表示して、テキストエディットのフォント変更
    def font_select(self):
        (font, ok) = QtWidgets.QFontDialog.getFont(self)
        if ok:
            self.ui.mainEdit.setFont(font)
    
    # ファイルダイアログを使って、ファイル名を取得して保存
    def save_text(self):
        text = self.ui.mainEdit.toPlainText()
        (file, selected_filter) = QtWidgets.QFileDialog.getSaveFileName(self)
        if file != '':
            with open(file, mode='w') as f:
                f.write(text)

    # ファイルダイアログにフィルタでHTMLをかけて、ファイルを保存
    def save_html(self):
        text = self.ui.mainEdit.toHtml()
        (file, selected_filter) = QtWidgets.QFileDialog.getSaveFileName(self, initialFilter="HTML file (*.html)", filter="HTML file (*.html)")
        if file != '':
            with open(file, mode='w') as f:
                f.write(text)
      

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = minieditor()
    window.show()
    sys.exit(app.exec_())
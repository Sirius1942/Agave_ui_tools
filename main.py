
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.main_window import Ui_MainWindow
# from login import Ui_dialog
from lib.tcmd import TCmdClass



# from SignalsE import Example

class MyMainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.cmdlists=TCmdClass()

    def addtext(self):
        _translate = QtCore.QCoreApplication.translate
        self.textEdit.setHtml(_translate("MainWindow",self.getText("abc")))
        # 每次修改内容，自动将光标移到最后
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        self.textEdit.setTextCursor(cursor)


    def getText(self,text):

        self.cmdlists.addText(text)


        return self.cmdlists.getText()

# class SignalsWindow(QWidget,SignalsExample):
# 	def __init__(self,parent=None):
#         super(SignalsExample,self).__init__(parent)
#         self.setupUi(self)
#     def keyPressEvent(self, e):
        
#         if e.key() == Qt.Key_Escape:
#             self.close()

if __name__=="__main__":

    app=QApplication(sys.argv)
    myWin=MyMainWindow()
    myWin.show()
    # sig=SignalsWindow()
    sys.exit(app.exec_())


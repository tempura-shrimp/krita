from PyQt5.QtWidgets import QAction, QMessageBox
from PyQt5.QtGui import QIcon
import sys
from . import docwrapper
import os
from scripter import resources_rc


class RunAction(QAction):

    def __init__(self, scripter, parent=None):
        super(RunAction, self).__init__(parent)
        self.scripter = scripter

        self.editor = self.scripter.uicontroller.editor
        self.output = self.scripter.uicontroller.findStackWidget('OutPut')

        self.triggered.connect(self.run)

        self.setText('Run')
        self.setIcon(QIcon(':/icons/run.svg'))

    @property
    def parent(self):
        return 'toolBar'

    def run(self):
        stdout = sys.stdout
        stderr = sys.stderr
        output = docwrapper.DocWrapper(self.output.document())
        output.write("======================================\n")
        sys.stdout = output
        sys.stderr = output
        script = self.editor.document().toPlainText()
        try:
            exec(script)
        except Exception as e:
            self.scripter.uicontroller.showException(str(e))
        sys.stdout = stdout
        sys.stderr = stderr

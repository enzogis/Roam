import os

from functools import partial

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import Qt
from qgis.core import QgsMapLayer

from configmanager.editorwidgets.core import ConfigWidget
from configmanager.editorwidgets.uifiles.ui_option_config import Ui_Form


class OptionWidgetConfig(Ui_Form, ConfigWidget):
    description = 'Select a item from a row of buttons'

    def __init__(self, parent=None):
        super(OptionWidgetConfig, self).__init__(parent)
        self.setupUi(self)
        self.multiCheck.stateChanged.connect(self.widgetchanged)

    def getconfig(self):
        config = {}
        config['list'] = {}
        config['list']['items'] = [item for item in self.listText.toPlainText().split('\n')]
        config['multi'] = self.multiCheck.isChecked()
        return config

    def setconfig(self, config):
        self.blockSignals(True)
        subconfig = config.get('list', {})
        multi = subconfig.get('multi', False)
        self.list = subconfig.get('items', [])
        itemtext = '\n'.join(self.list)
        self.listText.setPlainText(itemtext)
        self.multiCheck.setChecked(multi)
        self.blockSignals(False)


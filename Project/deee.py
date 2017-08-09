#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Custom TabBar and TabWidget.
Tabs like ChromeOS for Python3 Qt5 with Extras like UnDock / ReDock Tabs,
Pin / UnPin Tabs, On Mouse Hover Previews for all Tabs except current Tab,
Colored Tabs, Change Position, Change Shape, Fading Transition effect,
Close all Tabs to the Right, Close all Tabs to the Left, Close all other Tabs,
Mouse Hover Tracking, Add Tab Plus Button, Limit Maximum of Tabs, and more.
"""


from PyQt5.QtCore import QEvent, QTimeLine, QTimer

from PyQt5.QtGui import QBrush, QColor, QCursor, QPainter, QRadialGradient

from PyQt5.QtWidgets import (QColorDialog, QDialog, QInputDialog, QLabel,
                             QMainWindow, QMenu, QMessageBox, QTabBar,
                             QTabWidget, QToolButton, QVBoxLayout)


##############################################################################


class FaderWidget(QLabel):

    """Custom Placeholder Fading Widget for tabs on TabWidget."""

    def __init__(self, parent):
        """Init class."""
        super(FaderWidget, self).__init__(parent)
        self.timeline, self.opacity, self.old_pic = QTimeLine(), 1.0, None
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(750)  # 500 ~ 750 Ms is Ok, Not more.

    def paintEvent(self, event):
        """Overloaded paintEvent to set opacity and pic."""
        painter = QPainter(self)
        painter.setOpacity(self.opacity)
        if self.old_pic:
            painter.drawPixmap(0, 0, self.old_pic)

    def animate(self, value):
        """Animation of Opacity."""
        self.opacity = 1.0 - value
        return self.hide() if self.opacity < 0.1 else self.repaint()

    def fade(self, old_pic, old_geometry, move_to):
        """Fade from previous tab to new tab."""
        if self.isVisible():
            self.close()
        if self.timeline.state():
            self.timeline.stop()
        self.setGeometry(old_geometry)
        self.move(1, move_to)
        self.old_pic = old_pic
        self.timeline.start()
        self.show()


class TabBar(QTabBar):

    """Custom tab bar."""

    def __init__(self, parent=None, *args, **kwargs):
        """Init class custom tab bar."""
        super(TabBar, self).__init__(parent=None, *args, **kwargs)
        self.parent, self.limit = parent, self.count() * 2
        self.menu, self.submenu = QMenu("Tab Options"), QMenu("Tabs")
        self.tab_previews = True
        self.menu.addAction("Tab Menu").setDisabled(True)
        self.menu.addSeparator()
        self.menu.addAction("Set Tab Text", self.set_text)
        self.menu.addAction("Set Tab Color", self.set_color)
        self.menu.addAction("Set Limits", self.set_limit)
        self.menu.addSeparator()
        self.menu.addAction("Change Tab Shape", self.set_shape)
        self.menu.addAction("Top or Bottom Position", self.set_position)
        self.menu.addAction("Pin or Unpin Tab", self.set_pinned)
        self.menu.addAction("Undock Tab", self.make_undock)
        self.menu.addAction("Toggle Tabs Previews", self.set_tab_previews)
        self.menu.addSeparator()
        self.menu.addAction("Close this Tab",
                            lambda: self.removeTab(self.currentIndex()))
        self.menu.addAction("Close all Tabs to the Right",
                            self.close_all_tabs_to_the_right)
        self.menu.addAction("Close all Tabs to the Left",
                            self.close_all_tabs_to_the_left)
        self.menu.addAction("Close all other Tabs", self.close_all_other_tabs)
        self.menu.addSeparator()
        self.menu.addMenu(self.submenu)
        self.menu.aboutToShow.connect(self.build_submenu)
        self.tabCloseRequested.connect(
            lambda: self.removeTab(self.currentIndex()))
        self.setMouseTracking(True)
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        """Custom Events Filder for detecting clicks on Tabs."""
        if obj == self:
            if event.type() == QEvent.MouseMove:
                index = self.tabAt(event.pos())
                self.setCurrentIndex(index)
                return True
            else:
                return QTabBar.eventFilter(self, obj, event)  # False
        else:
            return QMainWindow.eventFilter(self, obj, event)

    def mouseDoubleClickEvent(self, event):
        """Handle double click."""
        self.menu.exec_(QCursor.pos())

    def set_tab_previews(self):
        """Toggle On/Off the Tabs Previews."""
        self.tab_previews = not self.tab_previews
        return self.tab_previews

    def close_all_tabs_to_the_right(self):
        """Close all tabs to the Right."""
        for i in range(self.currentIndex() + 1, self.count()):
            if self.count() > 2:
                self.removeTab(self.count() - 1)

    def close_all_tabs_to_the_left(self):
        """Close all tabs to the Left."""
        for i in range(self.currentIndex()):
            if self.count() > 2:
                self.removeTab(0)

    def close_all_other_tabs(self):
        """Close all other tabs."""
        self.close_all_tabs_to_the_right()
        self.close_all_tabs_to_the_left()

    def make_undock(self):
        """Undock Tab from TabWidget to a Dialog,if theres more than 2 Tabs."""
        msg = "<b>Needs more than 2 Tabs to allow Un-Dock Tabs !."
        return self.parent.make_undock() if self.count(
            ) > 2 else QMessageBox.warning(self, "Error", msg)

    def set_shape(self):
        """Handle set Shape on Tabs."""
        self.parent.setTabShape(0 if self.parent.tabShape() else 1)

    def set_position(self):
        """Handle set Position on Tabs."""
        self.parent.setTabPosition(0 if self.parent.tabPosition() else 1)

    def set_text(self):
        """Handle set Text on Tabs."""
        text = str(QInputDialog.getText(
            self, "Tab Options Dialog", "<b>Type Tab Text:",
            text=self.tabText(self.currentIndex()))[0]).strip()[:50]
        if text:
            self.setTabText(self.currentIndex(), text)

    def set_color(self):
        """Handle set Colors on Tabs."""
        color = QColorDialog.getColor()
        if color:
            self.setTabTextColor(self.currentIndex(), color)

    def set_pinned(self):
        """Handle Pin and Unpin Tabs."""
        index = self.currentIndex()
        if self.tabText(index) == "":
            self.setTabText(index, self.tabToolTip(index))
            self.tabButton(index, 1).show()
        else:
            self.setTabToolTip(index, self.tabText(index))
            self.setTabText(index, "")
            self.tabButton(index, 1).hide()

    def build_submenu(self):
        """Handle build a sub-menu on the fly with the list of tabs."""
        self.submenu.clear()
        self.submenu.addAction("Tab list").setDisabled(True)
        for index in tuple(range(self.count())):
            action = self.submenu.addAction("Tab {0}".format(index + 1))
            action.triggered.connect(
                lambda _, index=index: self.setCurrentIndex(index))

    def set_limit(self):
        """Limit the Maximum number of Tabs that can coexist, TBD by Dev."""
        limit = int(QInputDialog.getInt(
            self, "Tab Options Dialog", "<b>How many Tabs is the Maximum ?:",
            self.count() * 2, self.count() * 2, 99)[0])
        if limit:
            self.limit = limit
            return limit


class TabWidget(QTabWidget):

    """Custom tab widget."""

    def __init__(self, parent=None, *args, **kwargs):
        """Init class custom tab widget."""
        super(TabWidget, self).__init__(parent=None, *args, **kwargs)
        self.parent, self.previews, self.timer = parent, [], QTimer(self)
        self.fader, self.previous_pic = FaderWidget(self), None
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: [_.close() for _ in self.previews])
        self.setTabBar(TabBar(self))
        self.setMovable(False)
        self.setTabsClosable(True)
        self.setTabShape(QTabWidget.Triangular)
        self.addtab, self.menu_0 = QToolButton(self), QToolButton(self)
        self.addtab.setText(" + ")
        self.addtab.setToolTip("<b>Add Tabs")
        self.menu_0.setText(" ? ")
        self.menu_0.setToolTip("<b>Menu")
        font = self.addtab.font()
        font.setBold(True)
        self.addtab.setFont(font)
        self.menu_0.setFont(font)
        # self.addtab.clicked.connect(self.addTab)
        # self.menu_0.clicked.connect(self.show_menu)
        self.setCornerWidget(self.addtab, 1)
        self.setCornerWidget(self.menu_0, 0)

##############################################################################

if __name__ in '__main__':
    from PyQt5.QtWidgets import QApplication, QCalendarWidget
    app = QApplication([])
    gui = TabWidget()
    for i in range(9):
        gui.addTab(QLabel("<center><h1 style='color:red'>Tab {0} !".format(i))
                   if i % 2 else QCalendarWidget(), " Tab {0} ! ".format(i))
    gui.show()
exit(app.exec_())
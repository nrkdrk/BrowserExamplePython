#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 2.7.10 IlBilge Anadolu web browser
# Developer Berk Can

from PyQt4 import QtCore, QtGui, QtWebKit
import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QTabBar, QMenu, QCursor, QInputDialog, QColorDialog
from PyQt4.QtNetwork import QNetworkAccessManager, QSslConfiguration, QSsl

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        QtGui.QWidget.__init__(self)
        widget = QtGui.QTabWidget(self)
        self.setCentralWidget(widget)

        tab_widget = QtGui.QTabWidget(self)
        tab_widget.setTabBar(TabBar(self))
        tabs = []
        p_vertical = []
        tab_widget.setTabShape(0 if tab_widget.tabShape() else 1)
        #tab_widget.setTabPosition(0 if tab_widget.tabPosition() else 1)

        def adder(self):
            if len(tabs) < 10 or True:
                tabs.append(tabber())
                l = len(tabs)
                p_vertical.append(QtGui.QVBoxLayout(tabs[-1]))
                tab_widget.addTab(tabs[-1], 'Yeni Sekme')
                tab_widget.setCurrentIndex((l - 1))

        def remover(self):
            if len(tabs) > 1:
                ind = tab_index()
                tabs.pop(ind)
                p_vertical.pop(ind)
                tab_widget.removeTab(ind)


        tabButton = QtGui.QToolButton(self)
        tabButton.setText('+')
        font = tabButton.font()
        font.setBold(True)
        tabButton.setFont(font)
        tab_widget.setCornerWidget(tabButton)
        tabButton.clicked.connect(adder)

        def tabber():

            fin_url = ''

            def TabLabel0():
                print ''

            def TabLabel(t):
                if t == True and not webView.title() == '':
                    ind = tab_widget.currentIndex()
                    tab_widget.setTabText(ind, webView.title())

            def UrlChanged(url):
                ind = tab_index()
                tb_url.setText(url.toString())
                # tab_widget.setTabText(ind,html.title())
                load_prog.setValue(0)
                webView.load(QtCore.QUrl(tb_url.text()))
                webView.show()

            def FinalUrlChanged(url):
                ind = tab_index()
                tb_url.setText(url.toString())
                tab_widget.setTabText(ind, webView.title())
                load_prog.setValue(100)

            tabcentral = QtGui.QWidget()
            tabframe = QtGui.QFrame(tabcentral)
            tabgrid = QtGui.QVBoxLayout(tabframe)
            tabgrid.setMargin(0)
            tabgrid.setSpacing(0)
            tabmain = QtGui.QHBoxLayout(tabcentral)
            tabmain.setSpacing(0)
            tabmain.setMargin(0)

            tb_url = QtGui.QLineEdit(tabframe)

            bt_back = QtGui.QPushButton(tabframe)
            bt_ahead = QtGui.QPushButton(tabframe)
            bt_refresh = QtGui.QPushButton(tabframe)
            bt_stop = QtGui.QPushButton(tabframe)
            bt_go = QtGui.QPushButton(tabframe)
            bt_downloaded = QtGui.QPushButton(tabframe)
            bt_home = QtGui.QPushButton(tabframe)
            bt_menu = QtGui.QPushButton(tabframe)
            bt_favorites = QtGui.QPushButton(tabframe)

            bt_back.setIcon(QtGui.QIcon().fromTheme("go-previous"))
            bt_ahead.setIcon(QtGui.QIcon().fromTheme("go-next"))
            bt_refresh.setIcon(QtGui.QIcon().fromTheme("gtk-refresh"))
            bt_stop.setIcon(QtGui.QIcon().fromTheme("gtk-cancel"))
            bt_go.setIcon(QtGui.QIcon().fromTheme("stock_search"))
            bt_downloaded.setIcon(QtGui.QIcon().fromTheme("go-down"))
            bt_home.setIcon(QtGui.QIcon().fromTheme("go-home"))
            bt_menu.setIcon(QtGui.QIcon().fromTheme("format-justify-fill"))
            bt_favorites.setIcon(QtGui.QIcon().fromTheme("bookmark-new"))



            tab_widget.tabCloseRequested.connect(remover)
            tab_widget.setTabsClosable(True)
            load_prog = QtGui.QProgressBar()
            load_prog.setGeometry(10, 80, 20, 20)
            load_prog.setFixedWidth(80)
            address_area = QtGui.QHBoxLayout()
            address_area.addWidget(bt_back)
            address_area.addWidget(bt_ahead)
            address_area.addWidget(bt_refresh)
            address_area.addWidget(bt_stop)
            address_area.addWidget(tb_url)
            address_area.addWidget(bt_go)
            address_area.addWidget(bt_favorites)
            address_area.addWidget(load_prog)
            address_area.addWidget(bt_downloaded)
            address_area.addWidget(bt_home)
            address_area.addWidget(bt_menu)
            tabgrid.addLayout(address_area)
            webView = QtWebKit.QWebView()


            bt_go.hide()
            load_prog.hide()

            webView.page().setLinkDelegationPolicy(QtWebKit.QWebPage.DelegateAllLinks)
            webView.connect(webView, QtCore.SIGNAL("linkClicked(const QUrl&)"), UrlChanged)
            webView.connect(webView, QtCore.SIGNAL("loadStarted()"), TabLabel0)
            webView.connect(webView, QtCore.SIGNAL("loadFinished(bool)"), TabLabel)
            webView.connect(webView, QtCore.SIGNAL("urlChanged(const QUrl&)"), FinalUrlChanged)
            tabgrid.addWidget(webView)################################
            tabmain.addWidget(tabframe)

            default_url = "www.google.com"

            def browse():
                curl = tb_url.text() if tb_url.text() else default_url
                if curl == default_url:
                    url = 'http://' + default_url
                else:
                    purl = curl
                    purl = curl.split(' ')
                    print purl
                    if len(purl) == 1 and '.' in curl:
                        if not curl[:7] == 'http://':
                            url = 'http://' + curl
                    else:
                        url = 'http://www.google.co.in/?client=ubuntu#channel=fs&q=' + purl[0]
                        for i in range(1, len(purl)):
                            url += str('+' + purl[i])
                webView.load(QtCore.QUrl.fromUserInput(tb_url.text()))
                webView.show()
                TabLabel(True)

            def browsehome():
                webView.load(QtCore.QUrl.fromUserInput("www.google.com"))
                webView.show()
                TabLabel(True)

            bt_home.clicked.connect(browsehome)

            tabmain.connect(tb_url, QtCore.SIGNAL("returnPressed()"), browse)
            tabmain.connect(bt_go, QtCore.SIGNAL("clicked()"), browse)
            tabmain.connect(bt_back, QtCore.SIGNAL("clicked()"), webView.back)
            tabmain.connect(bt_ahead, QtCore.SIGNAL("clicked()"), webView.forward)
            tabmain.connect(bt_refresh, QtCore.SIGNAL("clicked()"), webView.reload)
            tabmain.connect(bt_stop, QtCore.SIGNAL("clicked()"), webView.stop)
            tb_url.setText(default_url)
            browse()
            return tabcentral

        tabs.append(tabber())

        p_vertical.append(QtGui.QVBoxLayout(tabs[-1]))
        tab_widget.addTab(tabs[-1], 'Yeni Sekme')

        def tab_index():
            curr = tab_widget.currentIndex()
            return curr

        vbox = QtGui.QVBoxLayout()
        vbox.setMargin(1)
        vbox.addWidget(tab_widget)
        widget.setLayout(vbox)

        self.createActions()
        self.createMenus()

        message = "IlBilge Anadolu Milli Tarayici"
        self.statusBar().showMessage(message)

        self.setGeometry(0, 0, 500, 650)
        self.setWindowTitle("IlBilge | Anadolu")
        self.resize(800, 600)
        self.setMinimumSize(500, 650)
        app_icon = QtGui.QIcon()
        app_icon.addFile('safari.svg', QtCore.QSize(16, 16))
        app_icon.addFile('safari.svg', QtCore.QSize(24, 24))
        app_icon.addFile('safari.svg', QtCore.QSize(32, 32))
        app_icon.addFile('safari.svg', QtCore.QSize(48, 48))
        app_icon.addFile('safari.svg', QtCore.QSize(256, 256))
        self.setWindowIcon(app_icon)

    def contextMenuEvent(self, event):
        menu = QtGui.QMenu(self)
        menu.addAction(self.cutAct)
        menu.addAction(self.copyAct)
        menu.addAction(self.pasteAct)
        menu.exec_(event.globalPos())

    def newTab(self):
        self.infoLabel.setText("Invoked <b>File|Open</b>")

    def newWindow(self):
        self.infoLabel.setText("Invoked <b>File|Open</b>")

    def newHiddenWindow(self):
        self.infoLabel.setText("Invoked <b>File|Save</b>")

    def print_(self):
        self.infoLabel.setText("Invoked <b>File|Print</b>")

    def undo(self):
        self.infoLabel.setText("Invoked <b>Edit|Undo</b>")

    def redo(self):
        self.infoLabel.setText("Invoked <b>Edit|Redo</b>")

    def cut(self):
        self.infoLabel.setText("Invoked <b>Edit|Cut</b>")

    def copy(self):
        self.infoLabel.setText("Invoked <b>Edit|Copy</b>")

    def paste(self):
        self.infoLabel.setText("Invoked <b>Edit|Paste</b>")

    def bold(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Bold</b>")

    def italic(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Italic</b>")

    def leftAlign(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Left Align</b>")

    def rightAlign(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Right Align</b>")

    def justify(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Justify</b>")

    def center(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Center</b>")

    def setLineSpacing(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Line Spacing</b>")

    def setParagraphSpacing(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Paragraph Spacing</b>")

    def about(self):
        QtGui.QMessageBox.about(self, "IlBilge Anadolu",
                                "<b>Ozgur yazilim kullanicilari dernegi</b> "
                                "(OYAKDER) tarafindan gelistirilen milli bir tarayicidir.")

    def downloaded(self):
        QtGui.QMessageBox.about(self, "Ind",
                                "<b>Ozgur yazilim kullanicilari dernegi</b> "
                                "(OYAKDER) tarafindan gelistirilen milli bir tarayicidir.")
    def bookMarks(self):
        QtGui.QMessageBox.about(self, "Yer imleri")

    def aboutQt(self):
        QtGui.QMessageBox.about(self, "Oyakder",
                                "<b>Ozgur yazilim kullanicilari dernegi</b> "
                                "(OYAKDER) sitesi, ALASTYR sunucularinda "
                                "barindirilmaktadir. OYAKDER olarak hedefimiz, "
                                "ulkemizde faaliyet gosteren ozgurr yazilim ve acık "
                                "kaynak topluluklarini-guruplarini bir catı altinda "
                                "toplamak, topluluklar-guruplar arasinda kopru vazifesini"
                                " ustlenerek is birlikteliklerini gelistirmek ve birlikte "
                                "kamu yararina projeler yapmaktır. OYAKDER, bu hedefler"
                                " dogrultusunda kamu yararina projeler yapmayi "
                                "ve bu projelerin basarili seklide sonuslanmasi"
                                " icin yazilim gelistirme, teknik destek ve "
                                "egitim yapilarini olusturmak suretiyle,"
                                " ulkemizde ozgur yazilima yon vermeyi amac e"
                                "dinmistir.Site ve forum icerisinde yer alan "
                                "tum icerik Creative Commons 3.0 (by-sa) ile "
                                "lisanslanmistir.")

    def createActions(self):
        self.newAct = QtGui.QAction("&Yeni Sekme", self,
                                    shortcut="Ctrl+T",
                                    statusTip="Create a new file", triggered=self.newTab)

        self.openAct = QtGui.QAction("&Yeni Pencere", self,
                                     shortcut="Ctrl+N",
                                     statusTip="Open an existing file", triggered=self.newWindow)

        self.saveAct = QtGui.QAction("&Yeni Gizli Pencere", self,
                                     shortcut="Shift+Ctrl+Q",
                                     statusTip="Save the document to disk", triggered=self.newHiddenWindow)

        self.printAct = QtGui.QAction("&Yazdir", self,
                                      shortcut=QtGui.QKeySequence.Print,
                                      statusTip="Print the document", triggered=self.print_)

        self.exitAct = QtGui.QAction("Cikis", self, shortcut="Ctrl+Q",
                                     statusTip="Exit the application", triggered=self.close)

        self.undoAct = QtGui.QAction("&Geri Al", self,
                                     shortcut=QtGui.QKeySequence.Undo,
                                     statusTip="Undo the last operation", triggered=self.undo)

        self.redoAct = QtGui.QAction("&Yenile", self,
                                     shortcut=QtGui.QKeySequence.Redo,
                                     statusTip="Redo the last operation", triggered=self.redo)

        self.cutAct = QtGui.QAction("Kes", self,
                                    shortcut=QtGui.QKeySequence.Cut,
                                    statusTip="Cut the current selection's contents to the clipboard",
                                    triggered=self.cut)

        self.copyAct = QtGui.QAction("&Kopyala", self,
                                     shortcut=QtGui.QKeySequence.Copy,
                                     statusTip="Copy the current selection's contents to the clipboard",
                                     triggered=self.copy)

        self.pasteAct = QtGui.QAction("&Yapistir", self,
                                      shortcut=QtGui.QKeySequence.Paste,
                                      statusTip="Paste the clipboard's contents into the current selection",
                                      triggered=self.paste)

        self.boldAct = QtGui.QAction("&Bold", self, checkable=True,
                                     shortcut="Ctrl+B", statusTip="Make the text bold",
                                     triggered=self.bold)

        boldFont = self.boldAct.font()
        boldFont.setBold(True)
        self.boldAct.setFont(boldFont)

        self.italicAct = QtGui.QAction("&Italic", self, checkable=True,
                                       shortcut="Ctrl+I", statusTip="Make the text italic",
                                       triggered=self.italic)

        italicFont = self.italicAct.font()
        italicFont.setItalic(True)
        self.italicAct.setFont(italicFont)

        self.setLineSpacingAct = QtGui.QAction("Set &Line Spacing...", self,
                                               statusTip="Change the gap between the lines of a paragraph",
                                               triggered=self.setLineSpacing)

        self.setParagraphSpacingAct = QtGui.QAction(
            "Set &Paragraph Spacing...", self,
            statusTip="Change the gap between paragraphs",
            triggered=self.setParagraphSpacing)

        self.aboutAct = QtGui.QAction("&Hakkinda", self,
                                      statusTip="Show the application's About box",
                                      triggered=self.about)

        self.downloadedAct = QtGui.QAction("&Indirilenler", self,
                                      statusTip="Show the application's About box",
                                      triggered=self.downloaded)

        self.allHistoryAct = QtGui.QAction("&Tum gecmisi goster", self,
                                      statusTip="Show the application's About box",
                                      triggered=self.downloaded)

        self.clearRecentPastAct = QtGui.QAction("&Yakin gecmisi temizle", self,
                                      statusTip="Show the application's About box",
                                      triggered=self.downloaded)

        self.bookMarksAct = QtGui.QAction("&Tum yer imlerini goster", self,
                                      statusTip="Show the application's About box",
                                      triggered=self.downloaded)

        self.aboutQtAct = QtGui.QAction("Oyakder Hakkinda", self,
                                        statusTip="Show the Qt library's About box",
                                        triggered=self.aboutQt)

        self.leftAlignAct = QtGui.QAction("&Left Align", self, checkable=True,
                                          shortcut="Ctrl+L", statusTip="Left align the selected text",
                                          triggered=self.leftAlign)

        self.rightAlignAct = QtGui.QAction("&Right Align", self,
                                           checkable=True, shortcut="Ctrl+R",
                                           statusTip="Right align the selected text",
                                           triggered=self.rightAlign)

        self.justifyAct = QtGui.QAction("&Justify", self, checkable=True,
                                        shortcut="Ctrl+J", statusTip="Justify the selected text",
                                        triggered=self.justify)

        self.centerAct = QtGui.QAction("&Center", self, checkable=True,
                                       shortcut="Ctrl+C", statusTip="Center the selected text",
                                       triggered=self.center)

        self.alignmentGroup = QtGui.QActionGroup(self)
        self.alignmentGroup.addAction(self.leftAlignAct)
        self.alignmentGroup.addAction(self.rightAlignAct)
        self.alignmentGroup.addAction(self.justifyAct)
        self.alignmentGroup.addAction(self.centerAct)
        self.leftAlignAct.setChecked(True)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&Dosya")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu("&Duzen")
        self.editMenu.addAction(self.undoAct)
        self.editMenu.addAction(self.redoAct)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)
        self.editMenu.addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Gecmis")
        self.helpMenu.addAction(self.allHistoryAct)
        self.helpMenu.addAction(self.clearRecentPastAct)

        self.helpMenu = self.menuBar().addMenu("&Yer imleri")
        self.helpMenu.addAction(self.bookMarksAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.helpMenu = self.menuBar().addMenu("&Araclar")
        self.helpMenu.addAction(self.downloadedAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.helpMenu = self.menuBar().addMenu("&Yardim")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.formatMenu = self.editMenu.addMenu("&Format")
        self.formatMenu.addAction(self.boldAct)
        self.formatMenu.addAction(self.italicAct)
        self.formatMenu.addSeparator().setText("Alignment")
        self.formatMenu.addAction(self.leftAlignAct)
        self.formatMenu.addAction(self.rightAlignAct)
        self.formatMenu.addAction(self.justifyAct)
        self.formatMenu.addAction(self.centerAct)
        self.formatMenu.addSeparator()
        self.formatMenu.addAction(self.setLineSpacingAct)
        self.formatMenu.addAction(self.setParagraphSpacingAct)

class TabBar(QTabBar):

    """Custom tab bar."""

    def __init__(self, parent=None, *args, **kwargs):
        """Init class custom tab bar."""
        super(TabBar, self).__init__(parent=None, *args, **kwargs)
        self.parent, self.limit = parent, self.count() * 2
        self.menu, self.submenu = QMenu("Tab Options"), QMenu("Tabs")
        self.tab_previews = True
        self.menu.addAction("Sekme Menusu").setDisabled(True)
        self.menu.addSeparator()
        self.menu.addAction("Sekme Adini Duzenle", self.set_text)
        self.menu.addAction("Sekme Rengini Duzenle", self.set_color)
        self.menu.addAction("Sekme Limitini Belirle", self.set_limit)
        self.menu.addSeparator()
        #self.menu.addAction("Sekme Tarzini Degistir", self.set_shape)
        self.menu.addAction("Sekme Barinin Pozisyonunu Degistir", self.set_position)
        self.menu.addAction("Sekme Bilgisini Gizle", self.set_pinned)
        self.menu.addSeparator()
        self.menu.addAction("Bu Sekmeyi Kapat",
                            lambda: self.removeTab(self.currentIndex()))
        self.menu.addAction("Sagdaki Tum Sekmeleri Kapat",
                            self.close_all_tabs_to_the_right)
        self.menu.addAction("Soldaki Tum Sekmeleri Kapat",
                            self.close_all_tabs_to_the_left)
        self.menu.addAction("Tum Sekmeleri Kapat", self.close_all_other_tabs)
        self.menu.addSeparator()
        self.tabCloseRequested.connect(
            lambda: self.removeTab(self.currentIndex()))
        self.setMouseTracking(True)
        self.installEventFilter(self)

    def contextMenuEvent(self, event):
        """Handle double click."""
        self.menu.exec_(QCursor.pos())

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

    def set_limit(self):
        """Limit the Maximum number of Tabs that can coexist, TBD by Dev."""
        limit = int(QInputDialog.getInt(
            self, "Maksimum Sekme", "<b>Maksimum Kaç sekme ?:",
            self.count() * 2, self.count() * 2, 99)[0])
        if limit:
            self.limit = limit
            return limit

def main():
    app = QtGui.QApplication(sys.argv)
    frame = MainWindow()
    frame.showMaximized()
    frame.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
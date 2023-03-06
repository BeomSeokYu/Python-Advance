import sys
import os
import pickle
from tkinter import dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

""" os에서의 절대 경로 획득 """
if getattr(sys, 'frozen', False):
    # exe로 실행한 경우, exe를 보관한 디렉토리의 full path를 취득
    CUR_PATH = os.path.dirname(os.path.abspath(sys.executable))
else:
    # py로 실행한 경우, py를 보관한 디렉토리의 full path를 취득
    CUR_PATH = os.path.dirname(os.path.abspath(__file__))
# 이 파일(py)이 있는 디렉토리의 절대 경로
# CUR_PATH = os.path.dirname(os.path.realpath(__file__))
# pickle 파일이 저장되는 장소
DATA_FOLDER_PATH = CUR_PATH + '\\' + 'DataFile'

""" 변수 """
ver = "v0.2"

wp = [2, 4, 3]

scoreKey =  {0:"고라파덕", 1:"귀조심", 2:"민머리", 3:"정고", 4:"재민",
             5:"차재",     6:"초코동", 7:"Hihat", 8:"hihi", 9:"Guest1",
             10:"Guest2", 11:"Guest3", 12:"Guest4", 13:"Guest5", 14:"Guest6"}
score =     {"고라파덕":0, "귀조심":0, "민머리":0, "정고":0, "재민":0,
             "차재":0, "초코동":0, "Hihat":0, "hihi":0, "Guest1":0,
             "Guest2":0, "Guest3":0, "Guest4":0, "Guest5":0, "Guest6":0}
cumulative_score = {"고라파덕":0, "귀조심":0, "민머리":0, "정고":0, "재민":0,
                    "차재":0, "초코동":0, "Hihat":0, "hihi":0, "Guest1":0,
                    "Guest2":0, "Guest3":0, "Guest4":0, "Guest5":0, "Guest6":0}
yacht = []
record = []

msg = ""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 메인 윈도우 창 설정 (최상위 창)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setMinimumSize(QtCore.QSize(300, 470))
        MainWindow.setMaximumSize(QtCore.QSize(9999, 9999))
        MainWindow.setIconSize(QtCore.QSize(24, 24))

        # 메인 윈도우에 위젯 및 텝 추가
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DigLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.DigLayout.setObjectName("DigLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.DigLayout_tap = QtWidgets.QVBoxLayout(self.tab1)
        self.DigLayout_tap.setObjectName("DigLayout_tap")
        
        """ 첫번째 탭 (구스구스덕) """
        # 승리 플레이어 그룹 박스
        self.groupBox_p = QtWidgets.QGroupBox(self.tab1)
        self.groupBox_p.setObjectName("groupBox_p")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_p)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 2, 4, 1, 1)
        self.pushButton_duck = QtWidgets.QPushButton(self.groupBox_p)
        self.pushButton_duck.setObjectName("pushButton_duck")
        self.pushButton_duck.setStyleSheet('color:white; background:red')
        self.pushButton_duck.clicked.connect(self.AddDuckScore)
        self.gridLayout.addWidget(self.pushButton_duck, 5, 5, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 2, 1, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 0, 6, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 4, 1, 1)
        self.pushButton_neutrality = QtWidgets.QPushButton(self.groupBox_p)
        self.pushButton_neutrality.setObjectName("pushButton_neutrality")
        self.pushButton_neutrality.setStyleSheet('color:blue; background:yellow')
        self.pushButton_neutrality.clicked.connect(self.AddNeutralityScore)
        self.gridLayout.addWidget(self.pushButton_neutrality, 5, 4, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 2, 6, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 3, 1, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 3, 3, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout.addWidget(self.checkBox_13, 3, 4, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout.addWidget(self.checkBox_14, 3, 5, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout.addWidget(self.checkBox_15, 3, 6, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 0, 5, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 2, 3, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 3, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_p)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 2, 5, 1, 1)
        self.pushButton_goose = QtWidgets.QPushButton(self.groupBox_p)
        self.pushButton_goose.setObjectName("pushButton_goose")
        self.pushButton_goose.setStyleSheet('color:black; background:white')
        self.pushButton_goose.clicked.connect(self.AddGooseScore)
        self.gridLayout.addWidget(self.pushButton_goose, 5, 3, 1, 1)
        self.Label1_Empty = QtWidgets.QLabel(self.groupBox_p)
        self.Label1_Empty.setText("")
        self.Label1_Empty.setObjectName("Label1_Empty")
        self.gridLayout.addWidget(self.Label1_Empty, 4, 4, 1, 1)
        self.DigLayout_tap.addWidget(self.groupBox_p)
        # 경기 기록 그룹 박스
        self.groupBox_hist = QtWidgets.QGroupBox(self.tab1)
        self.groupBox_hist.setObjectName("groupBox_hist")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_hist)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_hist)
        self.listWidget.setObjectName("listWidget")
        self.pushButton_remove = QtWidgets.QPushButton()
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.pushButton_remove.clicked.connect(self.ItemRemove)
        self.pushButton_clear = QtWidgets.QPushButton()
        self.pushButton_clear.setObjectName("pushButton_remove")
        self.pushButton_clear.clicked.connect(self.ItemClear)
        self.gridLayout_2.addWidget(self.listWidget, 1, 1, 1, 2)
        self.gridLayout_2.addWidget(self.pushButton_remove, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.pushButton_clear, 2, 2, 1, 1)
        self.DigLayout_tap.addWidget(self.groupBox_hist)
        # 스코어 그룹 박스
        self.groupBox_score = QtWidgets.QGroupBox(self.tab1)
        self.groupBox_score.setObjectName("groupBox_score")
        self.vertical_groupBox_score = QtWidgets.QVBoxLayout(self.groupBox_score)
        self.vertical_groupBox_score.setObjectName("vertical_groupBox_score")
        self.scrollArea_score = QtWidgets.QScrollArea(self.groupBox_score)
        self.scrollArea_score.setWidgetResizable(True)
        self.scrollArea_score.setObjectName("scrollArea_score")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.RankingLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.RankingLayout.setObjectName("RankingLayout")
        self.Label1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label1.setObjectName("Label1")
        self.Label2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label2.setObjectName("Label2")
        self.Label3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label3.setObjectName("Label3")
        self.Label4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label4.setObjectName("Label4")
        self.Label5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label5.setObjectName("Label5")
        self.Label6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label6.setObjectName("Label6")
        self.Label7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label7.setObjectName("Label7")
        self.Label8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label8.setObjectName("Label8")
        self.Label9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label9.setObjectName("Label9")
        self.Label10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label10.setObjectName("Label10")
        self.Label11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label11.setObjectName("Label11")
        self.Label12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label12.setObjectName("Label12")
        self.Label13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label13.setObjectName("Label13")
        self.Label14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label14.setObjectName("Label14")
        self.Label15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label15.setObjectName("Label15")
        self.Label16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label16.setObjectName("Label16")
        self.Label17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label17.setObjectName("Label17")
        self.Label18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label18.setObjectName("Label18")
        self.Label19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label19.setObjectName("Label19")
        self.Label20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label20.setObjectName("Label20")
        self.Label21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label21.setObjectName("Label21")
        self.Label22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label22.setObjectName("Label22")
        self.Label23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label23.setObjectName("Label23")
        self.Label24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label24.setObjectName("Label24")
        self.Label25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label25.setObjectName("Label25")
        self.Label26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label26.setObjectName("Label26")
        self.Label27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label27.setObjectName("Label27")
        self.Label28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label28.setObjectName("Label28")
        self.Label29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label29.setObjectName("Label29")
        self.Label30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label30.setObjectName("Label30")
        self.Label01 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label01.setObjectName("Label01")
        self.Label02 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label02.setObjectName("Label02")
        self.Label03 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label03.setObjectName("Label03")
        self.Label04 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label04.setObjectName("Label04")
        self.Label05 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label05.setObjectName("Label05")
        self.Label06 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label06.setObjectName("Label06")
        self.Label07 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label07.setObjectName("Label07")
        self.Label08 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label08.setObjectName("Label08")
        self.Label09 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label09.setObjectName("Label09")
        self.Label010 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label010.setObjectName("Label010")
        self.Label011 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label011.setObjectName("Label011")
        self.Label012 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label012.setObjectName("Label012")
        self.Label013 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label013.setObjectName("Label013")
        self.Label014 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label014.setObjectName("Label014")
        self.Label015 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label015.setObjectName("Label015")
        self.Label016 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label016.setObjectName("Label016")
        self.Label017 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label017.setObjectName("Label017")
        self.Label018 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label018.setObjectName("Label018")
        self.Label019 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label019.setObjectName("Label019")
        self.Label020 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label020.setObjectName("Label020")
        self.Label021 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label021.setObjectName("Label021")
        self.Label022 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label022.setObjectName("Label022")
        self.Label023 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label023.setObjectName("Label023")
        self.Label024 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label024.setObjectName("Label024")
        self.Label025 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label025.setObjectName("Label025")
        self.Label026 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label026.setObjectName("Label026")
        self.Label027 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label027.setObjectName("Label027")
        self.Label028 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label028.setObjectName("Label028")
        self.Label029 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label029.setObjectName("Label029")
        self.Label030 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label030.setObjectName("Label030")
        self.Label1.setStyleSheet("Color : red")
        self.Label16.setStyleSheet("Color : red")
        self.RankingLayout.addWidget(self.Label1, 0, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label2, 1, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label3, 2, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label4, 3, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label5, 4, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label6, 5, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label7, 6, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label8, 7, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label9, 8, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label10, 9, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label11, 10, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label12, 11, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label13, 12, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label14, 13, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label15, 14, 0, 1, 1)
        self.RankingLayout.addWidget(self.Label16, 0, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label17, 1, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label18, 2, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label19, 3, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label20, 4, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label21, 5, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label22, 6, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label23, 7, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label24, 8, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label25, 9, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label26, 10, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label27, 11, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label28, 12, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label29, 13, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label30, 14, 3, 1, 1)
        self.RankingLayout.addWidget(self.Label01, 0, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label02, 1, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label03, 2, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label04, 3, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label05, 4, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label06, 5, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label07, 6, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label08, 7, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label09, 8, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label010, 9, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label011, 10, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label012, 11, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label013, 12, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label014, 13, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label015, 14, 2, 1, 1)
        self.RankingLayout.addWidget(self.Label016, 0, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label017, 1, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label018, 2, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label019, 3, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label020, 4, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label021, 5, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label022, 6, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label023, 7, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label024, 8, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label025, 9, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label026, 10, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label027, 11, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label028, 12, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label029, 13, 4, 1, 1)
        self.RankingLayout.addWidget(self.Label030, 14, 4, 1, 1)
        self.scrollArea_score.setWidget(self.scrollAreaWidgetContents)
        self.vertical_groupBox_score.addWidget(self.scrollArea_score)
        self.DigLayout_tap.addWidget(self.groupBox_score)
        self.tabWidget.addTab(self.tab1, "")
        
        """ 두번째 탭 (야추의 전당) """
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")        
        self.gridLayout_tap2 = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout_tap2.setObjectName("gridLayout_tap2")
        # 야추 전당 플레이어
        self.groupBox_hof = QtWidgets.QGroupBox(self.tab2)
        self.DigLayout_groupbox_hof = QtWidgets.QVBoxLayout(self.groupBox_hof)
        self.DigLayout_groupbox_hof.setObjectName("DigLayout_groupbox_hof")
        self.label_mythic = QtWidgets.QLabel(self.groupBox_hof)
        self.label_mythic.setObjectName("label_mythic")
        self.label_mythic.setFont(QtGui.QFont("고딕",20))
        self.label_mythic.setStyleSheet("Color : pink; background:gray")
        self.label_mythic.setMargin(10)
        self.DigLayout_groupbox_hof.addWidget(self.label_mythic)
        self.label_legend = QtWidgets.QLabel(self.groupBox_hof)
        self.label_legend.setObjectName("label_legend")
        self.label_legend.setFont(QtGui.QFont("고딕",15))
        self.label_legend.setStyleSheet("Color : orange; background:gray")
        self.label_legend.setMargin(10)
        self.DigLayout_groupbox_hof.addWidget(self.label_legend)
        self.label_unique = QtWidgets.QLabel(self.groupBox_hof)
        self.label_unique.setObjectName("label_unique")
        self.label_unique.setFont(QtGui.QFont("고딕",10))
        self.label_unique.setStyleSheet("Color : yellow; background:gray")
        self.label_unique.setMargin(10)
        self.DigLayout_groupbox_hof.addWidget(self.label_unique)
        self.gridLayout_tap2.addWidget(self.groupBox_hof, 2, 0, 2, 1)
        self.groupBox_wp = QtWidgets.QGroupBox(self.tab2)
        self.groupBox_wp.setObjectName("groupBox_wp")
        self.gridLayout_groupbox_wp = QtWidgets.QGridLayout(self.groupBox_wp)
        self.gridLayout_groupbox_wp.setObjectName("gridLayout_groupbox_wp")
        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox_wp)
        self.radioButton_11.setObjectName("radioButton_11")
        self.gridLayout_groupbox_wp.addWidget(self.radioButton_11, 2, 4, 1, 1)
        self.pushButton_reg = QtWidgets.QPushButton(self.groupBox_wp)
        self.pushButton_reg.setObjectName("pushButton_reg")
        self.pushButton_reg.clicked.connect(self.HallOfFame)
        self.gridLayout_groupbox_wp.addWidget(self.pushButton_reg, 4, 7, 1, 1)
        self.radioButton_19 = QtWidgets.QRadioButton(self.groupBox_wp)
        self.radioButton_19.setObjectName("radioButton_19")
        self.gridLayout_groupbox_wp.addWidget(self.radioButton_19, 0, 3, 1, 1)
        self.radioButton_20 = QtWidgets.QRadioButton(self.groupBox_wp)
        self.radioButton_20.setObjectName("radioButton_20")
        self.gridLayout_groupbox_wp.addWidget(self.radioButton_20, 2, 6, 1, 1)
        self.radioButton_17 = QtWidgets.QRadioButton(self.groupBox_wp)
        self.radioButton_17.setObjectName("radioButton_17")
        self.gridLayout_groupbox_wp.addWidget(self.radioButton_17, 2, 3, 1, 1)
        self.radioButton_18 = QtWidgets.QRadioButton(self.groupBox_wp)
        self.radioButton_18.setObjectName("radioButton_18")
        self.gridLayout_groupbox_wp.addWidget(self.radioButton_18, 0, 1, 1, 1)
        self.radioButton_16 = QtWidgets.QRadioButton(self.groupBox_wp)
        self.radioButton_16.setObjectName("radioButton_16")
        self.gridLayout_groupbox_wp.addWidget(self.radioButton_16, 0, 6, 1, 1)
        self.radioButton_13 = QtWidgets.QRadioButton(self.groupBox_wp)
        self.radioButton_13.setObjectName("radioButton_13")
        self.gridLayout_groupbox_wp.addWidget(self.radioButton_13, 0, 7, 1, 1)
        self.radioButton_14 = QtWidgets.QRadioButton(self.groupBox_wp)
        self.radioButton_14.setObjectName("radioButton_14")
        self.gridLayout_groupbox_wp.addWidget(self.radioButton_14, 0, 4, 1, 1)
        self.radioButton_15 = QtWidgets.QRadioButton(self.groupBox_wp)
        self.radioButton_15.setObjectName("radioButton_15")
        self.gridLayout_groupbox_wp.addWidget(self.radioButton_15, 2, 7, 1, 1)
        self.radioButton_12 = QtWidgets.QRadioButton(self.groupBox_wp)
        self.radioButton_12.setObjectName("radioButton_12")
        self.gridLayout_groupbox_wp.addWidget(self.radioButton_12, 2, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_wp)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(9999)
        self.gridLayout_groupbox_wp.addWidget(self.spinBox, 4, 6, 1, 1)
        self.label_score = QtWidgets.QLabel(self.groupBox_wp)
        self.label_score.setObjectName("label_score")
        self.gridLayout_groupbox_wp.addWidget(self.label_score, 4, 4, 1, 1)
        self.gridLayout_tap2.addWidget(self.groupBox_wp, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab2, "")
        self.DigLayout.addWidget(self.tabWidget)
        # 메인창의 상태바 메뉴바 설정
        self.setting = QtWidgets.QAction('설정')
        self.setting.setShortcut('Ctrl+E')
        self.setting.setStatusTip("Setting")
        self.setting.triggered.connect(self.Setting)
        self.info = QtWidgets.QAction('정보')
        self.info.setShortcut('Ctrl+I')
        self.info.setStatusTip("Info")
        self.info.triggered.connect(self.Info)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setNativeMenuBar(False)
        self.filemenu = self.menubar.addMenu('메뉴')
        self.filemenu.addAction(self.setting)
        self.filemenu.addAction(self.info)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.checkBoxList = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5, 
                        self.checkBox_6, self.checkBox_7, self.checkBox_8, self.checkBox_9, self.checkBox_10,
                        self.checkBox_11, self.checkBox_12, self.checkBox_13, self.checkBox_14, self.checkBox_15]
        
        self.radioBoxList = [self.radioButton_18, self.radioButton_19, self.radioButton_14, self.radioButton_16, self.radioButton_13, 
                        self.radioButton_12, self.radioButton_17, self.radioButton_11, self.radioButton_20, self.radioButton_15]
        self.LoadData()
        self.retranslateUi(MainWindow)
        self.UpdateScoreboard()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "기멘의 게임 노트 " + ver))
        self.groupBox_p.setTitle(_translate("MainWindow", "승리 플레이어"))
        self.groupBox_hist.setTitle(_translate("MainWindow", "게임 기록 (게임중 이름 변경 시 기록 삭제 불가)"))
        self.groupBox_score.setTitle(_translate("MainWindow", "스코어"))
        self.pushButton_goose.setText(_translate("MainWindow", "거위 +" + str(wp[0])))
        self.pushButton_neutrality.setText(_translate("MainWindow", "중립 +" + str(wp[1])))
        self.pushButton_duck.setText(_translate("MainWindow", "오리 +" + str(wp[2])))
        self.pushButton_remove.setText(_translate("MainWindow", "선택 제거"))
        self.pushButton_clear.setText(_translate("MainWindow", "전체 제거 (게임 초기화)"))
        self.checkBox.setText(_translate("MainWindow", scoreKey[0]))
        self.checkBox_2.setText(_translate("MainWindow", scoreKey[1]))
        self.checkBox_3.setText(_translate("MainWindow", scoreKey[2]))
        self.checkBox_4.setText(_translate("MainWindow", scoreKey[3]))
        self.checkBox_5.setText(_translate("MainWindow", scoreKey[4]))
        self.checkBox_6.setText(_translate("MainWindow", scoreKey[5]))
        self.checkBox_7.setText(_translate("MainWindow", scoreKey[6]))
        self.checkBox_8.setText(_translate("MainWindow", scoreKey[7]))
        self.checkBox_9.setText(_translate("MainWindow", scoreKey[8]))
        self.checkBox_10.setText(_translate("MainWindow", scoreKey[9]))
        self.checkBox_11.setText(_translate("MainWindow", scoreKey[10]))
        self.checkBox_12.setText(_translate("MainWindow", scoreKey[11]))
        self.checkBox_13.setText(_translate("MainWindow", scoreKey[12]))
        self.checkBox_14.setText(_translate("MainWindow", scoreKey[13]))
        self.checkBox_15.setText(_translate("MainWindow", scoreKey[14]))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "구스구스덕"))
        
        self.groupBox_hof.setTitle(_translate("MainWindow", "야추의 전당"))
        self.label_mythic.setText(_translate("MainWindow", "- -"))
        self.label_legend.setText(_translate("MainWindow", "- -"))
        self.label_unique.setText(_translate("MainWindow", "- -"))
        self.groupBox_wp.setTitle(_translate("MainWindow", "야추의 전당 플레이어"))
        self.label_score.setText(_translate("MainWindow", "점수"))
        self.radioButton_11.setText(_translate("MainWindow", "Hihat"))
        self.radioButton_12.setText(_translate("MainWindow", "차재"))
        self.radioButton_13.setText(_translate("MainWindow", "재민"))
        self.radioButton_14.setText(_translate("MainWindow", "민머리"))
        self.radioButton_15.setText(_translate("MainWindow", "Guest"))
        self.radioButton_16.setText(_translate("MainWindow", "정고"))
        self.radioButton_17.setText(_translate("MainWindow", "초코동"))
        self.radioButton_18.setText(_translate("MainWindow", "고라파덕"))
        self.radioButton_19.setText(_translate("MainWindow", "귀조심"))
        self.radioButton_20.setText(_translate("MainWindow", "hihi"))
        self.pushButton_reg.setText(_translate("MainWindow", "등 록"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "야추의전당"))
        
    def LoadData(self):
        global yacht
        global score
        global scoreKey
        global cumulative_score
        global record
        global wp
        msg = ""
        loadflag = [0] * 6     
        path = DATA_FOLDER_PATH + '\\YachtDataFile.pickle'
        if os.path.exists(path):
            with open(path, 'rb') as f:
                yacht = list(pickle.load(f))
                loadflag[0] = 1
        path = DATA_FOLDER_PATH + '\\GooseDataFile.pickle'
        if os.path.exists(path):
            with open(path, 'rb') as f:
                score = dict(pickle.load(f))
                loadflag[1] = 1
        path = DATA_FOLDER_PATH + '\\CumulGooseDataFile.pickle'
        if os.path.exists(path):
            with open(path, 'rb') as f:
                cumulative_score = dict(pickle.load(f))
                loadflag[2] = 1
        path = DATA_FOLDER_PATH + '\\GooseRecordDataFile.pickle'
        if os.path.exists(path):
            self.listWidget.clear()
            with open(path, 'rb') as f:
                record = list(pickle.load(f))
                for i in record:
                    self.listWidget.addItem(i)
                loadflag[3] = 1
        path = DATA_FOLDER_PATH + '\\SettingDataFile.pickle'
        if os.path.exists(path):
            with open(path, 'rb') as f:
                wp = list(pickle.load(f))
                loadflag[4] = 1
        path = DATA_FOLDER_PATH + '\\NameSetKeyDataFile.pickle'
        if os.path.exists(path):
            with open(path, 'rb') as f:
                scoreKey = dict(pickle.load(f))
                loadflag[5] = 1
                
        self.UpdateScoreboard()
        if(loadflag[0] != 0 or loadflag[1] != 0 or loadflag[2] != 0) :
            if loadflag[0] == 1 :
                msg = msg + "YachtDB "
            if loadflag[1] == 1 :
                msg = msg + "GooseDB "
            if loadflag[2] == 1 :
                msg = msg + "CumulDB "
            if loadflag[3] == 1 :
                msg = msg + "RecordDB "
            if loadflag[4] == 1 :
                msg = msg + "SettingDB "
            if loadflag[5] == 1 :
                msg = msg + "NameSetKeyDB "
            msg = msg + "로드 완료"
        else:
            msg = msg + "로드 데이터 없음"
        MainWindow.statusBar().showMessage(msg)
                
                
    def HallOfFame(self):
        for i in range(10):
            if(self.radioBoxList[i].isChecked()):
                yacht.append((scoreKey[i], self.spinBox.value()))
                break
        path = DATA_FOLDER_PATH + '\\YachtDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(yacht, f)
        self.UpdateScoreboard()
        msg = "YachtData 저장됨"
        MainWindow.statusBar().showMessage(msg)
    
    def UpdateScoreboard(self):
        # 구스덕 점수
        slist = sorted(score.items(), key=lambda x: x[1], reverse = True)
        self.Label1.setText("1등 : " + slist[0][0])
        self.Label2.setText("2등 : " + slist[1][0])
        self.Label3.setText("3등 : " + slist[2][0])
        self.Label4.setText("4등 : " + slist[3][0])
        self.Label5.setText("5등 : " + slist[4][0])
        self.Label6.setText("6등 : " + slist[5][0])
        self.Label7.setText("7등 : " + slist[6][0])
        self.Label8.setText("8등 : " + slist[7][0])
        self.Label9.setText("9등 : " + slist[8][0])
        self.Label10.setText("10등 : " + slist[9][0])
        self.Label11.setText("11등 : " + slist[10][0])
        self.Label12.setText("12등 : " + slist[11][0])
        self.Label13.setText("13등 : " + slist[12][0])
        self.Label14.setText("14등 : " + slist[13][0])
        self.Label15.setText("15등 : " + slist[14][0])
        self.Label01.setText(str(slist[0][1]) + "점")
        self.Label02.setText(str(slist[1][1]) + "점")
        self.Label03.setText(str(slist[2][1]) + "점")
        self.Label04.setText(str(slist[3][1]) + "점")
        self.Label05.setText(str(slist[4][1]) + "점")
        self.Label06.setText(str(slist[5][1]) + "점")
        self.Label07.setText(str(slist[6][1]) + "점")
        self.Label08.setText(str(slist[7][1]) + "점")
        self.Label09.setText(str(slist[8][1]) + "점")
        self.Label010.setText(str(slist[9][1]) + "점")
        self.Label011.setText(str(slist[10][1]) + "점")
        self.Label012.setText(str(slist[11][1]) + "점")
        self.Label013.setText(str(slist[12][1]) + "점")
        self.Label014.setText(str(slist[13][1]) + "점")
        self.Label015.setText(str(slist[14][1]) + "점")
        # 구스덕 누적 점수
        slist = sorted(cumulative_score.items(), key=lambda x: x[1], reverse = True)
        self.Label16.setText(slist[0][0])
        self.Label17.setText(slist[1][0])
        self.Label18.setText(slist[2][0])
        self.Label19.setText(slist[3][0])
        self.Label20.setText(slist[4][0])
        self.Label21.setText(slist[5][0])
        self.Label22.setText(slist[6][0])
        self.Label23.setText(slist[7][0])
        self.Label24.setText(slist[8][0])
        self.Label25.setText(slist[9][0])
        self.Label26.setText(slist[10][0])
        self.Label27.setText(slist[11][0])
        self.Label28.setText(slist[12][0])
        self.Label29.setText(slist[13][0])
        self.Label30.setText(slist[14][0])
        self.Label016.setText(str(slist[0][1]) + "점 (누적)")
        self.Label017.setText(str(slist[1][1]) + "점")
        self.Label018.setText(str(slist[2][1]) + "점")
        self.Label019.setText(str(slist[3][1]) + "점")
        self.Label020.setText(str(slist[4][1]) + "점")
        self.Label021.setText(str(slist[5][1]) + "점")
        self.Label022.setText(str(slist[6][1]) + "점")
        self.Label023.setText(str(slist[7][1]) + "점")
        self.Label024.setText(str(slist[8][1]) + "점")
        self.Label025.setText(str(slist[9][1]) + "점")
        self.Label026.setText(str(slist[10][1]) + "점")
        self.Label027.setText(str(slist[11][1]) + "점")
        self.Label028.setText(str(slist[12][1]) + "점")
        self.Label029.setText(str(slist[13][1]) + "점")
        self.Label030.setText(str(slist[14][1]) + "점")
        # 야추 전당 점수
        yacht.sort(key=lambda x:x[1], reverse=True)
        if (len(yacht) > 0):
            self.label_mythic.setText(yacht[0][0] + " " + str(yacht[0][1]) + "점")
        if (len(yacht) > 1):
            self.label_legend.setText(yacht[1][0] + " " + str(yacht[1][1]) + "점")
        if (len(yacht) > 2):
            self.label_unique.setText(yacht[2][0] + " " + str(yacht[2][1]) + "점")
        
    def AddGooseScore(self):
        list = ""
        for i in range(len(self.checkBoxList)):
            if(self.checkBoxList[i].isChecked()):
                cumulative_score[scoreKey[i]] = cumulative_score[scoreKey[i]] + wp[0]
                score[scoreKey[i]] = score[scoreKey[i]] + wp[0]
                list = list + str(scoreKey[i]) + ' ' + str(wp[0]) + ' '
                self.checkBoxList[i].setChecked(False)
        self.listWidget.addItem(list)
        self.UpdateScoreboard()
        record.append(list)
        path = DATA_FOLDER_PATH + '\\GooseDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(score, f)
        path = DATA_FOLDER_PATH + '\\CumulGooseDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(cumulative_score, f)
        path = DATA_FOLDER_PATH + '\\GooseRecordDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(record, f)
        msg = "GooseData CumulGooseData GooseRecordData 저장됨"
        MainWindow.statusBar().showMessage(msg)
        
    def AddDuckScore(self):
        list = ""
        for i in range(len(self.checkBoxList)):
            if(self.checkBoxList[i].isChecked()):
                cumulative_score[scoreKey[i]] = cumulative_score[scoreKey[i]] + wp[2]
                score[scoreKey[i]] = score[scoreKey[i]] + wp[2]
                list = list + str(scoreKey[i]) + ' ' + str(wp[2]) + ' '
                self.checkBoxList[i].setChecked(False)
        self.listWidget.addItem(list)
        record.append(list)
        self.UpdateScoreboard()
        path = DATA_FOLDER_PATH + '\\GooseDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(score, f)
        path = DATA_FOLDER_PATH + '\\CumulGooseDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(cumulative_score, f)
        path = DATA_FOLDER_PATH + '\\GooseRecordDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(record, f)
        msg = "GooseData CumulGooseData GooseRecordData 저장됨"
        MainWindow.statusBar().showMessage(msg)
        
    def AddNeutralityScore(self):
        list = ""
        for i in range(len(self.checkBoxList)):
            if(self.checkBoxList[i].isChecked()):
                cumulative_score[scoreKey[i]] = cumulative_score[scoreKey[i]] + wp[1]
                score[scoreKey[i]] = score[scoreKey[i]] + wp[1]
                list = list + str(scoreKey[i]) + ' ' + str(wp[1]) + ' '
                self.checkBoxList[i].setChecked(False)
        self.listWidget.addItem(list)
        record.append(list)
        self.UpdateScoreboard()
        path = DATA_FOLDER_PATH + '\\GooseDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(score, f)
        path = DATA_FOLDER_PATH + '\\CumulGooseDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(cumulative_score, f)
        path = DATA_FOLDER_PATH + '\\GooseRecordDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(record, f)
        msg = "GooseData CumulGooseData GooseRecordData 저장됨"
        MainWindow.statusBar().showMessage(msg)

    def ItemRemove(self):
        del record[self.listWidget.currentRow()]
        takelist = self.listWidget.takeItem(self.listWidget.currentRow()).text().split()
        for i in range(0, len(takelist), 2):
            if(takelist[i] in score):
                score[takelist[i]] = score[takelist[i]] - int(takelist[i+1])
                cumulative_score[takelist[i]] = cumulative_score[takelist[i]] - int(takelist[i+1])
        self.UpdateScoreboard()
        path = DATA_FOLDER_PATH + '\\GooseDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(score, f)
        path = DATA_FOLDER_PATH + '\\CumulGooseDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(cumulative_score, f)
        path = DATA_FOLDER_PATH + '\\GooseRecordDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(record, f)
        msg = "GooseData CumulGooseData GooseRecordData 저장됨"
        MainWindow.statusBar().showMessage(msg)
        
    def ItemClear(self):
        self.listWidget.clear()
        record.clear()
        for i in range(0, 10):
            score[scoreKey[i]] = 0
        self.UpdateScoreboard()
        path = DATA_FOLDER_PATH + '\\GooseDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(score, f)
        path = DATA_FOLDER_PATH + '\\GooseRecordDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(record, f)
        for i in range(len(score)):
            score[scoreKey[i]] = 0
        self.UpdateScoreboard()
        msg = "GooseData clear 저장됨"
        MainWindow.statusBar().showMessage(msg)

    def Setting(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()
        self.pushButton_goose.setText("거위 +" + str(wp[0]))
        self.pushButton_neutrality.setText("중립 +" + str(wp[1]))
        self.pushButton_duck.setText("오리 +" + str(wp[2]))
        self.checkBox.setText(scoreKey[0])
        self.checkBox_2.setText(scoreKey[1])
        self.checkBox_3.setText(scoreKey[2])
        self.checkBox_4.setText(scoreKey[3])
        self.checkBox_5.setText(scoreKey[4])
        self.checkBox_6.setText(scoreKey[5])
        self.checkBox_7.setText(scoreKey[6])
        self.checkBox_8.setText(scoreKey[7])
        self.checkBox_9.setText(scoreKey[8])
        self.checkBox_10.setText(scoreKey[9])
        self.checkBox_11.setText(scoreKey[10])
        self.checkBox_12.setText(scoreKey[11])
        self.checkBox_13.setText(scoreKey[12])
        self.checkBox_14.setText(scoreKey[13])
        self.checkBox_15.setText(scoreKey[14])
        self.UpdateScoreboard()
        
    def Info(self):
        Dialog2 = QtWidgets.QDialog()
        ui = Ui_Dialog2()
        ui.setupUi(Dialog2)
        Dialog2.exec_()   
        
def createFolder():
    try:
        if not os.path.exists(DATA_FOLDER_PATH):
            os.makedirs(DATA_FOLDER_PATH)
    except OSError:
        print('Error: Creating directory. ' + DATA_FOLDER_PATH)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 500)
        Dialog.setMinimumSize(QtCore.QSize(200, 500))
        Dialog.setMaximumSize(QtCore.QSize(200, 500))
        self.DigLayout = QtWidgets.QGridLayout(Dialog)
        self.DigLayout.setObjectName("DigLayout")
        self.groupBox_goose_set = QtWidgets.QGroupBox(Dialog)
        self.groupBox_goose_set.setObjectName("groupBox_goose_set")
        self.gridLayout_set = QtWidgets.QGridLayout(self.groupBox_goose_set)
        self.gridLayout_set.setObjectName("gridLayout_set")
        self.spinBox_goose_score = QtWidgets.QSpinBox(self.groupBox_goose_set)
        self.spinBox_goose_score.setObjectName("spinBox_goose_score")
        self.gridLayout_set.addWidget(self.spinBox_goose_score, 0, 1, 1, 1)
        self.label_goose_set = QtWidgets.QLabel(self.groupBox_goose_set)
        self.label_goose_set.setObjectName("label_goose_set")
        self.gridLayout_set.addWidget(self.label_goose_set, 0, 0, 1, 1)
        self.label_neutr_set = QtWidgets.QLabel(self.groupBox_goose_set)
        self.label_neutr_set.setObjectName("label_neutr_set")
        self.gridLayout_set.addWidget(self.label_neutr_set, 1, 0, 1, 1)
        self.spinBox_neutr_score = QtWidgets.QSpinBox(self.groupBox_goose_set)
        self.spinBox_neutr_score.setObjectName("spinBox_neutr_score")
        self.gridLayout_set.addWidget(self.spinBox_neutr_score, 1, 1, 1, 1)
        self.label_duck_set = QtWidgets.QLabel(self.groupBox_goose_set)
        self.label_duck_set.setObjectName("label_duck_set")
        self.gridLayout_set.addWidget(self.label_duck_set, 2, 0, 1, 1)
        self.spinBox_duck_score = QtWidgets.QSpinBox(self.groupBox_goose_set)
        self.spinBox_duck_score.setObjectName("spinBox_duck_score")
        self.gridLayout_set.addWidget(self.spinBox_duck_score, 2, 1, 1, 1)
        self.DigLayout.addWidget(self.groupBox_goose_set, 1, 1, 4, 4)
        
        self.groupBox_name_set = QtWidgets.QGroupBox(Dialog)
        self.groupBox_name_set.setObjectName("groupBox_goose_set")
        self.gridLayout_set2 = QtWidgets.QGridLayout(self.groupBox_name_set)
        self.gridLayout_set2.setObjectName("gridLayout_set2")
        self.label_Empty2 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_Empty2.setObjectName("label_Empty2")
        self.label_Empty2.setText("  ")
        self.gridLayout_set2.addWidget(self.label_Empty2, 0, 5, 1, 1)
        self.label_p1 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p1.setObjectName("label_p1")
        self.lineEdit_p1 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p1.setObjectName("lineEdit_p1")
        self.lineEdit_p1.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p1, 0, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p1, 0, 1, 1, 1)
        self.label_p2 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p2.setObjectName("label_p2")
        self.lineEdit_p2 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p2.setObjectName("lineEdit_p2")
        self.lineEdit_p2.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p2, 1, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p2, 1, 1, 1, 1)
        self.label_p3 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p3.setObjectName("label_p3")
        self.lineEdit_p3 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p3.setObjectName("lineEdit_p3")
        self.lineEdit_p3.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p3, 2, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p3, 2, 1, 1, 1)
        self.label_p4 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p4.setObjectName("label_p4")
        self.lineEdit_p4 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p4.setObjectName("lineEdit_p4")
        self.lineEdit_p4.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p4, 3, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p4, 3, 1, 1, 1)
        self.label_p5 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p5.setObjectName("label_p5")
        self.lineEdit_p5 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p5.setObjectName("lineEdit_p5")
        self.lineEdit_p5.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p5, 4, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p5, 4, 1, 1, 1)
        self.label_p6 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p6.setObjectName("label_p6")
        self.lineEdit_p6 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p6.setObjectName("lineEdit_p6")
        self.lineEdit_p6.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p6, 5, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p6, 5, 1, 1, 1)
        self.label_p7 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p7.setObjectName("label_p1")
        self.lineEdit_p7 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p7.setObjectName("lineEdit_p1")
        self.lineEdit_p7.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p7, 6, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p7, 6, 1, 1, 1)
        self.label_p8 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p8.setObjectName("label_p8")
        self.lineEdit_p8 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p8.setObjectName("lineEdit_p8")
        self.lineEdit_p8.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p8, 7, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p8, 7, 1, 1, 1)
        self.label_p9 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p9.setObjectName("label_p9")
        self.lineEdit_p9 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p9.setObjectName("lineEdit_p9")
        self.lineEdit_p9.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p9, 8, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p9, 8, 1, 1, 1)
        self.label_p10 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p10.setObjectName("label_p10")
        self.lineEdit_p10 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p10.setObjectName("lineEdit_p10")
        self.lineEdit_p10.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p10, 9, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p10, 9, 1, 1, 1)
        self.label_p11 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p11.setObjectName("label_p11")
        self.lineEdit_p11 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p11.setObjectName("lineEdit_p11")
        self.lineEdit_p11.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p11, 10, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p11, 10, 1, 1, 1)
        self.label_p12 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p12.setObjectName("label_p12")
        self.lineEdit_p12 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p12.setObjectName("lineEdit_p12")
        self.lineEdit_p12.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p12, 11, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p12, 11, 1, 1, 1)
        self.label_p13 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p13.setObjectName("label_p13")
        self.lineEdit_p13 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p13.setObjectName("lineEdit_p13")
        self.lineEdit_p13.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p13, 12, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p13, 12, 1, 1, 1)
        self.label_p14 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p14.setObjectName("label_p14")
        self.lineEdit_p14 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p14.setObjectName("lineEdit_p14")
        self.lineEdit_p14.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p14, 13, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p14, 13, 1, 1, 1)
        self.label_p15 = QtWidgets.QLabel(self.groupBox_name_set)
        self.label_p15.setObjectName("label_p15")
        self.lineEdit_p15 = QtWidgets.QLineEdit(self.groupBox_name_set)
        self.lineEdit_p15.setObjectName("lineEdit_p15")
        self.lineEdit_p15.setMaxLength(10)
        self.gridLayout_set2.addWidget(self.label_p15, 14, 0, 1, 1)
        self.gridLayout_set2.addWidget(self.lineEdit_p15, 14, 1, 1, 1)
        self.DigLayout.addWidget(self.groupBox_name_set, 5, 1, 6, 4)
        
        self.pushButton_accept = QtWidgets.QPushButton()
        self.pushButton_accept.setObjectName("pushButton_accept")
        self.pushButton_accept.clicked.connect(lambda: self.Accept(Dialog))
        self.pushButton_close = QtWidgets.QPushButton()
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_close.clicked.connect(lambda: self.Destroy(Dialog))
        self.DigLayout.addWidget(self.pushButton_close, 15, 3, 1, 1)
        self.DigLayout.addWidget(self.pushButton_accept, 15, 4, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "설정"))
        self.groupBox_goose_set.setTitle(_translate("Dialog", "구스덕 우승 점수 설정"))
        self.groupBox_name_set.setTitle(_translate("Dialog", "구스덕 이름 설정"))
        self.label_goose_set.setText(_translate("Dialog", "거위 : " + str(wp[0])))
        self.label_neutr_set.setText(_translate("Dialog", "중립 : " + str(wp[1])))
        self.label_duck_set.setText(_translate("Dialog", "오리 : " + str(wp[2])))
        self.pushButton_accept.setText(_translate("Dialog", "적용"))
        self.pushButton_close.setText(_translate("Dialog", "취소"))
        
        self.label_p1.setText(_translate("Dialog", "P1 : "))
        self.label_p2.setText(_translate("Dialog", "P2 : "))
        self.label_p3.setText(_translate("Dialog", "P3 : "))
        self.label_p4.setText(_translate("Dialog", "P4 : "))
        self.label_p5.setText(_translate("Dialog", "P5 : "))
        self.label_p6.setText(_translate("Dialog", "P6 : "))
        self.label_p7.setText(_translate("Dialog", "P7 : "))
        self.label_p8.setText(_translate("Dialog", "P8 : "))
        self.label_p9.setText(_translate("Dialog", "P9 : "))
        self.label_p10.setText(_translate("Dialog", "P10 : "))
        self.label_p11.setText(_translate("Dialog", "P11 : "))
        self.label_p12.setText(_translate("Dialog", "P12 : "))
        self.label_p13.setText(_translate("Dialog", "P13 : "))
        self.label_p14.setText(_translate("Dialog", "P14 : "))
        self.label_p15.setText(_translate("Dialog", "P15 : "))

        self.lineEdit_p1.setText(scoreKey[0])
        self.lineEdit_p2.setText(scoreKey[1])
        self.lineEdit_p3.setText(scoreKey[2])
        self.lineEdit_p4.setText(scoreKey[3])
        self.lineEdit_p5.setText(scoreKey[4])
        self.lineEdit_p6.setText(scoreKey[5])
        self.lineEdit_p7.setText(scoreKey[6])
        self.lineEdit_p8.setText(scoreKey[7])
        self.lineEdit_p9.setText(scoreKey[8])
        self.lineEdit_p10.setText(scoreKey[9])
        self.lineEdit_p11.setText(scoreKey[10])
        self.lineEdit_p12.setText(scoreKey[11])
        self.lineEdit_p13.setText(scoreKey[12])
        self.lineEdit_p14.setText(scoreKey[13])
        self.lineEdit_p15.setText(scoreKey[14])
        
        self.spinBox_goose_score.setValue(wp[0])
        self.spinBox_neutr_score.setValue(wp[1])
        self.spinBox_duck_score.setValue(wp[2])
    
    def Accept(self, Dialog):
        
        score[self.lineEdit_p1.text()] = score.pop(scoreKey[0])
        cumulative_score[self.lineEdit_p1.text()] = cumulative_score.pop(scoreKey[0])
        scoreKey[0] = self.lineEdit_p1.text()
        score[self.lineEdit_p2.text()] = score.pop(scoreKey[1])
        cumulative_score[self.lineEdit_p2.text()] = cumulative_score.pop(scoreKey[1])
        scoreKey[1] = self.lineEdit_p2.text()
        score[self.lineEdit_p3.text()] = score.pop(scoreKey[2])
        cumulative_score[self.lineEdit_p3.text()] = cumulative_score.pop(scoreKey[2])
        scoreKey[2] = self.lineEdit_p3.text()
        score[self.lineEdit_p4.text()] = score.pop(scoreKey[3])
        cumulative_score[self.lineEdit_p4.text()] = cumulative_score.pop(scoreKey[3])
        scoreKey[3] = self.lineEdit_p4.text()
        score[self.lineEdit_p5.text()] = score.pop(scoreKey[4])
        cumulative_score[self.lineEdit_p5.text()] = cumulative_score.pop(scoreKey[4])
        scoreKey[4] = self.lineEdit_p5.text()
        score[self.lineEdit_p6.text()] = score.pop(scoreKey[5])
        cumulative_score[self.lineEdit_p6.text()] = cumulative_score.pop(scoreKey[5])
        scoreKey[5] = self.lineEdit_p6.text()
        score[self.lineEdit_p7.text()] = score.pop(scoreKey[6])
        cumulative_score[self.lineEdit_p7.text()] = cumulative_score.pop(scoreKey[6])
        scoreKey[6] = self.lineEdit_p7.text()
        score[self.lineEdit_p8.text()] = score.pop(scoreKey[7])
        cumulative_score[self.lineEdit_p8.text()] = cumulative_score.pop(scoreKey[7])
        scoreKey[7] = self.lineEdit_p8.text()
        score[self.lineEdit_p9.text()] = score.pop(scoreKey[8])
        cumulative_score[self.lineEdit_p9.text()] = cumulative_score.pop(scoreKey[8])
        scoreKey[8] = self.lineEdit_p9.text()
        score[self.lineEdit_p10.text()] = score.pop(scoreKey[9])
        cumulative_score[self.lineEdit_p10.text()] = cumulative_score.pop(scoreKey[9])
        scoreKey[9] = self.lineEdit_p10.text()
        score[self.lineEdit_p11.text()] = score.pop(scoreKey[10])
        cumulative_score[self.lineEdit_p11.text()] = cumulative_score.pop(scoreKey[10])
        scoreKey[10] = self.lineEdit_p11.text()
        score[self.lineEdit_p12.text()] = score.pop(scoreKey[11])
        cumulative_score[self.lineEdit_p12.text()] = cumulative_score.pop(scoreKey[11])
        scoreKey[11] = self.lineEdit_p12.text()
        score[self.lineEdit_p13.text()] = score.pop(scoreKey[12])
        cumulative_score[self.lineEdit_p13.text()] = cumulative_score.pop(scoreKey[12])
        scoreKey[12] = self.lineEdit_p13.text()
        score[self.lineEdit_p14.text()] = score.pop(scoreKey[13])
        cumulative_score[self.lineEdit_p14.text()] = cumulative_score.pop(scoreKey[13])
        scoreKey[13] = self.lineEdit_p14.text()
        score[self.lineEdit_p15.text()] = score.pop(scoreKey[14])
        cumulative_score[self.lineEdit_p15.text()] = cumulative_score.pop(scoreKey[14])
        scoreKey[14] = self.lineEdit_p15.text()
        
        path = DATA_FOLDER_PATH + '\\GooseDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(score, f)
        path = DATA_FOLDER_PATH + '\\CumulGooseDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(cumulative_score, f)
        path = DATA_FOLDER_PATH + '\\NameSetKeyDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(scoreKey, f)
        
        wp[0] = self.spinBox_goose_score.value()
        wp[1] = self.spinBox_neutr_score.value()
        wp[2] = self.spinBox_duck_score.value()
        path = DATA_FOLDER_PATH + '\\SettingDataFile.pickle'
        with open(path, 'wb') as f:
            pickle.dump(wp, f)
        msg = "SettingData 저장됨"
        MainWindow.statusBar().showMessage(msg)
        Dialog.close()
        
    def Destroy(self, Dialog):
        Dialog.close()
        
class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(200, 100)
        Dialog2.setMinimumSize(QtCore.QSize(200, 100))
        Dialog2.setMaximumSize(QtCore.QSize(200, 100))
        self.DigLayout2 = QtWidgets.QGridLayout(Dialog2)
        self.DigLayout2.setObjectName("DigLayout")
        self.label_info = QtWidgets.QLabel(Dialog2)
        self.label_info.setText("기멘의 게임 노트")
        self.label_info.setStyleSheet("color:#000000;font-size:12px;font-weight:bold")
        self.label_info.setAlignment(Qt.AlignVCenter |Qt.AlignHCenter)
        self.label_info2 = QtWidgets.QLabel(Dialog2)
        self.label_info2.setText("제작 : Hihat\n버전 : " + ver + "\nMade with Python3.10.1")
        self.label_info2.setAlignment(Qt.AlignTop)
        self.DigLayout2.addWidget(self.label_info, 0, 0, 1, 1)
        self.DigLayout2.addWidget(self.label_info2, 1, 0, 1, 1)
        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog2", "정보"))
        
if __name__ == "__main__":
    createFolder()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog,QInputDialog,  QApplication, QPushButton, QAction, QFileDialog, QLabel
import pyautogui
import time
from pynput import mouse
from PIL import Image
import os
import pickle

""" os에서의 절대 경로 획득 """
if getattr(sys, 'frozen', False):
    # exe로 실행한 경우, exe를 보관한 디렉토리의 full path를 취득
    CUR_PATH = os.path.dirname(os.path.abspath(sys.executable))
else:
    # py로 실행한 경우, py를 보관한 디렉토리의 full path를 취득
    CUR_PATH = os.path.dirname(os.path.abspath(__file__))
# 이 파일(py)이 있는 디렉토리의 절대 경로
# CUR_PATH = os.path.dirname(os.path.realpath(__file__))
# Data 파일이 저장되는 장소
DATA_FOLDER_PATH = CUR_PATH + '\\' + 'CaptureDataFile'

page = 0                            # 캡쳐 완료된 페이지 수 저장용
picture_size = [0, 0, 0, 0, 0, 0]   # 왼쪽 상단 좌표 (0,1), 오른쪽 하단 좌표 (2,3), 현재 마우스 좌표 (4,5)

msg = "캡쳐할 좌표를 등록하세요."

def get_mouse_point(x, y):
    print('\r마우스 좌표 : {0}'.format((x, y)), end='')
    picture_size[4] = x
    picture_size[5] = y
    path = DATA_FOLDER_PATH + '\\PointDataFile.pickle'
    with open(path, 'wb') as f:
        pickle.dump(picture_size, f)
    return False

def get_lest_mouse_point(x, y):
    print('\r마우스 좌표 : {0}'.format((x, y)), end='')
    picture_size[0] = x
    picture_size[1] = y
    path = DATA_FOLDER_PATH + '\\PointDataFile.pickle'
    with open(path, 'wb') as f:
        pickle.dump(picture_size, f)
    return False

def get_right_mouse_point(x, y):
    print('\r마우스 좌표 : {0}'.format((x, y)), end='')
    picture_size[2] = x
    picture_size[3] = y
    path = DATA_FOLDER_PATH + '\\PointDataFile.pickle'
    with open(path, 'wb') as f:
        pickle.dump(picture_size, f)
    return False

def png_to_pdf(fname):
    imglist = []
    for idx, file in enumerate(fname):
        globals()['img_{}'.format(idx)] = (Image.open(file)).convert("RGB")
        imglist.append(globals()['img_{}'.format(idx)])
    img_0.save(DATA_FOLDER_PATH, '\\New_pdf.pdf',save_all=True, append_images=imglist)

class MyApp(QMainWindow):
    label_point = QLabel
    label_left_point = QLabel
    label_right_point = QLabel
    label_path = QLabel

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CaptureTool')
        self.statusBar().showMessage(msg)
        #--------ProgressBar
# 앞의 두 매개변수는 창의 x, y 위치를 결정하고, 뒤의 두 매개변수는 각각 창의 너비와 높이를 결정합니다.
        openFile = QAction('To PDF', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip("Open New File")
        openFile.triggered.connect(self.show_file)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('설정')
        filemenu.addAction(openFile)

        btn_mouse_coordinates = QPushButton('마우스 좌표 보기 (P)', self)
        btn_mouse_coordinates.resize(btn_mouse_coordinates.sizeHint())
        btn_mouse_coordinates.setShortcut('p')
        btn_mouse_coordinates.move(30, 50)
        btn_mouse_coordinates.clicked.connect(self.mouse_coordinates)

        self.label_point = QLabel('', self)
        self.label_point.move(160,55)
        self.label_point.resize(self.label_point.sizeHint())

        btn_left_point = QPushButton('좌측 상단 좌표 저장 ([)', self)
        btn_left_point.setToolTip('이미지의 좌측 상단 꼭지점에 마우스를 올리고, 단축키를 사용합니다.')
        btn_left_point.setShortcut('[')
        btn_left_point.move(30,100)
        btn_left_point.resize(btn_left_point.sizeHint())
        btn_left_point.clicked.connect(self.Event_start_point)

        btn_left_point_set = QPushButton('수동 지정', self)
        btn_left_point_set.setToolTip('이미지의 좌측 상단 꼭지점을 수동으로 설정합니다.')
        btn_left_point_set.move(170,100)
        btn_left_point_set.resize(btn_left_point_set.sizeHint())
        btn_left_point_set.clicked.connect(self.set_left_page)

        self.label_left_point = QLabel('', self)
        self.label_left_point.move(250,105)
        self.label_left_point.resize(self.label_left_point.sizeHint())

        btn_right_point = QPushButton('우측 하단 좌표 저장 (])', self)
        btn_right_point.setToolTip('이미지 우측 하단 꼭지점에 마우스를 올리고, 단축키를 사용합니다.')
        btn_right_point.setShortcut(']')
        btn_right_point.move(30,150)
        btn_right_point.resize(btn_right_point.sizeHint())
        btn_right_point.clicked.connect(self.Event_end_point)

        btn_right_point_set = QPushButton('수동 지정', self)
        btn_right_point_set.setToolTip('이미지의 우측 상단 꼭지점을 수동으로 설정합니다.')
        btn_right_point_set.move(170,150)
        btn_right_point_set.resize(btn_right_point_set.sizeHint())
        btn_right_point_set.clicked.connect(self.set_right_page)

        self.label_right_point = QLabel('', self)
        self.label_right_point.move(250,155)
        self.label_right_point.resize(self.label_right_point.sizeHint())

        btn_last_page_set = QPushButton('마지막으로 캡쳐 완료한 페이지 설정', self)
        btn_last_page_set.setToolTip('프로그램이 비정상적으로 종료되거나, 이어서 캡쳐할 경우 마지막으로 캡쳐 완료한 페이지를 설정합니다.')
        btn_last_page_set.move(30,200)
        btn_last_page_set.resize(btn_last_page_set.sizeHint())
        btn_last_page_set.clicked.connect(self.page_input)

        self.label_path = QLabel("[저장 경로]\n" + DATA_FOLDER_PATH + "\\CapturedFiles", self)
        self.label_path.move(30,250)
        self.label_path.resize(self.label_path.sizeHint())

        btn_run = QPushButton('캡 쳐', self)
        btn_run.setToolTip('선택한 좌표 영역이 캡쳐됩니다. 다른 프로그램이 이미지를 가리지 않도록 해주세요.')
        btn_run.move(0, 300)
        btn_run.resize(500,170)
        btn_run.clicked.connect(self.get_picture)
        self.setGeometry(100,100,500,500)
        self.LoadData();
        self.show()

    def LoadData(self):
        global picture_size
        path = DATA_FOLDER_PATH + '\\PointDataFile.pickle'
        if os.path.exists(path):
            with open(path, 'rb') as f:
                picture_size = list(pickle.load(f))
        self.label_left_point.setText("(%s, %s)"%(picture_size[0],picture_size[1]))
        self.label_left_point.resize(self.label_left_point.sizeHint())
        self.label_left_point.update()
        self.label_right_point.setText("(%s, %s)"%(picture_size[2],picture_size[3]))
        self.label_right_point.resize(self.label_left_point.sizeHint())
        self.label_right_point.update()

    def set_left_page(self):
        p, ok = QInputDialog.getInt(self, '좌표 설정', 'x :')
        if ok:
            picture_size[0] = p
        p, ok = QInputDialog.getInt(self, '좌표 설정', 'y :')
        if ok:
            picture_size[1] = p
        self.label_left_point.setText("(%s, %s)"%(picture_size[0],picture_size[1]))
        self.label_left_point.resize(self.label_left_point.sizeHint())
        self.label_left_point.update()
        msg = "좌측 상단 좌표 : (%s, %s)"%(picture_size[0],picture_size[1])
        self.status(msg)

    def set_right_page(self):
        p, ok = QInputDialog.getInt(self, '좌표 설정', 'x :')
        if ok:
            picture_size[2] = p
        p, ok = QInputDialog.getInt(self, '좌표 설정', 'y :')
        if ok:
            picture_size[3] = p
        self.label_right_point.setText("(%s, %s)"%(picture_size[2],picture_size[3]))
        self.label_right_point.resize(self.label_right_point.sizeHint())
        self.label_right_point.update()
        msg = "우측 하단 좌표 : (%s, %s)"%(picture_size[2],picture_size[3])
        self.status(msg)

    def page_input(self):
        global page
        p, ok = QInputDialog.getInt(self, '페이지 설정', '마지막으로 캡쳐한 페이지 설정:')
        if ok:
            page = p
            msg = "마지막으로 캡쳐한 페이지 설정 : %dpage"%page
            self.status(msg)

    def mouse_coordinates(self):
        with mouse.Listener(on_move=get_mouse_point) as listener:
            listener.join()
            self.label_point.setText("(%s, %s)"%(picture_size[4],picture_size[5]))
            self.label_point.resize(self.label_point.sizeHint())
            self.label_point.update()
            msg = "마우스 좌표 : (%s, %s)"%(picture_size[4],picture_size[5])
            self.status(msg)

    def show_file(self):
        global dir_path
        fname = QFileDialog.getOpenFileNames(self, 'Open file' , DATA_FOLDER_PATH + "\\CapturedFiles",'Capture File(*.png)')
        fname[0].sort()
        if fname[0]:
            png_to_pdf(fname[0])

    def status(self,msg):
        self.statusBar().showMessage(msg)

    def Event_start_point(self):
        with mouse.Listener(on_move=get_lest_mouse_point) as listener:
            listener.join()
            self.label_left_point.setText("(%s, %s)"%(picture_size[0],picture_size[1]))
            self.label_left_point.resize(self.label_left_point.sizeHint())
            self.label_left_point.update()
            msg = "좌측 상단 좌표 : (%s, %s)"%(picture_size[0],picture_size[1])
            self.status(msg)

    def Event_end_point(self):
        with mouse.Listener(on_move=get_right_mouse_point) as listener:
            listener.join()
            self.label_right_point.setText("(%s, %s)"%(picture_size[2],picture_size[3]))
            self.label_right_point.resize(self.label_right_point.sizeHint())
            self.label_right_point.update()
            msg = "우측 하단 좌표 : (%s, %s)"%(picture_size[2],picture_size[3])
            self.status(msg)

    def get_picture(self):
        try:
            if not os.path.exists(DATA_FOLDER_PATH + "\\CapturedFiles"):
                os.makedirs(DATA_FOLDER_PATH + "\\CapturedFiles")
        except OSError:
            print('Error: Creating directory. ' + DATA_FOLDER_PATH + "\\CapturedFiles")
        global page
        time.sleep(0.1)
        if (picture_size[2] > 0 or picture_size[3] > 0) and (picture_size[0] < picture_size[2] and picture_size[1] < picture_size[3]):
            page = page + 1
            pyautogui.screenshot(DATA_FOLDER_PATH + '\\CapturedFiles\\%04d.png'%(page), region=(picture_size[0], picture_size[1],
            picture_size[2]-picture_size[0],picture_size[3]-picture_size[1]))
            msg = "%dpage 캡쳐 완료"%page
            self.status(msg)
        else :
            msg = "캡쳐 실패 (지정된 좌표를 확인해 주세요)"
            self.status(msg)

def createFolder():
    try:
        if not os.path.exists(DATA_FOLDER_PATH):
            os.makedirs(DATA_FOLDER_PATH)
    except OSError:
        print('Error: Creating directory. ' + DATA_FOLDER_PATH)
if __name__ == '__main__':
    createFolder()
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
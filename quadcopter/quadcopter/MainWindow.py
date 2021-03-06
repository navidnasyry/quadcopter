from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QAction,qApp


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('MainWindow.ui', self)
        self.setWindowTitle('Client')

        #connect functions to objects
        self.actionExit.triggered.connect(self.Exit)
        self.btn_takeoff.clicked.connect(self.enter_TakeOff)
        self.btn_land.clicked.connect(self.enter_Land)
        self.btn_up.clicked.connect(self.enter_Up)
        self.btn_down.clicked.connect(self.enter_Down)
        self.btn_arrowUp.clicked.connect(self.enter_UpArrow)
        self.btn_arrowDown.clicked.connect(self.enter_DownArrow)
        self.btn_arrowRight.clicked.connect(self.enter_RightArrow)
        self.btn_arrowLeft.clicked.connect(self.enter_LeftArrow)
        self.btn_send.clicked.connect(self.send_data)
        self.recive_data()





    def send_data(self):
        print("Send Data Clicked")
        #recive data from client
        flightMode = self.cmb_flightMode.currentText()
        roll = self.dsb_roll.value()
        pitch = self.dsb_pitch.value()
        maxAngle = self.dsb_maxAngle.value()
        maxYaw = self.dsb_maxYawAngle.value()
        maxThrust = self.dsb_maxThrust.value()
        minThrust = self.dsb_minThrust.value()

        print(flightMode)
        print(roll)
        print(pitch)
        print(maxAngle)
        print(maxYaw)
        print(maxThrust)
        print(minThrust)




    #Show Data
    def recive_data(self):
        print("Data recived...")

        #Battery
        self.pgs_battery.setValue(75)

        #Compass ==>> 0 = south  &  clockWise
        self.dial_compass.setValue(180)

        #Lcd ==>> maximum digits = 5

        #Barometer
        self.lcd_bar.display(1.2345)

        #Temperature
        self.lcd_temperature.display(20.25)

        #lcd vol/cur ==>> maximum digits = 7

        #Voltage
        self.lcd_voltage.display(220.2)

        #Current
        self.lcd_current.display(120.5)

        #LinearAcceleration
        self.lcd_linearAcceleration_X.display(30.50)
        self.lcd_linearAcceleration_Y.display(33.50)
        self.lcd_linearAcceleration_Z.display(35.50)

        #AngularVelocity
        self.lcd_angularVelocity_X.display(25.60)
        self.lcd_angularVelocity_Y.display(27.60)
        self.lcd_angularVelocity_Z.display(29.60)



    def Exit(self):
        print("Exit")
        self.close()

    def enter_TakeOff(self):
        print("Enter Takeoff")

    def enter_Land(self):
        print("Enter Land")

    def enter_Up(self):
        print("Enter Up")

    def enter_Down(self):
        print("Enter Down")

    def enter_UpArrow(self):
        print("Enter  UpArrow")

    def enter_DownArrow(self):
        print("Enter DownArrow")

    def enter_LeftArrow(self):
        print("Enter LeftArrow")

    def enter_RightArrow(self):
        print("Enter RightArrow")



'''
    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()'''

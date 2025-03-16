from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(487, 787)
        # Новые стили для всего интерфейса
        Form.setStyleSheet("""
            /* Основной стиль для окна */
            QWidget {
                background-color: #1E1E1E; /* Тёмный фон */
                color: #FFFFFF; /* Белый текст */
                font-family: "Segoe UI";
                font-size: 20px;
            }

            /* Стиль для QFrame (верхняя панель) */
            #function_frame {
                background-color: #2E3440; /* Тёмно-синий фон */
                border-bottom: 1px solid #4C566A; /* Серая граница */
                border-top-left-radius: 15px;
                border-top-right-radius: 15px;
            }

            /* Стиль для QLabel (заголовок) */
            QLabel {
                font-size: 25px;
                color: #ECEFF4; /* Светлый текст */
            }

            /* Стиль для кнопок */
            QPushButton {
                background-color: #4C566A; /* Тёмно-серый фон */
                color: #ECEFF4; /* Светлый текст */
                border-radius: 10px; /* Закруглённые углы */
                padding: 15px;
                font-size: 25px;
            }

            /* Стиль для кнопок при нажатии */
            QPushButton:pressed {
                background-color: #81A1C1; /* Голубой фон при нажатии */
            }

            /* Стиль для специальных кнопок (AC, +/-, %) */
            QPushButton[class="btn_group_1"] {
                background-color: #3B4252; /* Серый фон */
                color: #D8DEE9; /* Светло-серый текст */
            }

            /* Стиль для кнопок операций (+, -, ×, ÷) */
            QPushButton[class="btn_group_2"] {
                background-color: #D08770; /* Оранжевый фон */
                color: #2E3440; /* Тёмный текст */
                font-size: 30px;
            }

            /* Стиль для кнопки "=" */
            QPushButton#pushButton_19 {
                background-color: #A3BE8C; /* Зелёный фон */
                color: #2E3440; /* Тёмный текст */
                font-size: 35px;
            }

            /* Стиль для QLineEdit (поле ввода) */
            QLineEdit {
                background-color: #2E3440; /* Тёмно-синий фон */
                color: #ECEFF4; /* Светлый текст */
                border: none;
                font-size: 50px;
                padding: 10px;
            }
        """)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.function_frame = QtWidgets.QFrame(parent=Form)
        self.function_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.function_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.function_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.function_frame.setObjectName("function_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.function_frame)
        self.horizontalLayout.setContentsMargins(20, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.function_frame)
        self.label_2.setMinimumSize(QtCore.QSize(20, 20))
        self.label_2.setMaximumSize(QtCore.QSize(20, 20))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".\\icon/calculator.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(parent=self.function_frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.close_btn = QtWidgets.QPushButton(parent=self.function_frame)
        self.close_btn.setStyleSheet("")
        self.close_btn.setText("")
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.gridLayout_2.addWidget(self.function_frame, 0, 0, 1, 1)
        self.button_frame = QtWidgets.QFrame(parent=Form)
        self.button_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.button_frame.setObjectName("button_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.button_frame)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.zero_btn = QtWidgets.QPushButton(parent=self.button_frame)
        self.zero_btn.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.zero_btn.setStyleSheet("")
        self.zero_btn.setObjectName("zero_btn")
        self.gridLayout.addWidget(self.zero_btn, 5, 0, 1, 2)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_6.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStatesOutlyingIslands))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.button_frame)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 4)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 4, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_15.setStyleSheet("")
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setAutoExclusive(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 4, 3, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_19.setStyleSheet("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 5, 3, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 4, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_11.setStyleSheet("")
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setAutoExclusive(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 3, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_8.setStyleSheet("")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 3, 0, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 5, 2, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 4, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.button_frame)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.button_frame)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(-1)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("qproperty-iconSize: 40px;")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icon/plus-minus-variant.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.button_frame)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(-1)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\icon/percent-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.button_frame, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Calculator"))
        self.zero_btn.setText(_translate("Form", "0"))
        self.pushButton_6.setText(_translate("Form", "÷"))
        self.pushButton_6.setProperty("class", _translate("Form", "btn_group_2"))
        self.pushButton_9.setText(_translate("Form", "7"))
        self.lineEdit.setText(_translate("Form", "1,000"))
        self.pushButton_7.setText(_translate("Form", "9"))
        self.pushButton_16.setText(_translate("Form", "3"))
        self.pushButton_15.setText(_translate("Form", "+"))
        self.pushButton_15.setProperty("class", _translate("Form", "btn_group_2"))
        self.pushButton_19.setText(_translate("Form", "="))
        self.pushButton_19.setProperty("class", _translate("Form", "btn_group_2"))
        self.pushButton_17.setText(_translate("Form", "2"))
        self.pushButton_11.setText(_translate("Form", "﹣"))
        self.pushButton_11.setProperty("class", _translate("Form", "btn_group_2"))
        self.pushButton_3.setText(_translate("Form", "AC"))
        self.pushButton_3.setProperty("class", _translate("Form", "btn_group_1"))
        self.pushButton_13.setText(_translate("Form", "5"))
        self.pushButton_8.setText(_translate("Form", "×"))
        self.pushButton_8.setProperty("class", _translate("Form", "btn_group_2"))
        self.pushButton_10.setText(_translate("Form", "8"))
        self.pushButton_14.setText(_translate("Form", "4"))
        self.pushButton_20.setText(_translate("Form", "."))
        self.pushButton_18.setText(_translate("Form", "1"))
        self.pushButton_12.setText(_translate("Form", "6"))
        self.pushButton_4.setProperty("class", _translate("Form", "btn_group_1"))
        self.pushButton_5.setProperty("class", _translate("Form", "btn_group_1"))

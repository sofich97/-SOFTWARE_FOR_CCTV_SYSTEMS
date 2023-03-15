 # -*- coding: utf-8 -*-


from PyQt5 import QtWidgets     # Модуль для PyQt
from PyQt5 import QtCore        # Модуль для PyQt


from PyQt5.QtGui import QIcon


import time                     # Библиотека для работы с временем системы
import math                     # Библиотека для работы с математикой
import os                       # Библиотека для работы с ОС (создание папок и файлов)
import datetime                 # Библиотека для работы с датами
import numpy
import cv2



pass_folder = os.getcwd()       # Путь для сохранения данных (по умолчаю это расположение py- файла)



############# Всегда начинайте с инициализации Qt (только один раз для каждого приложения)#########################
app = QtWidgets.QApplication([])



#####    Функции для окна настроек камер ###############################


# Читае файл насроек и выставляет все как в нем
def start_program():

    try:

        f = open('setting.txt', 'r')    # открываем файл настроек, чтобы его прочитать

        H=f.read()                      # прочитали настройки, как строку

        G=H.split('\n')                 # преобразуем строку H в список G по разделителю '\n'

        QCom1.setCurrentIndex (int(G[0]))
        QCom2.setCurrentIndex (int(G[1]))
        QCom3.setCurrentIndex (int(G[2]))
        QCom4.setCurrentIndex (int(G[3]))
        QCom5.setCurrentIndex (int(G[4]))
        QCom6.setCurrentIndex (int(G[5]))
        QCom7.setCurrentIndex (int(G[6]))
        QCom8.setCurrentIndex (int(G[7]))
        QCom9.setCurrentIndex (int(G[8]))
        QCom10.setCurrentIndex (int(G[9]))
        QCom11.setCurrentIndex (int(G[10]))
        QCom12.setCurrentIndex (int(G[11]))
        QCom13.setCurrentIndex (int(G[12]))
        QCom14.setCurrentIndex (int(G[13]))
        QCom15.setCurrentIndex (int(G[14]))
        QCom16.setCurrentIndex (int(G[15]))

        f.close()


    except:

        set_default_sett()



# Установка настроек по умолчанию (при нажатии кнопки Default, все сбрасываетмя до начальных настроек)
def set_default_sett():


    f = open('setting.txt', 'w') # открывает файл setting.txt для записи в него начальных настроек камер

    f.write("0" '\n')   # сохраняет в 1-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 2-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 3-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 4-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 5-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 6-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 7-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 8-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 9-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 10-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 11-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 12-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 13-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 14-ой строке 0 и переходит на новую строку
    f.write("0" '\n')   # сохраняет в 15-ой строке 0 и переходит на новую строку
    f.write("0")        # сохраняет в 16-ой строке 0

    f.close()   # закрывает файл setting.txt


    QCom1.setCurrentIndex (0)             # задаю  QCom1 индекс 0
    QCom2.setCurrentIndex (0)             # задаю  QCom2 индекс 0
    QCom3.setCurrentIndex (0)             # задаю  QCom3 индекс 0
    QCom4.setCurrentIndex (0)             # задаю  QCom4 индекс 0
    QCom5.setCurrentIndex (0)             # задаю  QCom5 индекс 0
    QCom6.setCurrentIndex (0)             # задаю  QCom6 индекс 0
    QCom7.setCurrentIndex (0)             # задаю  QCom7 индекс 0
    QCom8.setCurrentIndex (0)             # задаю  QCom8 индекс 0
    QCom9.setCurrentIndex (0)             # задаю  QCom9 индекс 0
    QCom10.setCurrentIndex (0)             # задаю  QCom10 индекс 0
    QCom11.setCurrentIndex (0)             # задаю  QCom11 индекс 0
    QCom12.setCurrentIndex (0)             # задаю  QCom12 индекс 0
    QCom13.setCurrentIndex (0)             # задаю  QCom13 индекс 0
    QCom14.setCurrentIndex (0)             # задаю  QCom14 индекс 0
    QCom15.setCurrentIndex (0)             # задаю  QCom15 индекс 0
    QCom16.setCurrentIndex (0)             # задаю  QCom16 индекс 0

# Функция, которая выполняется при нажатии кнопки Ок на окне setting
def set_user_sett():

    f = open('setting.txt', 'w') # открывает файл setting.txt для записи в него выбрпнных настроек камер
    f.write(str(QCom1.currentIndex()) +'\n')    # сохраняет в 1-ой строке выбранную переменную в QCom1 и переходит на новую строку
    f.write(str(QCom2.currentIndex()) +'\n')    # сохраняет в 2-ой строке выбранную переменную в QCom2 и переходит на новую строку
    f.write(str(QCom3.currentIndex()) +'\n')    # сохраняет в 3-ой строке выбранную переменную в QCom3 и переходит на новую строку
    f.write(str(QCom4.currentIndex()) +'\n')    # сохраняет в 4-ой строке выбранную переменную в QCom4 и переходит на новую строку
    f.write(str(QCom5.currentIndex()) +'\n')    # сохраняет в 5-ой строке выбранную переменную в QCom5 и переходит на новую строку
    f.write(str(QCom6.currentIndex()) +'\n')    # сохраняет в 6-ой строке выбранную переменную в QCom6 и переходит на новую строку
    f.write(str(QCom7.currentIndex()) +'\n')    # сохраняет в 7-ой строке выбранную переменную в QCom7 и переходит на новую строку
    f.write(str(QCom8.currentIndex()) +'\n')    # сохраняет в 8-ой строке выбранную переменную в QCom8 и переходит на новую строку
    f.write(str(QCom9.currentIndex()) +'\n')    # сохраняет в 9-ой строке выбранную переменную в QCom9 и переходит на новую строку
    f.write(str(QCom10.currentIndex()) +'\n')   # сохраняет в 10-ой строке выбранную переменную в QCom10 и переходит на новую строку
    f.write(str(QCom11.currentIndex()) +'\n')   # сохраняетв 11-ой строке выбранную переменную в QCom11 и переходит на новую строку
    f.write(str(QCom12.currentIndex()) +'\n')   # сохраняет в 12-ой строке выбранную переменную в QCom12 и переходит на новую строку
    f.write(str(QCom13.currentIndex()) +'\n')   # сохраняет в 13-ой строке выбранную переменную в QCom13 и переходит на новую строку
    f.write(str(QCom14.currentIndex()) +'\n')   # сохраняет в 14-ой строке выбранную переменную в QCom14 и переходит на новую строку
    f.write(str(QCom15.currentIndex()) +'\n')   # сохраняет в 15-ой строке выбранную переменную в QCom15 и переходит на новую строку
    f.write(str(QCom16.currentIndex()) )        # сохраняет в 16-ой строке выбранную переменную в QCom16

    f.close()   # закрывает файл setting.txt


    second_window.close()    # закрывает окно setting
    first_window.show()      # открывается окно control


 # Закрываем окно настройки
def close_sett_wind():
    second_window.close()    # закрывает окно setting
    first_window.show()      # открывается окно control




# Функция, которая выполняется при нажатии кнопки 'Open second window'
def setting_window_show():
    second_window.show()
    first_window.hide()




def close_control_wind():
    first_window.close()





### -----------   Функции для окна control -------------------

# узнаем адрес папки, которую сами и выбрали
def select_folder():
    global pass_folder
    pass_folder = str(QtWidgets.QFileDialog.getExistingDirectory(first_window, "Select Directory"))  # Через QFileDialog



 # кнопка старт все идет с нее
# Функция, содержащая функции, нужные для начала записи с камер и сохранения видеоданных    (не меняется)
def start_video_record():


    global key_start_video # ключ проверки исправности камер

    poka_yoke()  # функция, которая производит проверку камер (активированы ли они в настройках, поддерживают разрешение, подключены ли в разъем)

    if key_start_video==True:

        btn2.setEnabled(True)   # активируется кнопка стоп
        btn3.setEnabled(False)   # блокируется кнопка folderbrowser
        btn4.setEnabled(False)    # блокируется кнопка setting
        btn5.setEnabled(False)    # блокируется кнопка exit
        btn1.setEnabled(False)    # блокируется кнопка старт

        get_number_work_dir()               # Считаем сколько папок уже есть в рабочей папке
        create_work_dir()                   # Создаем папку (дд.мм.дд) для сохранения видео (если уже есть, то не создаем)
        get_number_of_videofiles()          # Узнаем сколько видео уже есть с 1 камеры в данной папке (дд.мм.дд)
        camera_setting()                    # Настраиваем камеру и запускаем видеопоток
        start_timer()





# так как ничего не удаляем эта функция и не нужна вроде, но пусть будет
# Программа узнает число рабочих папок с видео в папке которую создал юзер или где лежит py файл, если он сам адрес не задавал (не меняется)
def get_number_work_dir():

    global  number_work_dir_list

    number_work_dir_list = []            # Пустой список, куда будет добавлять имена папок каждые новые сутки, чтобы потом удалять ненужные и не тратить всю память винта


    names = os.listdir(pass_folder)                         # Получаем список, содержащий именя всех файлов и папок в рабочей папке (на которую указывает pass_folder)
    for x in names:                                         # проходим по всем именам файлов из рабочей папки
        if x != "video_recorder.py" and x !="setting.txt":  # если имя файла из рабочей папки не равно исполняемому py файлу, то
            number_work_dir_list.append(x)                  # добавляем его имя в наш список рабочих папок и
    number_work_dir_list.sort()



# Функция, которая создает  рабочую папку  (не меняется)
def create_work_dir():

    global  path
    global  number_work_dir_list
    global  timestamp

    get_date_today() # узнаем текущую дату

    path = str(pass_folder) + "/" + timestamp      # Добавляем к выбранному адресу директории дату (она и будет имя типа папки "2019-03-25")


    if not os.path.exists(path):   # Проверяем, нет ли там уже этой папки, есть нет - создаем, если есть то не создаем
        os.makedirs(path)

        number_work_dir_list.append(timestamp)   # добавим имя новой папки с список рабочих папок, чтобы потом удалять :) хихи


 #Функция, которая узнает сегодняшнюю дату в формате год-месяц-день  (не меняется)
def  get_date_today():
    global timestamp
    timestamp = datetime.datetime.today().strftime('%Y-%m-%d')   # результат, например, "2019-03-25" в формате строки




# Функция узнает, сколько уже видеофайлов есть в текущей папке  (переделай под 4 камеры, 4 условия if будет, а не 1)
def get_number_of_videofiles():

   global num_vid_cam_1, num_vid_cam_2, num_vid_cam_3, num_vid_cam_4      # Счетчик видефайлов с камеры 1, задан в начале кода как 0


   num_vid_cam_1 = 0         # Число для счетки видео с камеры 1  (расширь на 4 камеры - num_vid_cam_2 и 3 и 4 и все равны 0)
   num_vid_cam_2 = 0
   num_vid_cam_3 = 0
   num_vid_cam_4 = 0

   names = os.listdir(path)  # Читаем все содержимое рабочей папки, результат - список, содержащий строки имен файлов, например, ['cam_1_0.avi', 'cam_2_0.avi', 'cam_3_0.avi', 'cam_4_0.avi']  т.е. в папке 4 ави файла по одному на каждую камеру


   for x in names:                # Походим по всем именам рабочей папки
        a=x.split("_")            # Разбиваем каждое имя по разделителю "_", следовательно строка  cam_1_0.avi  разобъется на список из таких элеменов a = ["cam", "1", "0.avi"], очевиедно что a[1] элемент этого списка это номер камеры с камеры
        if a[1] == "1":          # Если есть видос с первой камеры
            num_vid_cam_1 = num_vid_cam_1 + 1      # то увеличиваем счетчик на 1
        if a[1] == "2":          # Если есть видос с первой камеры
            num_vid_cam_2 = num_vid_cam_2 + 1      # то увеличиваем счетчик на 1
        if a[1] == "3":          # Если есть видос с первой камеры
            num_vid_cam_3 = num_vid_cam_3 + 1      # то увеличиваем счетчик на 1
        if a[1] == "4":          # Если есть видос с первой камеры
            num_vid_cam_4 = num_vid_cam_4 + 1      # то увеличиваем счетчик на 1



# Функция настроек камер  (под 4 камеры переделали ранее)
def camera_setting():

    global  path, fps_cam


    global width_cam_1, height_cam_1, width_wind_cam_1, height_wind_cam_1, cap1, color_mod_cam_1, res_wind_cam_1    # делаем частоту кадров, ширину и высоту кадра камеры глобальными, что использовать при записи видео на диск
    global out1, num_vid_cam_1, status_camera_1, fourcc1

    global width_cam_2, height_cam_2, width_wind_cam_2, height_wind_cam_2, cap2, color_mod_cam_2, res_wind_cam_2    # делаем частоту кадров, ширину и высоту кадра камеры глобальными, что использовать при записи видео на диск
    global out2, num_vid_cam_2, status_camera_2, fourcc2

    global width_cam_3, height_cam_3, width_wind_cam_3, height_wind_cam_3, cap3, color_mod_cam_3, res_wind_cam_3    # делаем частоту кадров, ширину и высоту кадра камеры глобальными, что использовать при записи видео на диск
    global out3, num_vid_cam_3, status_camera_3, fourcc3

    global width_cam_4, height_cam_4, width_wind_cam_4, height_wind_cam_4, cap4, color_mod_cam_4, res_wind_cam_4    # делаем частоту кадров, ширину и высоту кадра камеры глобальными, что использовать при записи видео на диск
    global out4, num_vid_cam_4, status_camera_4, fourcc4




    def_cam_count = QCom15.currentText()              # узнаем, сколько камер стоит помимо нашей камеры
    number_camera = int(def_cam_count)              # узнаем номер, по которому будет включать нашу камеру
    fps_cam = int(QCom13.currentText())             # узнаем частоту кадров и делаем её int




    status_camera_1 = QCom2.currentText()           # Узнаетм статус камеры (Enable или Disable)

    if status_camera_1 == "Disable":
        capp1 = cv2.VideoCapture(number_camera)
        if (capp1.isOpened()== True):        # Если камера 1  подключена
            number_camera = number_camera + 1
            capp1.release()

    if status_camera_1 == "Enable":                 # Будем юзать камеру, только если юзер выбрал Enable


        res_cam_1 = QCom1.currentText()                         # узнаем разрешение камеры как строку
        res_cam_1_list = res_cam_1.split('x')                   # разбиваем строку на высоту и ширину кадра используя разделитель "x"
        width_cam_1 = int(res_cam_1_list[0])                    # получаем ширину кадра и делаем её int
        height_cam_1 = int(res_cam_1_list[1])                   # получаем высоту кадра и делаем её int



        color_mod_cam_1 = QCom3.currentText()                   # узнаем режим цветности камеры, который выбрал юзер
        if color_mod_cam_1 ==  "Grayscale":                     # если выбрал чб, то
            color_mod_cam_1 = 6                                 # такой формат   черн бел, то же что и cv2.COLOR_BGR2GRAY
        if color_mod_cam_1 ==   "RGB":                          # если выбрал РГБ, то
            color_mod_cam_1 = 0                                 # то формат 0, что значит обычное цветное изображение



        res_wind_cam_1 =  QCom16.currentText()                  # узнаем разрешение, в котором видео будет показываться в окне (оно может не совпадаеть с разрешением, с которым сама камера выдает картинку)
        if res_wind_cam_1 == "Default":                         # если выбрано По умолчанию, то картинка будет выводится на экран с тем же разрешенимем, что установлено у камеры
           width_wind_cam_1 =  width_cam_1                      # просто приравниваем его к ширине кадра камеры
           height_wind_cam_1 = height_cam_1                     # просто приравниваем его к высоте кадра камеры
        else:                                                   # если выбрано не По умолчанию
           res_wind_cam_1_list = res_wind_cam_1.split('x')      # разбиваем строку разрешения (там либо 320x240 либо 640x480)
           width_wind_cam_1 = int(res_wind_cam_1_list[0])       # достаем ширину окна, где будет видео с камеры
           height_wind_cam_1 = int(res_wind_cam_1_list[1])      # достаем высоту откна, где будет видео с камеры


        cap1 = cv2.VideoCapture(number_camera)                # создаем видео поток камеры 1 используя её номер
        number_camera = number_camera + 1                   # инкремируем номер камеры
        cap1.set(cv2.CAP_PROP_FRAME_WIDTH, width_cam_1)         # задаем ширину кадра камеры
        cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, height_cam_1)       # задаем высоту кадра камеры
        cap1.set(cv2.CAP_PROP_FPS, fps_cam)                   # задаем fps камеры


        fourcc1 = cv2.VideoWriter_fourcc(*'XVID')                       # Выбираем сжатие  MJPG
        out1 = cv2.VideoWriter(path +"/"+ "cam_1_" + str(num_vid_cam_1)+".avi", fourcc1, fps_cam, (width_cam_1,height_cam_1))   # Создаетм avi файл, для записи в него видео с камеры, задав путь к файлу и имя, сжатие, частоту кадров и разрешение кадра


################   2 КАМЕРА   #########################


    status_camera_2 = QCom5.currentText()           # Узнаетм статус камеры (Enable или Disable)

    if status_camera_2 == "Disable":
        capp2 = cv2.VideoCapture(number_camera)
        if (capp2.isOpened()== True):               # Если камера 2  подключена
            number_camera = number_camera + 1
            capp2.release()


    if status_camera_2 == "Enable":                 # Будем юзать камеру, только если юзер выбрал Enable


        res_cam_2 = QCom4.currentText()                         # узнаем разрешение камеры как строку
        res_cam_2_list = res_cam_2.split('x')                   # разбиваем строку на высоту и ширину кадра используя разделитель "x"
        width_cam_2 = int(res_cam_2_list[0])                    # получаем ширину кадра и делаем её int
        height_cam_2 = int(res_cam_2_list[1])                   # получаем высоту кадра и делаем её int



        color_mod_cam_2 = QCom6.currentText()                   # узнаем режим цветности камеры, который выбрал юзер
        if color_mod_cam_2 ==  "Grayscale":                     # если выбрал чб, то
            color_mod_cam_2 = 6                                 # такой формат   черн бел, то же что и cv2.COLOR_BGR2GRAY
        if color_mod_cam_2 ==   "RGB":                          # если выбрал РГБ, то
            color_mod_cam_2 = 0                                 # то формат 0, что значит обычное цветное изображение



        res_wind_cam_2 =  QCom16.currentText()                  # узнаем разрешение, в котором видео будет показываться в окне (оно может не совпадаеть с разрешением, с которым сама камера выдает картинку)
        if res_wind_cam_2 == "Default":                         # если выбрано По умолчанию, то картинка будет выводится на экран с тем же разрешенимем, что установлено у камеры
           width_wind_cam_2 =  width_cam_2                      # просто приравниваем его к ширине кадра камеры
           height_wind_cam_2 = height_cam_2                    # просто приравниваем его к высоте кадра камеры
        else:                                                   # если выбрано не По умолчанию
           res_wind_cam_2_list = res_wind_cam_2.split('x')      # разбиваем строку разрешения (там либо 320x240 либо 640x480)
           width_wind_cam_2 = int(res_wind_cam_2_list[0])       # достаем ширину окна, где будет видео с камеры
           height_wind_cam_2 = int(res_wind_cam_2_list[1])      # достаем высоту откна, где будет видео с камеры


        cap2 = cv2.VideoCapture(number_camera)                # создаем видео поток камеры 1 используя её номер
        number_camera = number_camera + 1                   # инкремируем номер камеры
        cap2.set(cv2.CAP_PROP_FRAME_WIDTH, width_cam_2)         # задаем ширину кадра камеры
        cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, height_cam_2)       # задаем высоту кадра камеры
        cap2.set(cv2.CAP_PROP_FPS, fps_cam)                   # задаем fps камеры

        fourcc2 = cv2.VideoWriter_fourcc(*'XVID')                       # Выбираем сжатие  MJPG
        out2 = cv2.VideoWriter(path +"/"+ "cam_2_" + str(num_vid_cam_2)+".avi", fourcc2, fps_cam, (width_cam_2,height_cam_2))   # Создаетм avi файл, для записи в него видео с камеры, задав путь к файлу и имя, сжатие, частоту кадров и разрешение кадра





################   3 КАМЕРА   #########################


    status_camera_3 = QCom8.currentText()           # Узнаетм статус камеры (Enable или Disable)

    if status_camera_3 == "Disable":
        capp3 = cv2.VideoCapture(number_camera)
        if (capp3.isOpened()== True):               # Если камера 3  подключена
            number_camera = number_camera + 1
            capp3.release()



    if status_camera_3 == "Enable":                 # Будем юзать камеру, только если юзер выбрал Enable


        res_cam_3 = QCom7.currentText()                         # узнаем разрешение камеры как строку
        res_cam_3_list = res_cam_3.split('x')                   # разбиваем строку на высоту и ширину кадра используя разделитель "x"
        width_cam_3 = int(res_cam_3_list[0])                    # получаем ширину кадра и делаем её int
        height_cam_3 = int(res_cam_3_list[1])                   # получаем высоту кадра и делаем её int



        color_mod_cam_3 = QCom9.currentText()                   # узнаем режим цветности камеры, который выбрал юзер
        if color_mod_cam_3 ==  "Grayscale":                     # если выбрал чб, то
            color_mod_cam_3 = 6                                 # такой формат   черн бел, то же что и cv2.COLOR_BGR2GRAY
        if color_mod_cam_3 ==   "RGB":                          # если выбрал РГБ, то
            color_mod_cam_3 = 0                                 # то формат 0, что значит обычное цветное изображение



        res_wind_cam_3 =  QCom16.currentText()                  # узнаем разрешение, в котором видео будет показываться в окне (оно может не совпадаеть с разрешением, с которым сама камера выдает картинку)
        if res_wind_cam_3 == "Default":                         # если выбрано По умолчанию, то картинка будет выводится на экран с тем же разрешенимем, что установлено у камеры
           width_wind_cam_3 =  width_cam_3                      # просто приравниваем его к ширине кадра камеры
           height_wind_cam_3 = height_cam_3                    # просто приравниваем его к высоте кадра камеры
        else:                                                   # если выбрано не По умолчанию
           res_wind_cam_3_list = res_wind_cam_3.split('x')      # разбиваем строку разрешения (там либо 320x240 либо 640x480)
           width_wind_cam_3 = int(res_wind_cam_3_list[0])       # достаем ширину окна, где будет видео с камеры
           height_wind_cam_3 = int(res_wind_cam_3_list[1])      # достаем высоту откна, где будет видео с камеры


        cap3 = cv2.VideoCapture(number_camera)                # создаем видео поток камеры 1 используя её номер
        number_camera = number_camera + 1                   # инкремируем номер камеры
        cap3.set(cv2.CAP_PROP_FRAME_WIDTH, width_cam_3)         # задаем ширину кадра камеры
        cap3.set(cv2.CAP_PROP_FRAME_HEIGHT, height_cam_3)       # задаем высоту кадра камеры
        cap3.set(cv2.CAP_PROP_FPS, fps_cam)                   # задаем fps камеры


        fourcc3 = cv2.VideoWriter_fourcc(*'XVID')                       # Выбираем сжатие  MJPG
        out3 = cv2.VideoWriter(path +"/"+ "cam_3_" + str(num_vid_cam_3)+".avi", fourcc3, fps_cam, (width_cam_3,height_cam_3))   # Создаетм avi файл, для записи в него видео с камеры, задав путь к файлу и имя, сжатие, частоту кадров и разрешение кадра



################   4 КАМЕРА   #########################



    status_camera_4 = QCom11.currentText()           # Узнаетм статус камеры (Enable или Disable)

    if status_camera_4 == "Disable":
        capp4 = cv2.VideoCapture(number_camera)
        if (capp4.isOpened()== True):               # Если камера 3  подключена
            number_camera = number_camera + 1
            capp4.release()



    if status_camera_4 == "Enable":                 # Будем юзать камеру, только если юзер выбрал Enable


        res_cam_4 = QCom10.currentText()                         # узнаем разрешение камеры как строку
        res_cam_4_list = res_cam_4.split('x')                   # разбиваем строку на высоту и ширину кадра используя разделитель "x"
        width_cam_4 = int(res_cam_4_list[0])                    # получаем ширину кадра и делаем её int
        height_cam_4 = int(res_cam_4_list[1])                   # получаем высоту кадра и делаем её int



        color_mod_cam_4 = QCom12.currentText()                   # узнаем режим цветности камеры, который выбрал юзер
        if color_mod_cam_4 ==  "Grayscale":                     # если выбрал чб, то
            color_mod_cam_4 = 6                                 # такой формат   черн бел, то же что и cv2.COLOR_BGR2GRAY
        if color_mod_cam_4 ==   "RGB":                          # если выбрал РГБ, то
            color_mod_cam_4 = 0                                 # то формат 0, что значит обычное цветное изображение



        res_wind_cam_4 =  QCom16.currentText()                  # узнаем разрешение, в котором видео будет показываться в окне (оно может не совпадаеть с разрешением, с которым сама камера выдает картинку)
        if res_wind_cam_4 == "Default":                         # если выбрано По умолчанию, то картинка будет выводится на экран с тем же разрешенимем, что установлено у камеры
           width_wind_cam_4 =  width_cam_4                     # просто приравниваем его к ширине кадра камеры
           height_wind_cam_4 = height_cam_4                    # просто приравниваем его к высоте кадра камеры
        else:                                                   # если выбрано не По умолчанию
           res_wind_cam_4_list = res_wind_cam_4.split('x')      # разбиваем строку разрешения (там либо 320x240 либо 640x480)
           width_wind_cam_4 = int(res_wind_cam_4_list[0])       # достаем ширину окна, где будет видео с камеры
           height_wind_cam_4 = int(res_wind_cam_4_list[1])      # достаем высоту откна, где будет видео с камеры


        cap4 = cv2.VideoCapture(number_camera)                # создаем видео поток камеры 1 используя её номер
        number_camera = number_camera + 1                   # инкремируем номер камеры
        cap4.set(cv2.CAP_PROP_FRAME_WIDTH, width_cam_4)         # задаем ширину кадра камеры
        cap4.set(cv2.CAP_PROP_FRAME_HEIGHT, height_cam_4)       # задаем высоту кадра камеры
        cap4.set(cv2.CAP_PROP_FPS, fps_cam)                   # задаем fps камеры



        fourcc4 = cv2.VideoWriter_fourcc(*'XVID')                       # Выбираем сжатие  MJPG
        out4 = cv2.VideoWriter(path +"/"+ "cam_4_" + str(num_vid_cam_4)+".avi", fourcc4, fps_cam, (width_cam_4,height_cam_4))   # Создаетм avi файл, для записи в него видео с камеры, задав путь к файлу и имя, сжатие, частоту кадров и разрешение кадра





# Функция запускает таймер с заданным временем   (не меняется)
def start_timer():
    global fps_cam # выбранная частота кадров первой камеры

    a = (1/(float(fps_cam)))*1000  # Переводим fps в миллисекунды
    timer.start(a) # Запуск таймера





# тоже изменить под 4 камеры будет 4 раза if status_camera_1 == "Enable":
def get_and_save_video():

    global path, timestamp, fps_cam


    global cap1, width_wind_cam_1, height_wind_cam_1, color_mod_cam_1, res_wind_cam_1
    global status_camera_1, out1, fourcc1, width_cam_1, height_cam_1

    global cap2, width_wind_cam_2, height_wind_cam_2, color_mod_cam_2, res_wind_cam_2
    global status_camera_2, out2, fourcc2, width_cam_2, height_cam_2

    global cap3, width_wind_cam_3, height_wind_cam_3, color_mod_cam_3, res_wind_cam_3
    global status_camera_3, out3, fourcc3, width_cam_3, height_cam_3

    global cap4, width_wind_cam_4, height_wind_cam_4, color_mod_cam_4, res_wind_cam_4
    global status_camera_4, out4, fourcc4, width_cam_4, height_cam_4



    timestamp1 = datetime.datetime.today().strftime('%Y-%m-%d')   # узнаем текущую дату, чтобы узнать, не наступил ли новый день с момента нажимания на старт


    if timestamp1 !=  timestamp:
        create_work_dir()                   # Если дата изменилась с момента нажатия на кнопку пуск, то нужно завершить все видео и создать новую папку  с именеим с новой датой
        if status_camera_1 == "Enable":     # Если камера 1 вообще используется
            out1.release()                  # Завершим запись видео в текущую папку
            out1 = cv2.VideoWriter(path +"/"+ "cam_1_" + "0" +".avi", fourcc1, fps_cam, (width_cam_1,height_cam_1))   # Создаетм avi файл номер видео 0, так как во вновь созданной папке видеофайлов быть не может
        if status_camera_2 == "Enable":     # Если камера 1 вообще используется
            out2.release()                  # Завершим запись видео в текущую папку
            out2 = cv2.VideoWriter(path +"/"+ "cam_2_" + "0" +".avi", fourcc2, fps_cam, (width_cam_2,height_cam_2))   # Создаетм avi файл номер видео 0, так как во вновь созданной папке видеофайлов быть не может
        if status_camera_3 == "Enable":     # Если камера 1 вообще используется
            out3.release()                  # Завершим запись видео в текущую папку
            out3 = cv2.VideoWriter(path +"/"+ "cam_3_" + "0" +".avi", fourcc3, fps_cam, (width_cam_3,height_cam_3))   # Создаетм avi файл номер видео 0, так как во вновь созданной папке видеофайлов быть не может
        if status_camera_4 == "Enable":     # Если камера 1 вообще используется
            out4.release()                  # Завершим запись видео в текущую папку
            out4 = cv2.VideoWriter(path +"/"+ "cam_4_" + "0" +".avi", fourcc4, fps_cam, (width_cam_4,height_cam_4))   # Создаетм avi файл номер видео 0, так как во вновь созданной папке видеофайлов быть не может





    if status_camera_1 == "Enable":     # Если камера 1 вообще используется

        ret1,frame1 = cap1.read()                            # читаем кадр    frame1 с камеры 1
        timestamp_for_frame = datetime.datetime.now()        # получаем текущую дату и время
        ts = timestamp_for_frame.strftime("%A %d %B %Y %I:%M:%S%p")   # делаем её в нужном формате (смотри на видео с камеры)
        cv2.putText(frame1, ts, (10, frame1.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)  # белым цветом буквами внизу слева кадра выводим таймстмп


        gray1 = cv2.cvtColor(frame1, color_mod_cam_1)  # делаем кадр frame серым или оставляем цветным (0 - цветной, 6 - серый)
        out1.write(gray1)


        if res_wind_cam_1 != "Default":    # если настрокие не по дефолту то меняем разрешение полученного кадра на размеры окна для отображения (либо 320 на 240 илбо 640 на 480)
            gray1 = cv2.resize(gray1, (width_wind_cam_1, height_wind_cam_1))



        cv2.imshow('Camera 1',gray1)


    if status_camera_2 == "Enable":     # Если камера 1 вообще используется

        ret2,frame2 = cap2.read()                            # читаем кадр    frame1 с камеры 1
        timestamp_for_frame = datetime.datetime.now()        # получаем текущую дату и время
        ts = timestamp_for_frame.strftime("%A %d %B %Y %I:%M:%S%p")   # делаем её в нужном формате (смотри на видео с камеры)
        cv2.putText(frame2, ts, (10, frame2.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)  # белым цветом буквами внизу слева кадра выводим таймстмп


        gray2 = cv2.cvtColor(frame2, color_mod_cam_2)  # делаем кадр frame серым или оставляем цветным (0 - цветной, 6 - серый)
        out2.write(gray2)


        if res_wind_cam_2 != "Default":    # если настрокие не по дефолту то меняем разрешение полученного кадра на размеры окна для отображения (либо 320 на 240 илбо 640 на 480)
            gray2 = cv2.resize(gray2, (width_wind_cam_2, height_wind_cam_2))



        cv2.imshow('Camera 2',gray2)


    if status_camera_3 == "Enable":     # Если камера 1 вообще используется

        ret3,frame3 = cap3.read()                            # читаем кадр    frame1 с камеры 1
        timestamp_for_frame = datetime.datetime.now()        # получаем текущую дату и время
        ts = timestamp_for_frame.strftime("%A %d %B %Y %I:%M:%S%p")   # делаем её в нужном формате (смотри на видео с камеры)
        cv2.putText(frame3, ts, (10, frame3.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)  # белым цветом буквами внизу слева кадра выводим таймстмп


        gray3 = cv2.cvtColor(frame3, color_mod_cam_3)  # делаем кадр frame серым или оставляем цветным (0 - цветной, 6 - серый)
        out3.write(gray3)


        if res_wind_cam_3 != "Default":    # если настрокие не по дефолту то меняем разрешение полученного кадра на размеры окна для отображения (либо 320 на 240 илбо 640 на 480)
            gray3 = cv2.resize(gray3, (width_wind_cam_3, height_wind_cam_3))



        cv2.imshow('Camera 3',gray3)



    if status_camera_4 == "Enable":     # Если камера 1 вообще используется

        ret4,frame4 = cap4.read()                            # читаем кадр    frame1 с камеры 1
        timestamp_for_frame = datetime.datetime.now()        # получаем текущую дату и время
        ts = timestamp_for_frame.strftime("%A %d %B %Y %I:%M:%S%p")   # делаем её в нужном формате (смотри на видео с камеры)
        cv2.putText(frame4, ts, (10, frame4.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)  # белым цветом буквами внизу слева кадра выводим таймстмп


        gray4 = cv2.cvtColor(frame4, color_mod_cam_4)  # делаем кадр frame серым или оставляем цветным (0 - цветной, 6 - серый)
        out4.write(gray4)


        if res_wind_cam_4 != "Default":    # если настрокие не по дефолту то меняем разрешение полученного кадра на размеры окна для отображения (либо 320 на 240 илбо 640 на 480)
            gray4 = cv2.resize(gray4, (width_wind_cam_4, height_wind_cam_4))



        cv2.imshow('Camera 4',gray4)



# Функция останавливает таймер     (переделай под 4 камеры, будет 4 иф) будет 4 раза if
def stop_timer():

    global cap1, out1, cap2, out2, cap3, out3, cap4, out4
    global status_camera_1, status_camera_2, status_camera_3, status_camera_4


    btn2.setEnabled(False)   # блокируется кнопка стоп
    btn3.setEnabled(True)   # активируется кнопка folderbrowser
    btn4.setEnabled(True)    # активируется кнопка setting
    btn5.setEnabled(True)    # активируется кнопка exit
    btn1.setEnabled(True)    # активируется кнопка старт



    if status_camera_1 == "Enable":     # Если камера 1 вообще используется
        cap1.release()
        out1.release()

    if status_camera_2 == "Enable":     # Если камера 2 вообще используется
        cap2.release()
        out2.release()

    if status_camera_3 == "Enable":     # Если камера 3 вообще используется
        cap3.release()
        out3.release()

    if status_camera_4 == "Enable":     # Если камера 4 вообще используется
        cap4.release()
        out4.release()


    cv2.destroyAllWindows()
    timer.stop()   # Остановка таймера


    #   Функция защита от дурака
def poka_yoke():

    global key_start_video

    key_start_video=True       # ключ проверки корректной работы камер


    camera_1_key_enable = True
    camera_2_key_enable = True
    camera_3_key_enable = True
    camera_4_key_enable = True


    status_camera_1 = QCom2.currentText()   # Узнаем статус 4 камер
    status_camera_2 = QCom5.currentText()
    status_camera_3 = QCom8.currentText()
    status_camera_4 = QCom11.currentText()


    if status_camera_1=="Disable" and  status_camera_2=="Disable" and status_camera_3=="Disable" and status_camera_4=="Disable":  # Если все камеры не активны
        key_start_video=False   # то ключ проверки прекращает в режиме Запрещено

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle("Attention!")
        msg.setText("All camers is disable!")
        retval = msg.exec_()



    else:

        def_cam_count = QCom15.currentText()              # узнаем, сколько камер стоит помимо нашей камеры
        number_camera = int(def_cam_count)              # узнаем номер, по которому будет включать нашу камеру


        if status_camera_1 == "Disable":
            capp1 = cv2.VideoCapture(number_camera)
            if (capp1.isOpened()== True):               # Если камера 1  подключена
                number_camera = number_camera + 1
                capp1.release()


        if status_camera_1 == "Enable":                 # Будем юзать камеру, только если юзер выбрал Enable


            res_cam_1 = QCom1.currentText()                         # узнаем разрешение камеры как строку
            res_cam_1_list = res_cam_1.split('x')                   # разбиваем строку на высоту и ширину кадра используя разделитель "x"
            width_cam_1 = int(res_cam_1_list[0])                    # получаем ширину кадра и делаем её int
            height_cam_1 = int(res_cam_1_list[1])                   # получаем высоту кадра и делаем её int

            cap1 = cv2.VideoCapture(number_camera)                  # создаем видео поток камеры 1 используя её номер
            number_camera = number_camera + 1                       # инкремируем номер камеры
            cap1.set(cv2.CAP_PROP_FRAME_WIDTH, width_cam_1)         # задаем ширину кадра камеры
            cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, height_cam_1)       # задаем высоту кадра камеры
            cap1.set(cv2.CAP_PROP_FPS, 5)                           # задаем fps=5 камеры


            if (cap1.isOpened()== False):        # Если камера 1 не подключена
                status_camera_1 = "Disable"      # Статус камеры 1 отключена

                QCom2.setCurrentIndex (1)             # статус камеры 1 disable, в окне setting

                camera_1_key_enable = False

                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Attention!")
                msg.setText("Camera 1 don't work!")
                retval = msg.exec_()



            else:
                ret,frame = cap1.read()

                h = frame.shape[0]
                w = frame.shape[1]

                if  w != width_cam_1 and h != height_cam_1:

                    status_camera_1 = "Disable"      # Статус камеры 1 отключена

                    QCom2.setCurrentIndex (1)             # статус камеры 1 disable, в окне setting
                    camera_1_key_enable = False



                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("Attention!")
                    msg.setText("Camera 1 don't support chosen resolution!")
                    retval = msg.exec_()




            cap1.release()



        if status_camera_2 == "Disable":
            capp2 = cv2.VideoCapture(number_camera)
            if (capp2.isOpened()== True):               # Если камера 2  подключена
                number_camera = number_camera + 1
                capp2.release()



        if status_camera_2 == "Enable":                 # Будем юзать камеру, только если юзер выбрал Enable


            res_cam_2 = QCom4.currentText()                         # узнаем разрешение камеры как строку
            res_cam_2_list = res_cam_2.split('x')                   # разбиваем строку на высоту и ширину кадра используя разделитель "x"
            width_cam_2 = int(res_cam_2_list[0])                    # получаем ширину кадра и делаем её int
            height_cam_2 = int(res_cam_2_list[1])                   # получаем высоту кадра и делаем её int


            cap2 = cv2.VideoCapture(number_camera)                   # создаем видео поток камеры 1 используя её номер
            number_camera = number_camera + 1                         # инкремируем номер камеры
            cap2.set(cv2.CAP_PROP_FRAME_WIDTH, width_cam_2)           # задаем ширину кадра камеры
            cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, height_cam_2)        # задаем высоту кадра камеры
            cap2.set(cv2.CAP_PROP_FPS, 5)                            # задаем fps камеры




            if (cap2.isOpened()== False):        # Если камера 2 не подключена
                status_camera_2 = "Disable"      # Статус камеры 2 отключена

                QCom5.setCurrentIndex (1)             # статус камеры 2 disable, в окне setting
                camera_2_key_enable = False

                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Attention!")
                msg.setText("Camera 2 don't work!")
                retval = msg.exec_()

            else:
                ret,frame = cap2.read()

                h = frame.shape[0]
                w = frame.shape[1]

                if  w != width_cam_2 and h != height_cam_2:

                    status_camera_2 = "Disable"      # Статус камеры 2 отключена

                    QCom5.setCurrentIndex (1)             # статус камеры 2 disable, в окне setting

                    camera_2_key_enable = False


                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("Attention!")
                    msg.setText("Camera 2 don't support chosen resolution!")
                    retval = msg.exec_()




            cap2.release()


        if status_camera_3 == "Disable":
            capp3 = cv2.VideoCapture(number_camera)
            if (capp3.isOpened()== True):               # Если камера 3  подключена
                number_camera = number_camera + 1
                capp3.release()



        if status_camera_3 == "Enable":                 # Будем юзать камеру, только если юзер выбрал Enable


            res_cam_3 = QCom7.currentText()                         # узнаем разрешение камеры как строку
            res_cam_3_list = res_cam_3.split('x')                   # разбиваем строку на высоту и ширину кадра используя разделитель "x"
            width_cam_3 = int(res_cam_3_list[0])                    # получаем ширину кадра и делаем её int
            height_cam_3 = int(res_cam_3_list[1])                   # получаем высоту кадра и делаем её int


            cap3 = cv2.VideoCapture(number_camera)                # создаем видео поток камеры 1 используя её номер
            number_camera = number_camera + 1                   # инкремируем номер камеры
            cap3.set(cv2.CAP_PROP_FRAME_WIDTH, width_cam_3)         # задаем ширину кадра камеры
            cap3.set(cv2.CAP_PROP_FRAME_HEIGHT, height_cam_3)       # задаем высоту кадра камеры
            cap3.set(cv2.CAP_PROP_FPS, 5)                           # задаем fps камеры


            if (cap3.isOpened()== False):        # Если камера 3 не подключена
                status_camera_3 = "Disable"      # Статус камеры 3 отключена

                QCom8.setCurrentIndex (1)             # статус камеры 3 disable, в окне setting

                camera_3_key_enable = False


                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Attention!")
                msg.setText("Camera 3 don't work!")
                retval = msg.exec_()

            else:
                ret,frame = cap3.read()

                h = frame.shape[0]
                w = frame.shape[1]

                if  w != width_cam_3 and h != height_cam_3:

                    status_camera_3 = "Disable"      # Статус камеры 3 отключена

                    QCom8.setCurrentIndex (1)             # статус камеры 3 disable, в окне setting

                    camera_3_key_enable = False


                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("Attention!")
                    msg.setText("Camera 3 don't support chosen resolution!")
                    retval = msg.exec_()

            cap3.release()



        if status_camera_4 == "Disable":
            capp4 = cv2.VideoCapture(number_camera)
            if (capp4.isOpened()== True):               # Если камера 4  подключена
                number_camera = number_camera + 1
                capp4.release()



        if status_camera_4 == "Enable":                 # Будем юзать камеру, только если юзер выбрал Enable


            res_cam_4 = QCom10.currentText()                         # узнаем разрешение камеры как строку
            res_cam_4_list = res_cam_4.split('x')                   # разбиваем строку на высоту и ширину кадра используя разделитель "x"
            width_cam_4 = int(res_cam_4_list[0])                    # получаем ширину кадра и делаем её int
            height_cam_4 = int(res_cam_4_list[1])                   # получаем высоту кадра и делаем её int


            cap4 = cv2.VideoCapture(number_camera)                # создаем видео поток камеры 1 используя её номер
            number_camera = number_camera + 1                   # инкремируем номер камеры
            cap4.set(cv2.CAP_PROP_FRAME_WIDTH, width_cam_4)         # задаем ширину кадра камеры
            cap4.set(cv2.CAP_PROP_FRAME_HEIGHT, height_cam_4)       # задаем высоту кадра камеры
            cap4.set(cv2.CAP_PROP_FPS, 5)                   	# задаем fps камеры



            if (cap4.isOpened()== False):        # Если камера 4 не подключена
                status_camera_4 = "Disable"      # Статус камеры 4 отключена

                QCom11.setCurrentIndex (1)             # статус камеры 4 disable, в окне setting

                camera_4_key_enable = False

                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Attention!")
                msg.setText("Camera 4 don't work!")
                retval = msg.exec_()


            else:
                ret,frame = cap4.read()

                h = frame.shape[0]
                w = frame.shape[1]



                if  w != width_cam_4 and h != height_cam_4:

                    status_camera_4 = "Disable"      # Статус камеры 4 отключена

                    QCom11.setCurrentIndex (1)             # статус камеры 4 disable, в окне setting

                    camera_4_key_enable = False


                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("Attention!")
                    msg.setText("Camera 4 don't support chosen resolution!")
                    retval = msg.exec_()

            cap4.release()


        if camera_1_key_enable == False or  camera_2_key_enable == False or camera_3_key_enable == False or camera_4_key_enable == False:  # Если все камеры не активны
            key_start_video=False   # то ключ проверки прекращает в режиме Запрещено



##  Содержимое окна второго setting
#ОКНО КАМЕРЫ 1
 # Подписи Для камеры 1
lb1 = QtWidgets.QLabel('Set resolution')
lb2 = QtWidgets.QLabel('Status camera (on/off)')
lb3 = QtWidgets.QLabel('Image setup')

   # Разрешение камеры 1
QCom1 = QtWidgets.QComboBox()
QCom1.addItem("320x240")
QCom1.addItem("640x480")
QCom1.addItem("800x600")
QCom1.addItem("1024x768")
QCom1.addItem("1280x1024")
QCom1.addItem("1920x1080")


    # Состояние камеры 1
QCom2 = QtWidgets.QComboBox()
QCom2.addItem("Enable")
QCom2.addItem("Disable")


   # Режим цветности камеры 1
QCom3 = QtWidgets.QComboBox()
QCom3.addItem("Grayscale")
QCom3.addItem("RGB")






 # Создаем сетку для первого групбокса и закидываем туда виджиты
layout1 = QtWidgets.QGridLayout()
layout1.addWidget(lb1, 0, 0)
layout1.addWidget(QCom1, 0, 1)
layout1.addWidget(lb2, 1, 0)
layout1.addWidget(QCom2, 1, 1)
layout1.addWidget(lb3, 2, 0)
layout1.addWidget(QCom3, 2, 1)




# Закидываем все виджеты первой камеры в группобкс с подписью Камера 1
box1 = QtWidgets.QGroupBox("Camera 1")
box1.setLayout(layout1)



#ОКНО КАМЕРЫ 2
# Подписи Для камеры 2
lb4 = QtWidgets.QLabel('Set resolution')
lb5 = QtWidgets.QLabel('Status camera (on/off)')
lb6 = QtWidgets.QLabel('Image setup')

# Разрешение камеры 2
QCom4 = QtWidgets.QComboBox()
QCom4.addItem("320x240")
QCom4.addItem("640x480")
QCom4.addItem("800x600")
QCom4.addItem("1024x768")
QCom4.addItem("1280x1024")
QCom4.addItem("1920x1080")


# Состояние камеры 2
QCom5 = QtWidgets.QComboBox()
QCom5.addItem("Enable")
QCom5.addItem("Disable")


# Режим цветности камеры 2
QCom6 = QtWidgets.QComboBox()
QCom6.addItem("Grayscale")
QCom6.addItem("RGB")






# Создаем сетку для второго групбокса и закидываем туда виджиты
layout2 = QtWidgets.QGridLayout()
layout2.addWidget(lb4, 3, 0)
layout2.addWidget(QCom4, 3, 1)
layout2.addWidget(lb5, 4, 0)
layout2.addWidget(QCom5, 4, 1)
layout2.addWidget(lb6, 5, 0)
layout2.addWidget(QCom6, 5, 1)




# Закидываем все виджеты второй камеры в группобкс с подписью Камера 2
box2 = QtWidgets.QGroupBox("Camera 2")
box2.setLayout(layout2)


#ОКНО КАМЕРЫ 3
# Подписи Для камеры 3
lb7 = QtWidgets.QLabel('Set resolution')
lb8 = QtWidgets.QLabel('Status camera (on/off)')
lb9 = QtWidgets.QLabel('Image setup')

# Разрешение камеры 3
QCom7 = QtWidgets.QComboBox()
QCom7.addItem("320x240")
QCom7.addItem("640x480")
QCom7.addItem("800x600")
QCom7.addItem("1024x768")
QCom7.addItem("1280x1024")
QCom7.addItem("1920x1080")


# Состояние камеры 3
QCom8 = QtWidgets.QComboBox()
QCom8.addItem("Enable")
QCom8.addItem("Disable")


# Режим цветности камеры 3
QCom9 = QtWidgets.QComboBox()
QCom9.addItem("Grayscale")
QCom9.addItem("RGB")




# Создаем сетку для третьего групбокса и закидываем туда виджиты
layout3 = QtWidgets.QGridLayout()
layout3.addWidget(lb7, 6, 0)
layout3.addWidget(QCom7, 6, 1)
layout3.addWidget(lb8, 7, 0)
layout3.addWidget(QCom8, 7, 1)
layout3.addWidget(lb9, 8, 0)
layout3.addWidget(QCom9, 8, 1)




# Закидываем все виджеты третьей камеры в группобкс с подписью Камера 3
box3 = QtWidgets.QGroupBox("Camera 3")
box3.setLayout(layout3)



#ОКНО КАМЕРЫ 4
# Подписи Для камеры 4
lb10 = QtWidgets.QLabel('Set resolution')
lb11 = QtWidgets.QLabel('Status camera (on/off)')
lb12 = QtWidgets.QLabel('Image setup')

# Разрешение камеры 4
QCom10 = QtWidgets.QComboBox()
QCom10.addItem("320x240")
QCom10.addItem("640x480")
QCom10.addItem("800x600")
QCom10.addItem("1024x768")
QCom10.addItem("1280x1024")
QCom10.addItem("1920x1080")


# Состояние камеры 4
QCom11 = QtWidgets.QComboBox()
QCom11.addItem("Enable")
QCom11.addItem("Disable")


# Режим цветности камеры 4
QCom12 = QtWidgets.QComboBox()
QCom12.addItem("Grayscale")
QCom12.addItem("RGB")






# Создаем сетку для четвертого групбокса и закидываем туда виджиты
layout4 = QtWidgets.QGridLayout()
layout4.addWidget(lb10, 9, 0)
layout4.addWidget(QCom10, 9, 1)
layout4.addWidget(lb11, 10, 0)
layout4.addWidget(QCom11, 10, 1)
layout4.addWidget(lb12, 11, 0)
layout4.addWidget(QCom12, 11, 1)




# Закидываем все виджеты четвертой камеры в группобкс с подписью Камера 4
box4 = QtWidgets.QGroupBox("Camera 4")
box4.setLayout(layout4)



#ОБЩЕЕ ОКНО ДЛЯ ВСЕХ КАМЕР

# Подписи Для ВСЕХ КАМЕР
lb13 = QtWidgets.QLabel('Frame rate')
lb14 = QtWidgets.QLabel('File storage time')
lb15 = QtWidgets.QLabel('Default camera count')
lb16 = QtWidgets.QLabel('Resolution to display')


# ЧАСТОТА КАДРОВ
QCom13 = QtWidgets.QComboBox()
QCom13.addItem("1")
QCom13.addItem("3")
QCom13.addItem("5")
QCom13.addItem("10")
QCom13.addItem("15")



# ВРЕМЯ ХРАНЕНИЯ ФАЙЛОВ
QCom14 = QtWidgets.QComboBox()
QCom14.addItem("1")
QCom14.addItem("2")
QCom14.addItem("3")
QCom14.addItem("7")


# Изначальное количество имеющихся камер
QCom15 = QtWidgets.QComboBox()
QCom15.addItem("0")
QCom15.addItem("1")
QCom15.addItem("2")
QCom15.addItem("3")
QCom15.addItem("4")
QCom15.addItem("5")
QCom15.addItem("6")
QCom15.addItem("7")




# Разрешение видео, которое выводится на экран
QCom16 = QtWidgets.QComboBox()
QCom16.addItem("Default")
QCom16.addItem("320x240")
QCom16.addItem("640x480")



# Создаем сетку для пятого групбокса и закидываем туда виджиты
layout5 = QtWidgets.QGridLayout()
layout5.addWidget(lb13, 12, 0)
layout5.addWidget(QCom13, 12, 1)
layout5.addWidget(lb14, 13, 0)
layout5.addWidget(QCom14, 13, 1)
layout5.addWidget(lb15, 14, 0)
layout5.addWidget(QCom15, 14, 1)
layout5.addWidget(lb16, 15, 0)
layout5.addWidget(QCom16, 15, 1)





# Закидываем все виджеты в группобкс с подписью Для всех камер
box5 = QtWidgets.QGroupBox("For all camers")
box5.setLayout(layout5)


# Создаем кнопки
btn1 = QtWidgets.QPushButton('Ok')
btn1.clicked.connect(set_user_sett)
btn2 = QtWidgets.QPushButton('Default')
btn2.clicked.connect(set_default_sett)
btn3 = QtWidgets.QPushButton('Cancel')
btn3.clicked.connect(close_sett_wind)




# Создаем  первое окно и даем ему имя
second_window = QtWidgets.QWidget()
second_window .setWindowTitle('Setting')




# Упаковываем все в окно
layout24 = QtWidgets.QGridLayout()
second_window.setLayout(layout24)

layout24.addWidget(box1, 0, 0, 1, 2)
layout24.addWidget(box2, 1, 0, 1, 2)
layout24.addWidget(box3, 2, 0, 1, 2)
layout24.addWidget(box4, 3, 0, 1, 2)
layout24.addWidget(box5, 4, 0, 1, 2)

layout24.addWidget(btn1, 5, 0, 1, 2)
layout24.addWidget(btn2, 6, 0)
layout24.addWidget(btn3, 6, 1)




##  Содержимое окна control

# Создаем  первое окно и даем ему имя
first_window = QtWidgets.QWidget()
first_window .setWindowTitle('Control')


##

# Создаем первую кнопку и даем ей имя
btn1 = QtWidgets.QPushButton('Start')
btn1.clicked.connect(start_video_record)

# Создаем вторую кнопку и даем ей имя
btn2 = QtWidgets.QPushButton('Stop')
btn2.clicked.connect(stop_timer)

# Создаем третью кнопку и даем ей имя
btn3 = QtWidgets.QPushButton('FolderBrowser')
btn3.clicked.connect(select_folder)

# Создаем четвертую кнопку и даем ей имя
btn4 = QtWidgets.QPushButton('Setting')
btn4.clicked.connect(setting_window_show)

# Создаем пятую кнопку и даем ей имя
btn5 = QtWidgets.QPushButton('Exit')
btn5.clicked.connect(close_control_wind)



##      Затем виджеты помещаются на окна (тут 2 кнопки на первое окно)
##

# Создаем сетку для упакови кнопок Start и Stop в первый группбокс
layout1 = QtWidgets.QGridLayout()
layout1.addWidget(btn1, 0, 0) # Кладем первую кнопку в нулевую строку и нулевой столбец
layout1.addWidget(btn2, 1,0) # Кладем вторую кнопку в первую строку и нулевой столбец

# Создаем группбокс для упакови кнопок старт и стоп
box1 = QtWidgets.QGroupBox("Record control")
box1.setLayout(layout1)



# Создаем сетку для упакови кнопок FolderBrowser и Setting во второй группбокс
layout2 = QtWidgets.QGridLayout()
layout2.addWidget(btn3, 0,1) # Кладем третью кнопку в нулевую строку и первый столбец
layout2.addWidget(btn4, 1,1) # Кладем четвертую кнопку в первую строку и первый столбец

# Создаем группбокс Programm control для упакови кнопок FolderBrowser и Setting
box2 = QtWidgets.QGroupBox("Programm control")
box2.setLayout(layout2)



# Создаем сетку для упакови кнопки Exit в третий группбокс
layout3 = QtWidgets.QGridLayout()
layout3.addWidget(btn5, 0,2) # Кладем пятую кнопку в нулевую строку и второйй столбец

# Создаем группбокс для упакови кнопки Exit
box3 = QtWidgets.QGroupBox("")
box3.setLayout(layout3)



# Упаковываем все в окно
layout14 = QtWidgets.QGridLayout()
first_window.setLayout(layout14)
layout14.addWidget(box1, 0,0)
layout14.addWidget(box2, 0,1)
layout14.addWidget(box3, 0,2)


##    Закончили наполнять окна
##------------------------------------------












# Создаем таймер  timer1
timer = QtCore.QTimer()
timer.timeout.connect(get_and_save_video)  # Через заданные промежутки времени он, будучи включен, будет вызывать функцию increment





# Отображет первое окно
first_window.show()






start_program()


btn2.setEnabled(False)  # блокируем кнопку стоп



# Запуск опросника всех элементов окон Qt
# Курсор выполнения программы должен быть тут, чтобы окна работали корректно
app.exec_()






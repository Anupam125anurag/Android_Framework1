from robot.api.deco import keyword
from uiautomator import Device
from locators import settings_locators
#import yaml
import os
import time

ROBOT_AUTO_KEYWORDS = False

#configure = yaml.safe_load(open('test_data.yaml'))
#devicename = configure['Device_Serial']['Serial']
d = Device("98171FFBA00462", adb_server_host='127.0.0.1', adb_server_port=5037)

@keyword
def START_TEST():
    try:
        wakeup_device()
        time.sleep(2)
        #os.system("adb logcat > E:\sample.txt")
        time.sleep(4)
        return True
    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def END_TEST():
    
    close_app()
    time.sleep(1)
    go_to_home()
    return "Closing the tests"

@keyword
def GET_DEVINFO():
    try:
        return d.info
    except Exception as e:
        print("Exception Occured:",str(e))

@keyword
def GET_BUILD_ID():
    try:
        build_id = os.popen("adb shell getprop ro.build.id").read()
        return build_id
    except Exception as e:
        print("Exception occured: ", str(e))
        return False
@keyword
def GET_DEVICE_NAME():
    try:
        dev_name = os.popen("adb shell getprop ro.product.device").read()
        print(dev_name)
        return dev_name
    except Exception as e:
        print("Exception occured: ", str(e))
        return False
@keyword
def GET_DEVICE_MODEL():
    try:
        dev_model = os.popen("adb shell getprop ro.product.model").read()
        return dev_model
    except Exception as e:
        print("Exception occured: ", str(e))
        return False
@keyword
def GET_ANDROID_VERSION():
    try:
        android_version = os.popen("adb shell getprop ro.build.version.release").read()
        return android_version
    except Exception as e:
        print("Exception occured: ", str(e))
        return False

def swipe_screen():
    try:
        d.screen.on()
        size = d.info
        x = size['displayWidth'] / 2
        y = size['displayHeight'] / 2
        yl = size['displayHeight'] - 25
        d.swipe(x, y, x, -yl)

    except Exception as e:
        print("Exception Occured:", str(e))
        return False

def go_to_home():
        try:
            d.press.home()
        except Exception as e:
            print("Exception Occured:", str(e))
            return False


def launch_app(appname):
    try:

        swipe_screen()
        time.sleep(2)
        el = d(text=appname)
        check = el.wait.exists(timeout=3000)
        if check:
            el.click()
        else:
            if GET_DEVICE_NAME()=="msmnile\n":
               click_on("Search apps","android.widget.EditText")
            elif GET_DEVICE_NAME()=="coral\n":
               click_on_id("com.google.android.apps.nexuslauncher:id/input",
                            "android.widget.EditText")
            time.sleep(2)
            os.system("adb shell input text"+ " " + appname)
            time.sleep(3)
            d(text=appname,className="android.widget.TextView").click()
            time.sleep(2)
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False


def click_on(element_text,element_class):
    element = d(text=element_text,className=element_class)
    element.click()

def click_on_id(resource_id,class_name):
    element = d(resourceId=resource_id,className=class_name)
    element.click()

def wakeup_device():
    d.wakeup()

def element_exists(text_element, id_element):
    element = d(text=text_element, resourceId=id_element)
    if element.exists:
        return True
    else:
        return False

def element_exists_by_id_class(id_element, class_element):
    element = d(resourceId=id_element, className=class_element)
    if element.exists:
        return True
    else:
        return False

def click_on_text_id(ele_text, ele_id):
    element = d(text=ele_text, resourceId=ele_id)
    element.click()

def open_quick_settings():
    d.open.quick_settings()

#----

def enter_text(text):
    os.system("adb shell input text {text}")

def go_back():
    try:
        d.press.back()
        return True
    except Exception as e:
        print("Exception occured: ",str(e))
        return False
def open_recent_apps():
    try:
        d.press(187)
        return True
    except Exception as e:
        print("Exception occured: ",str(e))
        return False
def launch_quick_settings():
    try:
        d.open.quick_settings()
        return True
    except Exception as e:
        print("Exception occured: ",str(e))
        return False
def open_notification():
    try:
        d.open.notification()
        return True
    except Exception as e:
        print("Exception occured: ",str(e))
        return False

def close_app(): #n refers to number of apps opened
    go_to_home()
    open_recent_apps()
    time.sleep(2)
    if GET_DEVICE_NAME()=="msmnile\n":
       time.sleep(1)
       while element_exists_by_id_class(settings_locators.recent_app_screen_id_for_qboard, settings_locators.recent_app_screen_class) == True:
               time.sleep(2)
               swipe_screen()
    elif GET_DEVICE_NAME()=="coral\n":
         time.sleep(1)
         while element_exists_by_id_class(settings_locators.recent_app_screen_id, settings_locators.recent_app_screen_class) == True:
               time.sleep(2)
               swipe_screen()
    
    

def check_existence_by_name(name,classname):
    return d(text=name, className = classname).exists

def check_existence_by_id(resource_id,class_name):
    return d(resource_ID=resource_id,className=class_name).exists

def swipe_from_left():
    try:
        #d.screen.on()
        #d(scrollable=True).scroll.horiz.backward().toEnd()
        size = d.info
        x = size['displayWidth']
        y = size['displayHeight'] / 2
        #yl = size['displayHeight'] - 25
        d.swipe(0, y, x, y)


    except Exception as e:
        print("Exception Occured:", str(e))
        return False


def take_screenshot(name):
    try:
        d.screenshot("/home/idm/HDK855/Screenshots/{name}.png")
        return True
    except Exception as e:
        print("Exception occured: ",str(e))
        return False





def long_click_by_text(name,class_name):
    d(text=name,className=class_name).long_click()

def find_element_by_scroll(name,class_name):
    if check_existence_by_name(name,class_name):
        return True
    else:
        while check_existence_by_name(name,class_name)!=True:
            d(scrollable=True).scroll(steps=10)
            time.sleep(2)
            if check_existence_by_name(name,class_name):
                break



#END_TEST()
#close_app()
#swipe_screen()



import base_lib
from robot.api.deco import keyword
from locators import settings_locators
import time
import os

ROBOT_AUTO_KEYWORDS = False

@keyword
def LAUNCH_SETTINGS():
    try:
        base_lib.launch_app(settings_locators.appname)
        return True

    except Exception as e:
        print("Exception occured: ",str(e))
        return False

@keyword
def ENABLE_WIFI():
    try:
        time.sleep(2)
        base_lib.click_on(settings_locators.network_option, settings_locators.settings_options_class_name)
        time.sleep(3)
        base_lib.click_on(settings_locators.internet_option, settings_locators.settings_options_class_name)
        time.sleep(2)
        result = base_lib.element_exists(settings_locators.status_off, settings_locators.wifi_click_switch_id)
        time.sleep(2)
        
        base_lib.click_on_id("android:id/switch_widget","android.widget.Switch")
        time.sleep(2)

        return True

    except Exception as e:
        print("Exception occured: ", str(e))
        return False

@keyword
def DISABLE_WIFI():
    try:
        time.sleep(2)
        base_lib.click_on(settings_locators.network_option, settings_locators.settings_options_class_name)
        time.sleep(3)
        base_lib.click_on(settings_locators.internet_option, settings_locators.settings_options_class_name)
        time.sleep(2)
        result = base_lib.element_exists(settings_locators.status_on, settings_locators.wifi_click_switch_id)
        time.sleep(2)
        
        base_lib.click_on_id("android:id/switch_widget","android.widget.Switch")
        time.sleep(2)

        return True

    except Exception as e:
        print("Exception occured: ", str(e))
        return False


@keyword
def ENABLE_BLUETOOTH():
    try:
        time.sleep(2)
        base_lib.click_on(settings_locators.connected_device_option, settings_locators.settings_options_class_name)
        time.sleep(3)
        base_lib.click_on(settings_locators.connection_preference_option, settings_locators.settings_options_class_name)
        time.sleep(2)
        base_lib.click_on(settings_locators.bluetooth_option, settings_locators.settings_options_class_name)
        time.sleep(2)
        result = base_lib.element_exists(settings_locators.status_off, settings_locators.wifi_click_switch_id)
        time.sleep(2)
        
        base_lib.click_on_id("android:id/switch_widget","android.widget.Switch")
        time.sleep(2)

        return True

    except Exception as e:
        print("Exception occured: ", str(e))
        return False


@keyword
def DISABLE_BLUETOOTH():
    try:
        time.sleep(2)
        base_lib.click_on(settings_locators.connected_device_option, settings_locators.settings_options_class_name)
        time.sleep(3)
        base_lib.click_on(settings_locators.connection_preference_option, settings_locators.settings_options_class_name)
        time.sleep(2)
        base_lib.click_on(settings_locators.bluetooth_option, settings_locators.settings_options_class_name)
        time.sleep(2)
        result = base_lib.element_exists(settings_locators.status_on, settings_locators.wifi_click_switch_id)
        time.sleep(2)
        
        base_lib.click_on_id("android:id/switch_widget","android.widget.Switch")
        time.sleep(2)

        return True

    except Exception as e:
        print("Exception occured: ", str(e))
        return False

@keyword
def OPEN_QUICK_SETTINGS():
    try:
        base_lib.open_quick_settings()
        return True
    except Exception as e:
        print("Exception occured: ", str(e))
        return False

@keyword
def VERIFY_BATTERY_SAVER_OPTION_AND_CLICK():
    try:
        OPEN_QUICK_SETTINGS()
        time.sleep(2)
        result = base_lib.element_exists(settings_locators.battery_saver_option, settings_locators.battery_saver_option_id)
        if result == True:
            base_lib.click_on_text_id(settings_locators.battery_saver_option, settings_locators.battery_saver_option_id)
            if base_lib.element_exists(settings_locators.battery_saver_turn_on_popup_text, settings_locators.battery_saver_turn_on_popup_id):
                base_lib.click_on_text_id(settings_locators.battery_saver_turn_on_popup_text, settings_locators.battery_saver_turn_on_popup_id)
        else:
            return False

        time.sleep(5)
        base_lib.click_on_text_id(settings_locators.battery_saver_option, settings_locators.battery_saver_option_id)
        time.sleep(1)
        return True

    except Exception as e:
        print("Exception occured: ", str(e))
        return False

@keyword
def VERIFY_BUILD_ID():
    try:
        build_id=os.popen(settings_locators.adb_command_build_id).read()
        print(build_id)
        if build_id == settings_locators.device_build_id:
            return True
        else:
            return False

    except Exception as e:
        print("Exception occured: ", str(e))
        return False

@keyword
def ENABLE_ADAPTIVE_BRIGHTNESS():
    try:
        base_lib.swipe_screen()
        time.sleep(2)
        ele = base_lib.element_exists(settings_locators.display_option_text, settings_locators.display_option_id)
        if ele:
            base_lib.click_on_text_id(settings_locators.display_option_text, settings_locators.display_option_id)
            time.sleep(3)
        else:
            base_lib.click_on_id("com.android.settings:id/search_action_bar", "android.view.ViewGroup")
            time.sleep(2)
            os.system("adb shell input text " + "adaptive")
            time.sleep(2)
            base_lib.go_back()
            base_lib.click_on_id(settings_locators.adaptive_option_text, settings_locators.adaptive_option_id)
            time.sleep(3)

        result_ab = base_lib.element_exists(settings_locators.status_off, settings_locators.adaptive_brightness_switch_id)
    
        base_lib.click_on_id("android:id/switch_widget","android.widget.Switch")
        time.sleep(2)
    except Exception as e:
        print("Exception occured: ", str(e))
        return False

@keyword
def DISABLE_ADAPTIVE_BRIGHTNESS():
    try:
        time.sleep(2)
        ele = base_lib.element_exists(settings_locators.display_option_text, settings_locators.display_option_id)
        if ele:
            base_lib.click_on_text_id(settings_locators.display_option_text, settings_locators.display_option_id)
            time.sleep(3)
        else:
            base_lib.click_on_id("com.android.settings:id/search_action_bar", "android.view.ViewGroup")
            time.sleep(2)
            os.system("adb shell input text " + "display")
            time.sleep(2)
            base_lib.go_back()
            base_lib.click_on_text_id(settings_locators.display_option_text, settings_locators.display_option_id)
            time.sleep(3)

        base_lib.click_on_text_id(settings_locators.adaptive_brightness_option_text, settings_locators.adaptive_brightness_option_id)
        time.sleep(2)
        result_ab = base_lib.element_exists(settings_locators.status_on, settings_locators.adaptive_brightness_switch_id)
        if result_ab == True:
            base_lib.click_on_text_id(settings_locators.status_on, settings_locators.adaptive_brightness_switch_id)
        time.sleep(2)
        return True

    except Exception as e:
        print("Exception occured: ", str(e))
        return False

@keyword
def LAUNCH_DROZER():
    try:
        base_lib.launch_app("drozer Agent")
        return True

    except Exception as e:
        print("Exception occured: ",str(e))
        return False







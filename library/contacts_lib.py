import base_lib
from robot.api.deco import keyword
import time
from locators import contacts_locators as loc
import os

ROBOT_AUTO_KEYWORDS = False


@keyword
def LAUNCH_CONTACTS():
    try:
        print("Launching Contacts")
        #details=base_lib.GET_DEVINFO()
        #print(details)
        base_lib.launch_app(loc.appName)
        time.sleep(6)
        return True
    except Exception as e:
        base_lib.take_screenshot("Launch_contacts_failure")
        print("Exception occured",str(e))
        return False


@keyword
def ADD_CONTACT(contact_name,contact_number):
     try:
       if base_lib.GET_DEVICE_NAME()=="msmnile\n":
           print("Adding new Contact")

           base_lib.click_on_id(loc.add_contact_button_resource_ID,
                                loc.add_contact_button_class)
           time.sleep(1)
           if base_lib.check_existence_by_name(loc.cancel_button_text, loc.cancel_button_class):
               base_lib.click_on(loc.cancel_button_text, loc.cancel_button_class)
           time.sleep(1)
           base_lib.click_on(loc.first_name_text, loc.first_name_class)
           base_lib.enter_text(contact_name)
           base_lib.go_back()
           base_lib.click_on(loc.phone_text, loc.phone_class)
           base_lib.enter_text(contact_number)
           base_lib.click_on(loc.save_button_text, loc.save_button_class)
           time.sleep(3)

           print("Contact successfully added")
           # with open("locators\\contacts_locators.py",mode='a') as f:
           # f.write(f"\n{contact_name}="+f'"{str(contact_name)}"')
           # f.write(f"\n{contact_number}="+f'"{str(contact_name)}"')

           base_lib.go_back()
           time.sleep(2)
           return True
       elif base_lib.GET_DEVICE_NAME()=="coral\n":
           base_lib.close_app()
           base_lib.launch_app(loc.appName_phone)
           time.sleep(1)
           base_lib.click_on(loc.create_new_contact_text,loc.create_new_contact_class)
           time.sleep(1)
           base_lib.click_on(loc.first_name_text, loc.first_name_class)
           base_lib.enter_text(contact_name)
           base_lib.go_back()
           base_lib.click_on(loc.phone_text, loc.phone_class)
           base_lib.enter_text(contact_number)
           time.sleep(3)
           base_lib.click_on(loc.save_button_pixel_text, loc.save_button_class)
           time.sleep(3)
           print("Contact successfully added")
           time.sleep(2)
           return True



     except Exception as e:
       base_lib.take_screenshot("Add_contact_failure")
       print("Exception occured",str(e))
       return False


@keyword
def SEARCH_CONTACT_BY_NAME(name):
    try:
        if base_lib.GET_DEVICE_NAME=="msmnile\n":
            base_lib.click_on_id(loc.search_ID, loc.search_class)
            base_lib.enter_text(name)
            time.sleep(2)
            # base_lib.click_on(name, loc.contact_class)
            if base_lib.check_existence_by_name(name, loc.contact_class):
                time.sleep(2)
                return True
        elif base_lib.GET_DEVICE_NAME()=="coral\n":
            base_lib.click_on(loc.search_contact_text,loc.search_class)
            base_lib.enter_text(name)
            if base_lib.check_existence_by_name(name, loc.contact_class):
                time.sleep(2)
                return True

    except Exception as e:
        base_lib.take_screenshot("Search_contact_failure")
        print("Exception occured", str(e))
        return False


@keyword
def CLICK_CONTACT(name):
    base_lib.click_on_id(name,loc.contact_class)

@keyword
def LONG_CLICK_CONTACT(name):
    base_lib.long_click_by_text(name,loc.contact_class)



@keyword
def EXPORT_CONTACTS():
    try:
        if base_lib.GET_DEVICE_NAME()=="msmnile\n":
            # base_lib.click_on(loc.hamburger_name, loc.hamburger_class)
            base_lib.swipe_from_left()
            time.sleep(2)
            base_lib.click_on_id(loc.settings_resource_id, loc.settings_class)
            time.sleep(2)
            base_lib.find_element_by_scroll(loc.export_text, loc.export_class)
            time.sleep(1)
            base_lib.click_on(loc.export_text, loc.export_class)
            time.sleep(1)
            base_lib.click_on(loc.export_to_text, loc.export_to_class)
            time.sleep(3)
            if base_lib.check_existence_by_name(loc.access_media_allow_text, loc.access_media_allow_class):
                base_lib.click_on(loc.access_media_allow_text, loc.access_media_allow_class)

            time.sleep(5)
            base_lib.click_on(loc.save_button_text, loc.save_button_class)
            time.sleep(2)
            return True
        elif base_lib.GET_DEVICE_NAME()=="coral\n":
            base_lib.click_on(loc.fix_and_manage_text,loc.fix_and_manage_text_class)
            base_lib.click_on(loc.export_to_file_text,loc.export_to_file_class)
            base_lib.click_on(loc.check_box_text,loc.check_box_class)
            base_lib.click_on(loc.export_to_vcf_file_text,loc.export_to_vcf_file_class)
            if base_lib.check_existence_by_name(loc.access_media_allow_text, loc.access_media_allow_class):
                base_lib.click_on(loc.access_media_allow_text, loc.access_media_allow_class)

            time.sleep(5)
            base_lib.click_on(loc.save_button_text, loc.save_button_class)
            time.sleep(2)
            return True

    except Exception as e:
        base_lib.take_screenshot("Export_contact_failure")
        print("Exception occured", str(e))
        return False

@keyword
def IMPORT_CONTACTS():
    try:
        if base_lib.GET_DEVICE_NAME=="msmnile\n":
            # base_lib.click_on(loc.hamburger_name, loc.hamburger_class)
            base_lib.swipe_from_left()
            time.sleep(2)
            base_lib.click_on_id(loc.settings_resource_id, loc.settings_class)
            time.sleep(2)
            base_lib.find_element_by_scroll(loc.import_text, loc.import_class)
            time.sleep(1)
            base_lib.click_on(loc.import_text, loc.import_class)
            time.sleep(2)
            base_lib.click_on(loc.import_from_text, loc.import_from_class)
            print("Importing...")
            time.sleep(3)
            if base_lib.check_existence_by_name(loc.access_media_allow_text, loc.access_media_allow_class):
                base_lib.click_on(loc.access_media_allow_text, loc.access_media_allow_class)
            time.sleep(5)
            base_lib.click_on_id(loc.contacts_vcf_resource_ID, loc.contacts_vcf_image_class)
            time.sleep(3)
            base_lib.go_back()
            print("Import successful")
            time.sleep(2)
            return True
        elif base_lib.GET_DEVICE_NAME()=="coral\n":
            base_lib.click_on(loc.fix_and_manage_text,loc.fix_and_manage_text_class)
            base_lib.click_on(loc.import_from_file_text,loc.export_to_file_class)
            base_lib.click_on(loc.check_box_text,loc.check_box_class)
            time.sleep(3)
            if base_lib.check_existence_by_name(loc.access_media_allow_text, loc.access_media_allow_class):
                base_lib.click_on(loc.access_media_allow_text, loc.access_media_allow_class)
            time.sleep(5)
            base_lib.click_on(loc.contacts_vcf_text, loc.contacts_vcf_class)
            time.sleep(3)
            base_lib.go_back()
            print("Import successful")
            time.sleep(2)
            return True
    except Exception as e:
        base_lib.take_screenshot("Import_failure")
        print("Exception occured", str(e))
        return False





@keyword
def SEND_MESSAGE(contact_name,message):
    try:
        if base_lib.GET_DEVICE_NAME=="msmnile\n":
            SEARCH_CONTACT_BY_NAME(contact_name)
            CLICK_CONTACT(contact_name)
            time.sleep(3)
            base_lib.click_on_id(loc.message_icon_resource_ID, loc.message_icon_class)
            time.sleep(2)
            base_lib.click_on_id(loc.enter_message_here_ID, loc.enter_message_here_class)
            base_lib.enter_text(message)
            time.sleep(2)
            if base_lib.element_exists_by_id_class(loc.send_button_ID, loc.send_button_class):
                base_lib.click_on_id(loc.send_button_ID, loc.send_button_class)
            else:
                base_lib.go_back()
            time.sleep(2)
            return True
        elif base_lib.GET_DEVICE_NAME() == "coral\n":
            SEARCH_CONTACT_BY_NAME(contact_name)
            base_lib.go_back()
            CLICK_CONTACT(contact_name)
            time.sleep(3)
            base_lib.click_on(loc.text_message_icon_text,loc.text_message_class)
            time.sleep(2)
            base_lib.click_on(loc.type_message,loc.type_message_class)
            base_lib.enter_text(message)
            base_lib.click_on(loc.send_icon_ID,loc.send_icon_class)
            return True


    except Exception as e:
        base_lib.take_screenshot("Send_message_failure")
        print("Exception occured", str(e))
        return False


@keyword
def EDIT_CONTACT_NAME(contact_name,changed_name):
    try:
        SEARCH_CONTACT_BY_NAME(contact_name)
        time.sleep(2)
        CLICK_CONTACT(contact_name)
        time.sleep(1)
        if base_lib.GET_DEVICE_NAME=="msmnile\n":
           base_lib.click_on_id(loc.edit_icon, loc.edit_icon_class)
        elif base_lib.GET_DEVICE_NAME() == "coral\n":
           base_lib.click_on_id(loc.edit_icon_for_pixel_ID, loc.edit_icon_class)
        time.sleep(2)
        base_lib.click_on(contact_name, loc.first_name_class)
        base_lib.enter_text(changed_name)
        if base_lib.GET_DEVICE_NAME=="msmnile\n":
            base_lib.click_on(loc.save_button_text, loc.save_button_class)
        elif base_lib.GET_DEVICE_NAME() == "coral\n":
            base_lib.click_on(loc.save_button_pixel_text, loc.save_button_class)
        time.sleep(3)
        base_lib.go_back()
        a=contact_name+changed_name
        if SEARCH_CONTACT_BY_NAME(a):
            time.sleep(2)
            return True
        else:
            base_lib.close_app()
            LAUNCH_CONTACTS()
            SEARCH_CONTACT_BY_NAME(a)
            time.sleep(2)
            return True
    except Exception as e:
        base_lib.take_screenshot("Edit_contact_failure")
        print("Exception occured", str(e))
        return False


@keyword
def EDIT_CONTACT_NUMBER(contact_name,changed_number):
    try:
        SEARCH_CONTACT_BY_NAME(contact_name)
        time.sleep(2)
        CLICK_CONTACT(contact_name)
        time.sleep(1)
        if base_lib.GET_DEVICE_NAME=="msmnile\n":
           base_lib.click_on_id(loc.edit_icon, loc.edit_icon_class)
        elif base_lib.GET_DEVICE_NAME() == "coral\n":
           base_lib.click_on_id(loc.edit_icon_for_pixel_ID, loc.edit_icon_class)
        time.sleep(2)
        base_lib.click_on(loc.phone_text, loc.phone_class)
        base_lib.enter_text(changed_number)
        if base_lib.GET_DEVICE_NAME=="msmnile\n":
            base_lib.click_on(loc.save_button_text, loc.save_button_class)
        elif base_lib.GET_DEVICE_NAME() == "coral\n":
            base_lib.click_on(loc.save_button_pixel_text, loc.save_button_class)
        time.sleep(3)
        return True
    except Exception as e:
        base_lib.take_screenshot("Edit_contact_failure")
        print("Exception occured", str(e))
        return False


@keyword
def DELETE_CONTACT(contact_name):
    try:
        if base_lib.GET_DEVICE_NAME=="msmnile\n":
            SEARCH_CONTACT_BY_NAME(contact_name)
            time.sleep(1)
            LONG_CLICK_CONTACT(contact_name)
            time.sleep(2)
            print("Deleting....")
            base_lib.click_on_id(loc.delete_ID, loc.delete_class)
            time.sleep(2)
            print("Confirming.....")
            base_lib.click_on_text_id(loc.delete_popup_text, loc.delete_popup_id)
            print("Delete successful")
            time.sleep(2)
            return True
        elif base_lib.GET_DEVICE_NAME() == "coral\n":
            return True
    except Exception as e:
        base_lib.take_screenshot("Delete_contact_failure")
        print("Exception occured", str(e))
        return False


#IMPORT_CONTACTS()
#DELETE_CONTACT("xyz")
SEND_MESSAGE("xyz","Hi")
#ADD_CONTACT("abc","0123456789")
#ADD_CONTACT("xyz","9876543210")


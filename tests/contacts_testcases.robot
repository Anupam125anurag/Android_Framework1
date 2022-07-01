*** Settings ***
Documentation    Sanity test
Suite Setup    Initialize Metadata

Library     ../library/base_lib.py
Library     ../library/contacts_lib.py


Test Setup   START_TEST
Test Teardown  END_TEST

*** Keyword ***
Initialize Metadata
        ${devicename}       GET_DEVICE_NAME
        Set suite metadata    Device Name    ${devicename}
        ${devicemodel}       GET_DEVICE_MODEL
        Set suite metadata    Device Model    ${devicemodel}
        ${Android_ver}       GET_ANDROID_VERSION
        Set suite metadata    OS Version    ${Android_ver}
        ${build_id}       GET_BUILD_ID
        Set suite metadata    Build ID    ${build_id}


*** Variables ***
${contact1_name}    xyz
${contact1_number}   9876543210
${contact2_name}    abc
${contact2_number}   0123456789
${changed_name}      acb
${changed_number}    456
${message}          Hi,Good_Day!

*** Test Cases ***
Test_001 - CREATE NEW CONTACT
    [tags]    Sanity
    ${result}     LAUNCH_CONTACTS
    ${result}     ADD_CONTACT     ${contact1_name}   ${contact1_number}
    ${result}     ADD_CONTACT     ${contact2_name}   ${contact2_number}
    run keyword if  ${result}==False    Fail    ADD_CONTACT_FAILED    ELSE    LOG    PASS


Test_002 - SEARCH CONTACT
    [tags]    Sanity
    ${result}     LAUNCH_CONTACTS
    ${result}      SEARCH_CONTACT_BY_NAME   ${contact1_name}
    run keyword if  ${result}==False    Fail    SEARCH_CONTACT_FAILED    ELSE    LOG    PASS


Test_003 - EDIT CONTACT NAME
    [tags]    Sanity
    ${result}     LAUNCH_CONTACTS
    ${result}      EDIT_CONTACT_NAME    ${contact2_name}  ${changed_name}
    run keyword if  ${result}==False    Fail    EDIT_CONTACT_FAILED    ELSE    LOG    PASS

Test_004 - EDIT CONTACT NUMBER
    [tags]    Sanity
    ${result}     LAUNCH_CONTACTS
    ${result}      EDIT_CONTACT_NUMBER    ${contact1_name}   ${changed_number}
    run keyword if  ${result}==False    Fail    EDIT_CONTACT_FAILED    ELSE    LOG    PASS


Test_005 - EXPORT CONTACT
    [tags]    Sanity
    ${result}     LAUNCH_CONTACTS
    ${result}      EXPORT_CONTACTS
    run keyword if  ${result}==False    Fail    EXPORT_CONTACT_FAILED    ELSE    LOG    PASS


Test_006 - IMPORT CONTACTS
    [tags]    Sanity
    ${result}     LAUNCH_CONTACTS
    ${result}     IMPORT_CONTACTS
    run keyword if  ${result}==False    Fail    IMPORT_CONTACT_FAILED    ELSE    LOG    PASS


Test_007 - SEND TEXT MESSAGE
    [tags]    Sanity
    ${result}     LAUNCH_CONTACTS
    ${result}     SEND_MESSAGE   ${contact1_name}    ${message}
    run keyword if  ${result}==False    Fail    MESSAGE_CONTACT_FAILED    ELSE    LOG    PASS

Test_008 - DELETE CONTACT
    [tags]    Sanity
    ${result}     LAUNCH_CONTACTS
    ${result}     DELETE_CONTACT   ${contact1_name}
    run keyword if  ${result}==False    Fail    DELETE_CONTACT_FAILED    ELSE    LOG    PASS

*** Settings ***
#Suite Setup    Initialize Metadata
Library     ../library/base_lib.py
Library     ../library/multimedia_lib.py

Test Setup   START_TEST
Test Teardown  END_TEST

*** Keyword ***


*** Test Cases ***
Test 001 - Play an audio music
    [tags]    Sanity
    #launch music player
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_MUSIC
    ${result}     PLAY_MUSIC
    run keyword if  ${result}==False    Fail   Playing_Music_Failed    ELSE    LOG    PASS


Test 002 - Pause an audio music
    [tags]    Sanity
    #launch music player
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_MUSIC
    ${result}     PLAY_MUSIC
    ${result}     PAUSE_MUSIC
    run keyword if  ${result}==False    Fail   Pausing_Music_Failed    ELSE    LOG    PASS

Test 003 - Next audio
    [tags]    Sanity
    #launch music player
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_MUSIC
    ${result}     PLAY_MUSIC
    ${result}     NEXT_MUSIC
    run keyword if  ${result}==False    Fail   Playing_Next_Music_Failed    ELSE    LOG    PASS

Test 004 - Previous audio
    [tags]    Sanity
    #launch music player
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_MUSIC
    ${result}     PLAY_MUSIC
    ${result}     PREVIOUS_MUSIC
    run keyword if  ${result}==False    Fail   Playing_Previous_Music_Failed    ELSE    LOG    PASS

Test 005 - Play a video
    [tags]    Sanity
    #launch video player
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_VIDEO
    ${result}     PLAY_VIDEO
    run keyword if  ${result}==False    Fail   Playing_Video_Failed    ELSE    LOG    PASS


Test 006 - Pause a video
    [tags]    Sanity
    #launch video player
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_VIDEO
    ${result}     PLAY_VIDEO
    ${result}     PAUSE_VIDEO
    run keyword if  ${result}==False    Fail   Pausing_Video_Failed    ELSE    LOG    PASS

Test 007 - Next  video
    [tags]    Sanity
    #launch video player
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_VIDEO
    ${result}     PLAY_VIDEO
    ${result}     NEXT_VIDEO
    run keyword if  ${result}==False    Fail   Playing_Next_Video_Failed    ELSE    LOG    PASS

Test 008 - Previous video
    [tags]    Sanity
    #launch video player
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_VIDEO
    ${result}     PLAY_VIDEO
    ${result}     PREVIOUS_VIDEO
    run keyword if  ${result}==False    Fail   Playing_Previous_Video_Failed    ELSE    LOG    PASS

Test 009 - Play an audio and then open browser
    [tags] Sanity
    #launch audio player
    ${result} LAUNCH_MUSIC
    ${result} GOTO_HOME
    ${result} LAUNCH_BROWSER
    run keyword if  ${result}==False    Fail   Launch_Browser_Failed    ELSE    LOG    PASS





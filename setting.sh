#!/usr/bin/env bash

DIR_PATH=`dirname $0`
URL_PATH=$DIR_PATH"/src/sender/url.py"
SETTINGS_PATH=$DIR_PATH"/src/config/settings.py"

echo -e "\033[0;34mMade by \033[1;36mkuj0210, KeonHeeLee, seok8418 \033[1;34m"
echo -e "\033[0;34m- Github : \033[1;36mhttps://github.com/IoT-Pet-Home-System/petHomeSystem"
echo -e "\033[0;34m- E-mail : \033[1;36mon_11@naver.com\033[0m"
echo " "

echo -e "\033[1;36m1. Main-Server Setting\033[0m"

echo -e "- Write chatting-bot server\'s domain: \c"
read url

payload="SERVER_URL = \""$url"\""
echo $payload

if [ -e `ls $URL_PATH` ]; then
    rm -rf "$URL_PATH"
    touch "$URL_PATH"
    echo $payload >> "$URL_PATH"
else
    touch "$URL_PATH"
    echo $payload >> "$URL_PATH"
fi

echo -e "\033[1;36m2. Pet-home\'s Basic Settings\033[0m"

echo -e "- Delay sending request to main-server(sec): \c"
read delay

echo -e "- Delay sending feed-alarm to main-server(min): \c"
read feed

echo -e "- Delay sending door-alarm to main-server(min): \c"
read door

payload="WAIT_DELAY =\"$delay\"\nFEED_ALARM = \"$feed\"\nDOOR_ALARM = \"$door\""

if [ -e `ls $SETTINGS_PATH` ]; then
    rm -rf "$SETTINGS_PATH"
    touch "$SETTINGS_PATH"
    echo $payload >> "$SETTINGS_PATH"
else
    touch "$SETTINGS_PATH"
    echo $payload >> "$SETTINGS_PATH"
fi

echo -e "\033[0;34mIoT-Pet-Home-System's Pet Home Setting is complete!!\033[0m"

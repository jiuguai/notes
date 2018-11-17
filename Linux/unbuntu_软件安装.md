1. 安装chrome
    1. sudo wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/

    2. wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -

    3. sudo apt-get update

    4. sudo apt-get install google-chrome-stable

    5. /usr/bin/google-chrome-stable
        1. sudo apt install --reinstall libnss3 (如果提示错误可尝试重新安装libnss3)

    6. sudo apt install gnome-keyring
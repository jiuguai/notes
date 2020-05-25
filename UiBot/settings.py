import platform
import os

DESKTOP_DIR = os.path.join(os.environ['USERPROFILE'],"desktop")

if platform.node() == "zero_PC":
    MYSQL_CON_DIC = {
        "user":"root",
        "password":"jiuguai",
        "host":"127.0.0.1",
        "port":3306,
        "charset":'utf8mb4',
        "database":"dunshen"
    
    }

else:
    MYSQL_CON_DIC = {
        "user":"uibot",
        "password":"OHdSK3Ab0iuvgDrn",
        "host":"192.168.75.130",
        "port":3306,
        "charset":'utf8mb4',
        "database":"uibot_entwebconsole"
    
    }
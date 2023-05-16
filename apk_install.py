
from adb_shell.auth.keygen import keygen
from ppadb.client import Client as AdbClient
import subprocess
import os, glob


class Adb:

    def __init__(self):
        self.adb = os.getcwd()+'\platform-tools\\adb.exe'
        self.apk_files = glob.glob(f'{os.getcwd()}\\apk\\*.apk')
        self.app_package_id = "com.facebook.katana"
        subprocess.call(f"{self.adb} start-server", shell=True)
        self.client = AdbClient(host="127.0.0.1", port=5037)

    def installAllApp(self):
        devices = self.client.devices()
        if (len(devices) > 0):
            i = 0
            for device in devices:
                if device.is_installed(self.app_package_id) == True:
                    subprocess.run(f"{self.adb} -s {device.serial} uninstall {self.app_package_id}", shell = True)
                subprocess.run(f"{self.adb} -s {device.serial} install -r {self.apk_files[i]}", shell = True)
                i += 1
        else:
            print("Không có device nào")
            return 0

adb = Adb().installAllApp()
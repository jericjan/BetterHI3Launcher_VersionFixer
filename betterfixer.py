#Python3 version of hugo24's snippet
import winreg
import json

REG_PATH = r"SOFTWARE\Bp\Better HI3 Launcher"

def set_reg(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_BINARY, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def get_reg(name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

#Example MouseSensitivity
#Read value
sea_reg = get_reg('VersionInfoSEA')
glob_reg = get_reg('VersionInfoGlobal')
if sea_reg != None:
    reg_json = json.loads(get_reg('VersionInfoSEA').decode('utf-8'))
    print(reg_json['game_info']['version'])
    if reg_json['game_info']['version'] == '4.7.0_361c5ee9333':
        print("All good!")
    else:
        print("Better launcher has wrong version!")
        print("Fixing...")
        reg_json['game_info']['version'] = '4.7.0_361c5ee9333'
        fixed_json = json.dumps(reg_json,separators=(',', ':')).encode('utf-8')
        print(fixed_json)
        set_reg('VersionInfoSEA',fixed_json)
if glob_reg != None:
    reg_json = json.loads(get_reg('VersionInfoGlobal').decode('utf-8'))
    print(reg_json['game_info']['version'])
    if reg_json['game_info']['version'] == '4.7.0_361c5ee9333':
        print("All good!")
    else:
        print("Better launcher has wrong version!")
        print("Fixing...")
        reg_json['game_info']['version'] = '4.7.0_361c5ee9333'
        fixed_json = json.dumps(reg_json,separators=(',', ':')).encode('utf-8')
        print(fixed_json)
        set_reg('VersionInfoGlobal',fixed_json)            
input()

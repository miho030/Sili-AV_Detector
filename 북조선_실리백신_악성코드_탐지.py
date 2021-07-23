#-*- coding: utf-8 -*-
"""
*English
+===========================================================+
+ Caution!                                                  +
+                                                           +
+                                                           +
+ This program is developed for research purposes.          +
+ This dedicated vaccine was made only to detect and        +
+ treat the malware;'실리왁찐' that leaked from North Korea.+
+                                                           + 
+ This Script is based on GNU GPL version 3.                +
+ Anyone can modify this program to own system environment. +
+                                                           +
+ Copyright(c) by Misty                                     +
+                                                           +
+ KISA Kucis Seahawk..                                      +
+===========================================================+

*korean
+===========================================================+
+ 주의!                                                     +
+                                                           +
+                                                           +
+ 이 프로그램은 연구 목적으로 제작/개발 되었습니다.         +
+ 이 전용 백신은 오로지 북한에서 유출된 북한 백신인         +
+ '실리왁찐'의 악성코드 버전만을 탐지하고 삭제합니다.       +
+                                                           + 
+ 이 프로그램은 GNU GPL 버전 3를 기반으로 제작되었습니다.   +
+ 누구나 자신의 시스템에 맞추어                             +
+ 코드를 수정하여 사용할 수 있습니다.                       +
+                                                           +
+ Copyright(c) by Misty                                     +
+                                                           +
+ KISA Kucis Seahawk..                                      +
+===========================================================+
"""

# major lib import.
import os, sys
import hashlib


# define/make fucntion about 실리왁찐's malware md5 hash.
def FoxDB():
    SV_Info_db = {'Unconfirmed 10525.crdownload->F0x-RAR_extract-VirusTotalUploadN' : ['26ee6f7c33a40eb215b27340313c54cf', 855477],
                  'Sili Anti Virus Scanner.exe->F0x-Trojan/Win32exe' : ['978ba6be4df6ba3ce8c88682e50f7e19', 2344960],
                  'mbmob.exe->F0x-Trojan/Win32exe-NetAssemble;' : ['6d40880a890cc92515855387f6e80bba', 263168]
                  }
    return SV_Info_db


# make DB manufacture engine fuction.
def Fox_mkdb(Fox_hashval, SV_Info_DB):
    for key, value in SV_Info_db.items():
        if value[0]==Fox_hashval:
            return True, key
        return False, ''


# Detect & serach engine.
def FoxMain(Fox_file):
    SV_Info_db = Fox_mkdb()
    Fox_Sdb = map(lambda value: value[1], SV_Info_DB.value())

    Fox_open_file = open(Fox_file, 'rb')
    Fox_file_size = os.path.getsize(file)
    if Fox_file_size not in Fox_sdb:
        print(file, ': [-]', 'Not malware')
        return

    Fox_file_buf = Fox_open_file.read()
    Fox_open_file.close

    Fox_hash = hashlib.md5()
    f.update(file_buf)
    Fox_hashval = Fox_hash.hexdigest

    Fox_Detect, name = Fox_mkdb(Fox_hashval, SV_Info_db)
    if Fox_Detect == True:
        print(file, ': [!]', 'Malware detected!(', name, ')')
        os.remove(file)
    else:
        print(file, ': [-]', 'Not malware')


if __name__ == '__main__':
    if len(sys.argv)==2:
        Fox_file = sys.argv[1]
        
    else:
        
        Fox_file = raw_input('[+]', 'Ienter your file location : ')
    FoxMain(Fox_file)
















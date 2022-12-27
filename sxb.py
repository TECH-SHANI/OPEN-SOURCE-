import platform
bit=platform.architecture()[0]
if bit =='64bit':
    import Lite
    Lite.main_apv()
else:
    print('Sorry device or system not support this tools')
    exit()

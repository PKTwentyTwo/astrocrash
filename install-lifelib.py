import os
import platform
operatingsystem = platform.uname()[0]
release = platform.uname()[2]
print('OS: '+operatingsystem)
print('Release: '+release)
if operatingsystem == 'Windows':
    print('Installing lifelib with pip...')
    os.system('pip install python-lifelib')
    print('Installing Cygwin...')
    import lifelib
    lifelib.install_cygwin()
elif operatingsystem == 'Linux':
    if release.count('WSL') > 0:

        print('Installing lifelib using git...')
        os.system('git clone https://gitlab.com/apgoucher/lifelib')
    else:
        print('Installing lifelib with pip...')
        os.system('pip install python-lifelib')

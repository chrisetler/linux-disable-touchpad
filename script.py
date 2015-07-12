#!/usr/bin/env python
import subprocess
DEVICE_NUM = '11'
#get the current value of the touchpad state (val = {0->off, 1->on})
touchpadVal = subprocess.Popen(['xinput','list-props',DEVICE_NUM],stdout=subprocess.PIPE)
val = subprocess.check_output(['grep','Enabled'], stdin=touchpadVal.stdout)
touchpadVal.wait()
val = val[len(val) -2]

if(val == '0' ):
    print "Turning On"
    subprocess.call(['xinput','set-prop',DEVICE_NUM,'Device Enabled','1'])
else:
    print "Turning Off"
    subprocess.call(['xinput','set-prop',DEVICE_NUM,'Device Enabled','0'])

# -*- encoding=utf8 -*-
from airtest.core.api import *

#连接设备，具体用法&参考：https://mp.weixin.qq.com/s/znYi-eCifeMXfce9GDpW-w
auto_setup(__file__,devices=['android://127.0.0.1:5037/emulator-5554'])

start_app('com.dotamax.app')


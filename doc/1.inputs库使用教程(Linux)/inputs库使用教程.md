# inputs库使用教程



[toc]

作者: 阿凯爱玩机器人 | QQ:  244561792 | 微信: xingshunkai

[1Z实验室](http://1zlab.com/) | [B站](https://space.bilibili.com/40344504) | [知乎](https://www.zhihu.com/people/mushroom-x)



## 软硬件版本

![](image/gamepad.png)

* **操作系统**: `Ubuntu 20.04`

  > 注: Windows更简单一些，代码都是通用的。 

* **手柄型号**：`谷粒金刚2 Pro`

  手柄与PC通过TypeC数据线链接, 功能模式切换到Windows D

  > 注:  D代表直连。GamePad库不局限于任何手柄机型。

  

## 查看USB设备信息

在Linux下执行命令行, 查看USB设备信息

```bash
sudo cat /sys/kernel/debug/usb/devices 
```

*输出日志*

> 注: 日志只呈现了手柄相关的信息

```
...
T:  Bus=01 Lev=01 Prnt=01 Port=00 Cnt=01 Dev#= 23 Spd=12   MxCh= 0
D:  Ver= 2.00 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
P:  Vendor=0079 ProdID=0122 Rev= 1.09
S:  Manufacturer=ZhiXu
S:  Product=GuliKit Controller D
C:* #Ifs= 1 Cfg#= 1 Atr=80 MxPwr=400mA
I:* If#= 0 Alt= 0 #EPs= 2 Cls=03(HID  ) Sub=00 Prot=00 Driver=usbhid
E:  Ad=81(I) Atr=03(Int.) MxPS=  64 Ivl=5ms
E:  Ad=01(O) Atr=03(Int.) MxPS=  64 Ivl=10ms
...
```

于是我们可以知道手柄的`Vendor` 与`ProdID` 的编号.

```
Vendor=0079 ProdID=0122
```

注:ID号为16进制，所以应该写为

```
Vendor=0x0079 ProdID=0x0122
```

## 开发环境配置

### 用户组配置

对于Linux操作系统，需要先将当前用户添加到`inputs group`组里面. 

查看当前用户组

```bash
$ groups
kyle adm dialout cdrom sudo dip plugdev lpadmin lxd sambashare docker
```

将当前用户`kyle`添加到用户组`dialout`里面

```bash
sudo usermod -a -G dialout kyle
```

添加完成之后，系统需要重启。

### 安装inputs

`inputs` 是一个输入设备读取的库。 相比较其他的库， inputs的依赖最小，最简洁。

[PyPi](https://pypi.org/project/inputs/)  | [使用文档](https://inputs.readthedocs.io/en/latest/)
安装`inputs`

```bash
sudo pip3 install inputs
```

## `inputs`使用实例

### 获取设备列表

源码

```python
# 获取所有的USB设备
from inputs import devices
# 遍历所有设备名称，并打印出来
for device in devices:
    print(device)
```

日志

```
SINO WEALTH Gaming KB
USB OPTICAL MOUSE
SINO WEALTH Gaming KB  Mouse
ZhiXu GuliKit Controller D
SINO WEALTH Gaming KB  System Control
```

其中`ZhiXu GuliKit Controller D`是谷粒金刚2 Pro的设备名称.

### 获取游戏手柄事件并打印

```python
from inputs import get_gamepad
# 打印
while True:
    # 获取游戏手柄事件
    events = get_gamepad()
    # 逐一打印事件信息
    for event in events:
        # 数据类型 |字符串|字符串|整数|
        print(f"事件类型: {event.ev_type} | 事件代码: {event.code} | 事件状态: {event.state}")  # 字符串
    print("-"*50)
```

操作游戏手柄，查看事件输出。 

> 注: 每款手柄的功能按键事件可能有出入， 以实际为准。

## 联系作者

![](../../阿凯爱玩机器人.jpg)

# GamePad库Python使用示例

[toc]

作者: 阿凯爱玩机器人 | QQ:  244561792 | 微信: xingshunkai

[1Z实验室](http://1zlab.com/) | [B站](https://space.bilibili.com/40344504) | [知乎](https://www.zhihu.com/people/mushroom-x)



## 导入依赖


```python
import logging
# 自定义库
# 用户需要根据自己手柄的情况, 编写gamepad的子类
# 在init_sensor函数里面定义都有哪些传感器组件，以及编号
# 详情参见`gamepad.py`与`gulikit.py`
from gulikit import Gulikit
```

## 创建手柄


```python
# 创建手柄
# 可以设置不同的日志模式
pad = Gulikit(logging_level=logging.INFO)
# pad = Gulikit(logging_level=logging.WARN)
```

    [LEFT_JOYSTICK_X][INFO]: 数值更新: 128
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 128
    [RIGHT_JOYSTICK_X][INFO]: 数值更新: 128
    [RIGHT_JOYSTICK_Y][INFO]: 数值更新: 128


## 事件绑定

### 普通按键事件绑定


```python
# 绑定回调函数
def a_click():
    print("按键A按下")

def a_release():
    print("按键A释放")
    
def a_change():
    print("按键A数值变动")

pad.btn_a.on_click = a_click
pad.btn_a.on_release = a_release
pad.btn_a.on_change = a_change
```

### 十字按键事件绑定
> 注: 十字按键的四个元素， 都可以当普通按键来使用。


```python
def cross_btn_update():
    position = pad.btn_cross.get_position()
    print(f"十字按键更新, 坐标: {position}")

def cross_btn_release():
    print("十字按键释放")

pad.btn_cross.on_change = cross_btn_update
pad.btn_cross.on_release = cross_btn_release
```

### 遥杆按键事件绑定


```python
def left_joystick_change():
    position = pad.left_joystick.get_position()
    print(f"遥杆位置更新: {position}")

pad.left_joystick.on_change = left_joystick_change
```

## 事件监听线程(非阻塞)


```python
# 手动执行事件监听器
pad.start_event_listener_thread()
```


```python
# 终止游戏手柄事件监听器
# pad.stop_event_listener_thread()
```

    [A][INFO]: 按键按下
    [A][INFO]: 按键释放


    按键A按下
    按键A数值变动
    按键A释放
    按键A数值变动


    [UP][INFO]: 按键按下
    [DOWN][INFO]: 按键释放
    [UP][INFO]: 按键释放
    [DOWN][INFO]: 按键释放


    十字按键更新, 坐标: (0, -1)
    十字按键释放
    十字按键更新, 坐标: (0, 0)


    [RIGHT_JOYSTICK_X][INFO]: 数值更新: 133
    [RIGHT_JOYSTICK_Y][INFO]: 数值更新: 138
    [RIGHT_JOYSTICK_Y][INFO]: 数值更新: 139
    [RIGHT_JOYSTICK_Y][INFO]: 数值更新: 138
    [RIGHT_JOYSTICK_X][INFO]: 数值更新: 132
    [RIGHT_JOYSTICK_Y][INFO]: 数值更新: 136
    [RIGHT_JOYSTICK_X][INFO]: 数值更新: 128
    [RIGHT_JOYSTICK_Y][INFO]: 数值更新: 127
    [LEFT_JOYSTICK_X][INFO]: 数值更新: 124
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 117
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 111
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 104
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 90
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 76
    [LEFT_JOYSTICK_X][INFO]: 数值更新: 123
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 61
    [LEFT_JOYSTICK_X][INFO]: 数值更新: 119
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 41
    [LEFT_JOYSTICK_X][INFO]: 数值更新: 111
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 14
    [LEFT_JOYSTICK_X][INFO]: 数值更新: 100
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 0
    [LEFT_JOYSTICK_X][INFO]: 数值更新: 95
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 2
    [LEFT_JOYSTICK_X][INFO]: 数值更新: 102
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 14
    [LEFT_JOYSTICK_X][INFO]: 数值更新: 119


    遥杆位置更新: (124, 128)
    遥杆位置更新: (124, 117)
    遥杆位置更新: (124, 111)
    遥杆位置更新: (124, 104)
    遥杆位置更新: (124, 90)
    遥杆位置更新: (124, 76)
    遥杆位置更新: (123, 76)
    遥杆位置更新: (123, 61)
    遥杆位置更新: (119, 61)
    遥杆位置更新: (119, 41)
    遥杆位置更新: (111, 41)
    遥杆位置更新: (111, 14)
    遥杆位置更新: (100, 14)
    遥杆位置更新: (100, 0)
    遥杆位置更新: (95, 0)
    遥杆位置更新: (95, 2)
    遥杆位置更新: (102, 2)
    遥杆位置更新: (102, 14)
    遥杆位置更新: (119, 14)


    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 40
    [LEFT_JOYSTICK_X][INFO]: 数值更新: 135
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 78
    [LEFT_JOYSTICK_X][INFO]: 数值更新: 143
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 115
    [LEFT_JOYSTICK_X][INFO]: 数值更新: 128
    [LEFT_JOYSTICK_Y][INFO]: 数值更新: 127


    遥杆位置更新: (119, 40)
    遥杆位置更新: (135, 40)
    遥杆位置更新: (135, 78)
    遥杆位置更新: (143, 78)
    遥杆位置更新: (143, 115)
    遥杆位置更新: (128, 115)
    遥杆位置更新: (128, 127)

## 联系作者

![](../../阿凯爱玩机器人.jpg)

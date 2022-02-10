'''传感器'''

from asyncio.log import logger
import enum
from copy import deepcopy
from inputs import InputEvent
# 自定义库
from utils.logger_interface import LoggerInterface

class SensorEventFlag(enum.Enum):
    '''传感器事件标志位'''
    NONE = 0   # 处理完成/未发生/未设置
    VALUE_CHANGE = 1  # 数值变化

class Sensor(LoggerInterface):
    '''传感器对象'''
    def __init__(self, name, event_type, event_code, \
            on_change=None, logging_level=None):
        # 父类初始化
        super().__init__(name=name, logging_level=logging_level)
        # 传感器名字
        self.name = name
        # 传感器的事件类型与代码
        self.event_type = event_type
        self.event_code = event_code
        # 传感器数值记录
        self._value = 0
        # 标志位
        self._event_flag = SensorEventFlag.NONE
        # 判断回调函数是否有效， 配置回调函数
        # 数值变换的时候，执行的回调函数
        if callable(on_change):
            self.on_change = on_change
        else:
            self.on_change = None
        
    def event_filter(self, event: InputEvent):
        '''事件过滤器
        判断当前事件，是否跟传感器有关系
        '''
        if event.ev_type == self.event_type and event.code == self.event_code:
            return True
        return False
    
    def event_handler(self, event):
        '''事件处理器'''
        if not self.event_filter(event):
            # 该事件与传感器不相关
            return
        # 提取传感器的数值
        self.value = event.state
        # 判断是否要调用数值变化的回调函数
        if self._event_flag == SensorEventFlag.VALUE_CHANGE \
            and self.on_change is not None:
            self.on_change()  
        # 事件Flag清空
        self._event_flag = SensorEventFlag.NONE
    
    @property
    def value(self):
        '''返回传感器的数值'''
        return self._value
        
    @value.setter
    def value(self, new_value):
        '''赋值传感器数值'''
        if new_value != self._value:
            # 设置标志位
            self._event_flag = SensorEventFlag.VALUE_CHANGE
        self._value = new_value
    
    

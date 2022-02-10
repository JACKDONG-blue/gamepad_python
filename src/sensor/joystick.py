'''摇杆'''
import enum
from logging import Logger
from unittest.mock import DEFAULT
from inputs import InputEvent
# 自定义库
from sensor.sensor import Sensor, SensorEventFlag
from utils.logger_interface import LoggerInterface
	
class JoyStickAxis(Sensor):
	'''遥感(单轴)'''
	DEFAULT_VALUE = 128 # 默认值
	def __init__(self, name, event_type, event_code, on_change=None, \
			logging_level=None):
		# 父类初始化
		super().__init__(name, event_type, event_code, on_change, logging_level)
		# 遥杆
		self.joystick = None
		# 设置当前值
		self.value = self.DEFAULT_VALUE
	
	def event_handler(self, event):
		'''事件处理器'''
		if not self.event_filter(event):
			# 该事件与传感器不相关
			return
		# 更新传感器的数值
		self.value = event.state
		# 更新回调函数
		if self.on_change is not None and \
			self._event_flag == SensorEventFlag.VALUE_CHANGE:
			self.on_change()
		# 遥杆更新
		if self.joystick is not None:
			self.joystick.update()
		# 事件Flag清空
		self._event_flag = SensorEventFlag.NONE
		
class JoyStick(LoggerInterface):
	'''游戏手柄'''
	 
	def __init__(self, name, axis_x, axis_y, on_change=None, logging_level=None):
		# 父类初始化
		super().__init__(name, logging_level)
		# 赋值x轴与y轴
		self.axis_x = axis_x
		self.axis_y = axis_y
		# 把当前的joystick也绑定到axis上
		self.axis_x.joystick = self
		self.axis_y.joystick = self
		# 更新会调函数
		self.on_change = on_change if callable(on_change) else None
		# 记录上一次的坐标
		self.last_x = JoyStickAxis.DEFAULT_VALUE
		self.last_y = JoyStickAxis.DEFAULT_VALUE
	
	def get_position(self):
		'''获取位置信息'''
		return (self.axis_x.value, self.axis_y.value)
	
	def update(self):
		'''更新'''
		x, y = self.get_position()
		# 判断数值是否发生了变化
		if self.last_x == x and self.last_y == y:
			return
		# 更新回调函数
		if self.on_change is not None:
			self.on_change()
		# 更新数据
		self.last_x = x
		self.last_y = y
'''
普通按键
'''
from asyncio.log import logger
import enum

from sensor.sensor import SensorEventFlag, Sensor

class ButtonEventFlag(enum.Enum):
	'''传感器事件标志位'''
	NONE = 0   # 处理完成/未发生/未设置
	VALUE_CHANGE = 1  # 数值变化
	BUTTON_CLICK = 2    # 按键按下
	BUTTON_RELEASE = 3  # 按键释放

class ButtonValue(enum.Enum):
	'''按键数值'''
	BUTTON_CLICK = 1    # 按键按下
	BUTTON_RELEASE = 0  # 按键释放
	
class Button(Sensor):
	'''按键'''
	def __init__(self, name, event_type, event_code, \
			on_click=None, on_release=None, on_change=None, \
			logging_level=None):
		# 父类初始化
		super().__init__(name, event_type, event_code, on_change, logging_level)
		# 点击回调函数
		self.on_click = on_click if callable(on_click) else None
		# 释放回调函数
		self.on_release = on_release if callable(on_release) else None
	
	def event_handler(self, event):
		'''事件处理器'''
		if not self.event_filter(event):
			# 该事件与传感器不相关
			return
		# 提取传感器的数值
		self.value = event.state
		# self.logger.info(f"value = {self.value}")
		# 判断是否要调用数值变化的回调函数
		if self.value == ButtonValue.BUTTON_CLICK.value and self.on_click is not None:
			# self.logger.info("button click")
			self.on_click()
		elif self.value == ButtonValue.BUTTON_RELEASE.value and self.on_release is not None:
			# self.logger.info("button release")
			self.on_release()
		# 数值更新事件回调
		if self.on_change is not None:
			# self.logger.info("button value change")
			self.on_change()
		
		# 事件Flag清空
		self._event_flag = ButtonEventFlag.NONE
	
	@property
	def value(self):
		'''返回传感器的数值'''
		return self._value
	
	@value.setter
	def value(self, new_value):
		'''复制传感器数值'''
		if new_value == ButtonValue.BUTTON_CLICK.value:
			# 设置标志位
			self._event_flag = ButtonEventFlag.BUTTON_CLICK
			self.logger.info("按键按下")
		elif new_value == ButtonValue.BUTTON_RELEASE.value:
			# 设置标志位
			self._event_flag = ButtonEventFlag.BUTTON_RELEASE
			self.logger.info("按键释放")
		# 复制
		self._value = new_value
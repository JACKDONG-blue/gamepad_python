'''
十字按键
'''
import enum
from logging import Logger
from inputs import InputEvent
# 自定义库
from sensor.button import Button, ButtonEventFlag
from utils.logger_interface import LoggerInterface

class CrossButtonSingleValue(enum.Enum):
	'''十字按键数值'''
	BUTTON_RELEASE = 0  # 按键释放
	BUTTON_CLICK1 = -1  # 按键按下(1)
	BUTTON_CLICK2 = 1   # 按键按下(2)

class CrossButtonSingle(Button):
	'''十字按键(单个)'''
	def __init__(self, name, event_type, event_code,
			button_click_value=CrossButtonSingleValue.BUTTON_CLICK1, 
			on_click=None, logging_level=None):
		# 按键按下的数值
		self.button_click_value = button_click_value
		# 注: 十字按键只可以绑定按下事件, 不可以配置按键释放与更新事件
		super().__init__(name, event_type, event_code, on_click, None, None, logging_level)
		# 绑定十字按键
		self.cross_button = None
	
	def event_filter(self, event: InputEvent):
		'''事件过滤器
		判断当前事件，是否跟传感器有关系
		'''
		if not (event.ev_type == self.event_type and event.code == self.event_code):
			return False
		# self.logger.info(f"event_state = {event.state} |std: {self.button_click_value.value}")
		if event.state  not in  [self.button_click_value.value, \
			CrossButtonSingleValue.BUTTON_RELEASE.value]:
			# 按键抬起了
			self.value = CrossButtonSingleValue.BUTTON_RELEASE.value
			return False
		return True
		
	def event_handler(self, event):
		'''事件处理器'''
		if not self.event_filter(event):
			# 该事件与传感器不相关
			return
		# self.logger.info("handle event")
		# 更新传感器的数值
		self.value = event.state
		# 十字按键只相应按下事件
		if self.on_click is not None and \
			self._event_flag == ButtonEventFlag.BUTTON_CLICK:
			self.on_click()
		elif self.on_release is not None and  \
			self._event_flag == ButtonEventFlag.BUTTON_RELEASE:
			self.on_release()
		# 数值更新事件
		if self.on_change is not None:
			self.on_change()
		# 如果绑定了十字按键
		if self.cross_button is not None:
			# 巧用cross_button的更新函数
			# self.logger.info("call self.cross_button.update()")
			self.cross_button.update()
		# 事件Flag清空
		self._event_flag = ButtonEventFlag.NONE
	
	@property
	def value(self):
		'''返回传感器的数值'''
		return self._value
	
	@value.setter
	def value(self, new_value):
		'''复制传感器数值'''
		if new_value == self.button_click_value.value:
			# 设置标志位
			self.logger.info(f"按键按下")
			self._event_flag = ButtonEventFlag.BUTTON_CLICK
		elif new_value == CrossButtonSingleValue.BUTTON_RELEASE.value:
			# 设置标志位
			self.logger.info(f"按键释放")
			self._event_flag = ButtonEventFlag.BUTTON_RELEASE
		# 复制
		self._value = new_value
		# self.logger.info("value = {self._value}")
	
class CrossButton(LoggerInterface):
	'''十字按键
	十字按键，用户返回二维坐标
	x轴取值范围 [-1, 0, 1]
	y轴取值范围 [-1, 0, 1]
	'''
	def __init__(self, name,  btn_up, btn_down, btn_left, btn_right, \
			on_release=None, on_change=None, logging_level=None):
		# 父类初始化
		super().__init__(name=name, logging_level=logging_level)
		# 按键赋值
		self.btn_up = btn_up
		self.btn_down = btn_down
		self.btn_left = btn_left
		self.btn_right = btn_right
		# 把当前的CrossButton也绑定到单个按键上
		self.btn_up.cross_button = self
		self.btn_down.cross_button = self
		self.btn_left.cross_button = self
		self.btn_right.cross_button = self
		# 点击回调函数, 任一轴更新
		self.on_change = on_change if callable(on_change) else None
		# 释放回调函数， x轴跟y轴都释放的时候
		self.on_release = on_release if callable(on_release) else None
		# 记录上一次的坐标
		self.last_x = 0
		self.last_y = 0
	
	def get_position(self):
		'''获取2D坐标'''
		x, y = 0, 0
		# 获取y坐标
		if self.btn_down.value != CrossButtonSingleValue.BUTTON_RELEASE.value:
			y = self.btn_down.value
		elif self.btn_up.value != CrossButtonSingleValue.BUTTON_RELEASE.value:
			y = self.btn_up.value
		# 获取x坐标
		if self.btn_left.value != CrossButtonSingleValue.BUTTON_RELEASE.value:
			x = self.btn_left.value
		elif self.btn_right.value != CrossButtonSingleValue.BUTTON_RELEASE.value:
			x = self.btn_right.value
		return (x, y)
	
	def update(self):
		'''更新'''
		x, y = self.get_position()
		# 判断跟之前的数值是否一样
		if self.last_x == x and self.last_y == y:
			return
		# 十字按键释放
		if x == 0 and y == 0 and self.on_release is not None:
			# 默认会传入当前坐标
			self.on_release()
		# 十字按键状态更新
		if self.on_change is not None:
			self.on_change()
		# 更新数据
		self.last_x = x
		self.last_y = y
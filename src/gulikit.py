from gamepad import GamePad
from sensor.button import Button
from sensor.cross_button import CrossButtonSingle, \
	CrossButtonSingleValue, CrossButton

class Gulikit(GamePad):
	'''谷粒金刚游戏手柄
	测试机型: 谷粒金刚2Pro
	'''
	def init_sensor(self):
		'''传感器初始化'''
		# GamePad 构成元素
		# 右侧功能按键
		self.btn_a = Button("A", "Key", "BTN_THUMB")
		self.btn_b = Button("B", "Key", "BTN_TRIGGER")
		self.btn_x = Button("X", "Key", "BTN_TOP")
		self.btn_y = Button("Y", "Key", "BTN_THUMB2")
		# 右侧顶部按键
		self.btn_r1 = Button("R1", "Key", "BTN_PINKIE")
		self.btn_r2 = Button("R2", "Key", "BTN_BASE2")
		# 左侧顶部按键
		self.btn_l1 = Button("L1", "Key", "BTN_TOP2")
		self.btn_l2 = Button("L2", "Key", "BTN_BASE")
		# 左侧十字按键
		self.btn_up = CrossButtonSingle("UP", "Absolute", "ABS_HAT0Y", \
			button_click_value=CrossButtonSingleValue.BUTTON_CLICK1)
		self.btn_down = CrossButtonSingle("DOWN", "Absolute", "ABS_HAT0Y", \
			button_click_value=CrossButtonSingleValue.BUTTON_CLICK2)
		self.btn_left = CrossButtonSingle("LEFT", "Absolute", "ABS_HAT0X", \
			button_click_value=CrossButtonSingleValue.BUTTON_CLICK1)
		self.btn_right = CrossButtonSingle("RIGHT", "Absolute", "ABS_HAT0X",
			button_click_value=CrossButtonSingleValue.BUTTON_CLICK2)
		self.btn_cross = CrossButton("CROSS_BUTTON", self.btn_up, self.btn_down,\
			self.btn_left, self.btn_right)
		
		
		
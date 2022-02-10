from gamepad import GamePad
from sensor.button import Button
from sensor.cross_button import CrossButtonSingle, \
	CrossButtonSingleValue, CrossButton
from sensor.joystick import JoyStickAxis, JoyStick

class Gulikit(GamePad):
	'''谷粒金刚游戏手柄
	测试机型: 谷粒金刚2Pro
	'''
	
	def init_sensor(self):
		'''传感器初始化'''
		# GamePad 构成元素
		# 右侧功能按键
		self.btn_a = Button("A", "Key", "BTN_THUMB", \
			logging_level=self.logging_level)
		self.btn_b = Button("B", "Key", "BTN_TRIGGER", \
			logging_level=self.logging_level)
		self.btn_x = Button("X", "Key", "BTN_TOP", \
			logging_level=self.logging_level)
		self.btn_y = Button("Y", "Key", "BTN_THUMB2", \
			logging_level=self.logging_level)
		# 右侧顶部按键
		self.btn_r1 = Button("R1", "Key", "BTN_PINKIE", \
			logging_level=self.logging_level)
		self.btn_r2 = Button("R2", "Key", "BTN_BASE2", \
			logging_level=self.logging_level)
		# 左侧顶部按键
		self.btn_l1 = Button("L1", "Key", "BTN_TOP2", \
			logging_level=self.logging_level)
		self.btn_l2 = Button("L2", "Key", "BTN_BASE", \
			logging_level=self.logging_level)
		# 左侧十字按键
		self.btn_up = CrossButtonSingle("UP", "Absolute", "ABS_HAT0Y", \
			button_click_value=CrossButtonSingleValue.BUTTON_CLICK1, \
			logging_level=self.logging_level)
		self.btn_down = CrossButtonSingle("DOWN", "Absolute", "ABS_HAT0Y", \
			button_click_value=CrossButtonSingleValue.BUTTON_CLICK2, \
			logging_level=self.logging_level)
		self.btn_left = CrossButtonSingle("LEFT", "Absolute", "ABS_HAT0X", \
			button_click_value=CrossButtonSingleValue.BUTTON_CLICK1, \
			logging_level=self.logging_level)
		self.btn_right = CrossButtonSingle("RIGHT", "Absolute", "ABS_HAT0X",
			button_click_value=CrossButtonSingleValue.BUTTON_CLICK2,
			logging_level=self.logging_level)
		self.btn_cross = CrossButton("CROSS_BUTTON", self.btn_up, self.btn_down,\
			self.btn_left, self.btn_right, logging_level=self.logging_level)
		# 左侧遥杆
		self.left_joystick_x = JoyStickAxis("LEFT_JOYSTICK_X", "Absolute", "ABS_X", \
			logging_level=self.logging_level)
		self.left_joystick_y = JoyStickAxis("LEFT_JOYSTICK_Y", "Absolute", "ABS_Y", \
			logging_level=self.logging_level)
		self.left_joystick = JoyStick("LEFT_JOYSTICK", self.left_joystick_x, \
			self.left_joystick_y, logging_level=self.logging_level)
		# 右侧遥感
		self.right_joystick_x = JoyStickAxis("RIGHT_JOYSTICK_X", "Absolute", "ABS_Z", \
			logging_level=self.logging_level)
		self.right_joystick_y = JoyStickAxis("RIGHT_JOYSTICK_Y", "Absolute", "ABS_RZ", \
			logging_level=self.logging_level)
		self.right_joystick = JoyStick("RIGHT_JOYSTICK", self.right_joystick_x, \
			self.right_joystick_y, logging_level=self.logging_level)
		
'''
游戏手柄
'''
import time
from threading import Event, Thread
from inputs import get_gamepad
from sympy import EX

from sensor.sensor import Sensor
from sensor.button import Button
from utils.logger_interface import LoggerInterface
from utils.thread import KillableThread

class EventListenerThread(Thread):
	'''事件监听线程'''
	def __init__(self, gamepad):
		self.stop_event = Event()
		self.gamepad = gamepad
		super().__init__()
		
	def run(self):
		while True:
			# print("...")
			try:
				if self.stop_event.is_set():
					print("退出")
					break
				# 事件监听
				self.gamepad.event_listener()
				time.sleep(0.001)
			except Exception as e:
				print(e)
	def stop(self):
		'''停止'''
		self.stop_event.set()
		print(f"self.stop_event.set() = {self.stop_event.is_set()}")
	
class GamePad(LoggerInterface):
	'''游戏手柄'''
	def __init__(self, name="Gamepad", logging_level=None) -> None:
		'''构造器'''
		# 父类初始化
		super().__init__(name=name, logging_level=logging_level)
		# 传感器初始化
		self.init_sensor()
		# 初始化事件-传感器映射字典
		self.init_event_sensor_map()
		# 多线程参数
		# self.exit_event = Event()
		# 事件监听线程
		self.event_listener_thread = None
	def init_sensor(self):
		'''传感器初始化'''
		# 根据手柄布局，配置传感器
		pass
		
	def init_event_sensor_map(self):
		'''初始化事件-传感器映射字典'''
		self.event_sensor_map = {}
		for key, sensor in self.__dict__.items():
			# 判断是否是Sensor对象
			if isinstance(sensor, Sensor):
				# 使用事件代码作为主键
				# 允许多个sensor订阅同一个code
				if sensor.event_code in self.event_sensor_map:
					self.event_sensor_map[sensor.event_code].append(sensor)
				else:
					self.event_sensor_map[sensor.event_code] = [sensor,]
				
		# print(self.event_sensor_map)
	
	def event_listener(self):
		'''事件监听'''
		# 遍历事件(这个函数是阻塞的)
		# 如果没有事件发生，则会一直卡在这里
		# PROBLEM: inputs里面的device.read函数没有超时机制
		events =  get_gamepad()
		for event in events:
			# self.logger.info("事件捕获")
			# self.logger.info(f"设备名: {event.device} 触发时间: {event.timestamp}")
			# 数据类型 |字符串|字符串|整数|
			# self.logger.info(f"事件类型: {event.ev_type} | 事件代码: {event.code} | 事件状态: {event.state}")  # 字符串
			# 判断事件是否在映射地图里
			if event.code not in self.event_sensor_map:
				# self.logger.info(f"未知事件代码: {event.code}")
				continue
			# 获取该传感器
			sensor_list = self.event_sensor_map[event.code]
			# 执行回调函数
			for sensor in sensor_list:
				# self.logger.info(f"响应传感器: {sensor.name}")
				sensor.event_handler(event)
	
	# def event_listener_loop(self):
	# 	'''事件监听器'''
	# 	while True:
	# 		# 退出
	# 		# if self.exit_event.is_set():
	# 		# 	break
	# 		# 事件监听
	# 		self.event_listener()
	
	def start_event_listener_thread(self):
		'''开启事件监听器线程'''
		# 创建线程
		self.event_listener_thread = EventListenerThread(self)
		# 开启线程
		self.event_listener_thread.start()
	
	def stop_event_listener_thread(self):
		'''停止事件监听器线程'''
		# 线程停止
		self.event_listener_thread.stop()
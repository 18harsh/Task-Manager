# from kivmob import KivMob, TestIds
from kivy.app import App
from .view import MainWindow

from kivy.clock import Clock

class MainApp(App):
	def build(self):
		# self.ads = KivMob(TestIds.APP)
		# self.ads.new_banner(TestIds.BANNER,top_pos=False)
		# self.ads.new_interstitial(TestIds.INTERSTITIAL)
		# self.ads.request_interstitial()
		# self.ads.request_banner()

		# # self.ads.show_banner()
		# Clock.schedule_interval(lambda x: self.ads.show_interstitial(),5*60)

		mainwin = MainWindow()
		return mainwin

	# def on_resume(self):
	# 	self.ads.request_interstitial()
	# 	self.ads.show_interstitial()
  
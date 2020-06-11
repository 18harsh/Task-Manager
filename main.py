# python main.py --size=320x645 --dpi=96
from app import MainApp
from kivy.garden.iconfonts import register

from os.path import dirname,join

if __name__=="__main__":
	register('MatIcons',join(dirname(__file__),'app/assets/fonts/Material-Design-Iconic-Font.ttf'),join(dirname(__file__),'app/assets/fonts/zmd.fontd'))
	MainApp().run() 
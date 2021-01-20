from tkinter import *


class Resource:

	def __init__(self):
		self.images = {}
		self.images["Floor"] = self.load_image("./images/Floor.gif")
		self.images["Wall"] = self.load_image("./images/Wall.gif")
		self.images["Hero-down"] = self.load_image("./images/Hero-down.gif")
		self.images["Hero-right"] = self.load_image("./images/Hero-right.gif")
		self.images["Hero-left"] = self.load_image("./images/Hero-left.gif")
		self.images["Hero-up"] = self.load_image("./images/Hero-up.gif")
		self.images["Boss"] = self.load_image("images/Boss.gif")
		self.images["Skeleton"] = self.load_image("./images/Skeleton.gif")



	def load_image(self, path):

		img = PhotoImage(file=path)
		return img

	def get_image(self, key):
		return self.images[key]
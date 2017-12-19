#!/usr/local/bin/python
#coding:utf-8
#电影网站 定义Movie类
import webbrowser

class Movie():
	"""This class is used to create Movie object"""
	def __init__(self,title,storyline,poster_image,release_date,trailer_url):
		"""init movie class with title、storyline、poster_image、release_date、trailer_url"""
		self.title = title
		self.storyline = storyline
		self.poster_image = poster_image
		self.release_date = release_date
		self.trailer_url = trailer_url

	def show_trailer(self):
		"""open a browser with the url of movie trailer"""
		webbrowser.open(self.trailer_url)
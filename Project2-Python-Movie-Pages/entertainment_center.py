#!/usr/local/bin/python
#coding:utf-8
#电影网站 生成电影实例和页面

import media
import fresh_tomatoes

the_myth = media.Movie("神话",
	"讲述秦朝时期一位将军和公主骨铭心的爱情故事",
	"http://img.sootuu.com/Exchange/2009-11/2009112013521200.jpg",
	"2005-09-23",
	"http://www.iqiyi.com/v_19rrhx58uo.html")

kingsman = media.Movie("特工学院:王牌特工",
	"一部特工主题的科幻动作片",
	"https://img3.doubanio.com/view/photo/l/public/p2231932406.webp",
	"2015-03-27",
	"http://www.iqiyi.com/v_19rrnqzc4g.html")

the_shawshank_redemption = media.Movie("肖申克的救赎",
	"讲述了银行家安迪由于冤案被关进监狱最终靠努力实现救赎重获自由的励志故事",
	"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp",
	"1994-09-10",
	"http://www.iqiyi.com/v_19rra0h3wg.html")

the_pursuit_of_happyness = media.Movie("当幸福来敲门",
	"讲述了一位医疗器械推销员在生活困境面前积极努力，最终获得股票投资公司实习岗位改变人生的故事",
	"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1312700628.webp",
	"2008-01-17",
	"http://www.iqiyi.com/v_19rrk3nlys.html")


movies = [the_myth,kingsman,the_shawshank_redemption,the_pursuit_of_happyness]

fresh_tomatoes.open_movies_page(movies)

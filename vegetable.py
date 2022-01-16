

from typing import List
from vegetableModel import VegetableModel

class Vegetable:
	def __init__(self):
		self.file_name = 'zoldseg.txt'
		self.vegetables: List[VegetableModel] = []
		self.lines = []
	
	def read_content(self):
		fp = open(self.file_name, 'r', encoding='utf-8')
		self.lines = fp.readlines()
		fp.close()
	
	def convert_content(self):
		for line in self.lines[1::]:
			(id, name, quantity, price, site) = line.split(';')
			vegetableModel = VegetableModel(
				id, name, int(quantity), int(price), site
			)
			self.vegetables.append(vegetableModel)
	
	def print_all(self):
		for vegetable in self.vegetables:
			print(
				vegetable.name,
				vegetable.site,
				vegetable.quantity
				)
	
	# A Szolnokon található zöldséget össz tömegét
	def szolnok_sum_wight(self):
		osszeg = 0
		for vegetable in self.vegetables:
			if vegetable.site.find('Szolnok') != -1 :
				osszeg += vegetable.quantity
		print("A Szolnokon található zöldséget össz tömegét: ", osszeg)
			
			

	# Melyik telephelyen van értékben legtöbb zöldség
	def most_valuable_vegetables(self):
		max_vegetable = self.vegetables[0]
		for vegetable in self.vegetables:
			if vegetable.price < max_vegetable.price:
				max_vegetable = vegetable
		print("legtöbb zöldség itt van: ",max_vegetable.site)

vegetable = Vegetable()
vegetable.read_content()
vegetable.convert_content()
vegetable.print_all()
vegetable.szolnok_sum_wight()
vegetable.most_valuable_vegetables()

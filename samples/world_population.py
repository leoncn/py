import json
from pygal.maps.world import COUNTRIES

class WorldPopulation():
	"""World population by year"""
	def __init__(self):
		self.by_years = {}
		data_source = "population_data.json"

		with open(data_source) as f:
			data = json.load(f)

		for pop_item in data:
			year = int(pop_item['Year'])
			if not year in self.by_years:
				self.by_years[year] = {}

			code_and_pop = self.__country_pop(pop_item)
			if code_and_pop:
				self.by_years[year].update(code_and_pop)

	def pop_of(self, year= 2010):
		return self.by_years[year]

	def __country_pop(self, pop):
		c_code = self.__country_code(pop['Country Name'])

		if c_code:
			return {c_code : int(float(pop['Value']))}

		return None

	def __country_code(self, country):
		for code, name in COUNTRIES.items():
			if name == country:
				return code
		return None
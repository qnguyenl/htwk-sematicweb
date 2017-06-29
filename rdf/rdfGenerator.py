from rdflib import URIRef, BNode, Literal, Namespace, Graph
from rdflib.namespace import NamespaceManager
import json
import csv

g = Graph()
namespace_manager = NamespaceManager(g)
nCar = Namespace("http://www.imn.htwk-leipzig.de/qnguyenl/car/")
nBrand = Namespace("http://www.imn.htwk-leipzig.de/qnguyenl/brand/")
nPlz = Namespace("http://www.imn.htwk-leipzig.de/qnguyenl/plz/")
nState = Namespace("http://www.imn.htwk-leipzig.de/qnguyenl/state/")
namespace_manager.bind('car',nCar)
namespace_manager.bind('brand',nBrand)
namespace_manager.bind('plz',nPlz)
namespace_manager.bind('state',nState)
with open('./data/mobile/mobile.json') as json_data:
	cars = json.load(json_data)
	for car in cars:
		c = nCar[car['id']]
		g.add((c,nCar['name'],Literal(car['name'])))
		g.add((c,nCar['price'],Literal(car['price'])))
		g.add((c,nCar['brand'],nBrand[car['brandId']]))
		g.add((c,nCar['plz'],nPlz[car['location']]))
		#g.serialize('car.xml',format="xml")

with open('./data/mobile_de_brand/mobile_de_brand.json') as json_data:
	brands = json.load(json_data)
	for brand in brands:
		b = nBrand[brand['id']]
		g.add((b,nBrand['name'],Literal(brand['name'])))

with open('./data/plz/zuordnung_plz_ort.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		plz = nPlz[row[2]]
		g.add((plz,nPlz['state'],nState[row[3]]))

with open('./data/population/population.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=';', quotechar='"')
	for row in reader:
		state = nState[row[0]]
		g.add((state,nState['name'],Literal(row[0])))
		g.add((state,nState['populationTotal'],Literal(row[2])))
		g.add((state,nState['populationEachKm2'],Literal(row[5])))
g.serialize('./data/result/data.rdf',format="xml",encoding="utf-8")
g.close()
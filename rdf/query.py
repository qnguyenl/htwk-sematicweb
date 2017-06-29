import rdflib
import csv
from rdflib import Graph
from rdflib.plugins.sparql.results.csvresults import CSVResultSerializer

g = Graph()
g.parse("./data/result/data.rdf",format="xml")
q = """SELECT ?stateName (COUNT(?car) AS ?ANZAHL) ?population
		WHERE {
			?car car:plz ?plz .
			?plz plz:state ?state .
			?state state:name ?stateName ;
					state:populationEachKm2 ?population .
		}
		GROUP BY ?state 
		"""
rs = g.query(q)
with open('./data/result/spraqlResult.csv','w') as csvfile:
	write = csv.writer(csvfile, delimiter=',', quotechar='"')
	write.writerow(['Bundesland','cars','Einwohnerzahl je Km2'])
	for row in rs.result:
		print('%s %s %s' % row)
		write.writerow(row)
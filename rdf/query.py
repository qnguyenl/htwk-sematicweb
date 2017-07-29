import rdflib
import csv
from rdflib import Graph
from rdflib.plugins.sparql.results.csvresults import CSVResultSerializer

g = Graph()
g.parse("../data/result/data.rdf",format="xml")
q = """SELECT ?stateName (COUNT(?car) AS ?ANZAHL) ?brandName
		WHERE {
			?car car:plz ?plz ;
				car:brand ?brand .
			?brand brand:name ?brandName .
			?plz plz:state ?state .
			?state state:name ?stateName .
			FILTER regex(?stateName, "^Sachsen") 
		}
		GROUP BY ?state ?brand
		ORDER BY ?stateName DESC(?ANZAHL) LIMIT 5
		"""
rs = g.query(q)
with open('../data/result/spraqlResult.csv','w') as csvfile:
	write = csv.writer(csvfile, delimiter=',', quotechar='"')
	write.writerow(['Bundesland','cars','Brand'])
	for row in rs.result:
		#print('%s %s %s' % row)
		write.writerow(row)
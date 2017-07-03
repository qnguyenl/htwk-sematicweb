# htwk-sematicweb
Sematic web Projekt
Zusammenhang zwischen der Einwohnerzahl und der Anzahl der Angebote von "Brand new" Luxusauto in den Bundesländern

#Ergebnisse
Beispiel für Anfragen:
1. Anzahl der Autoangeboten im vergleichen mit Einwohnerzahl je Km2 in Bundesländern.
* SPARQL
```sparql
SELECT ?stateName (COUNT(?car) AS ?cars) ?populationEachKm2 
WHERE {
     ?car car:plz ?plz .
     ?plz plz:state ?state .
     ?state state:name ?stateName ;
     	state:populationEachKm2 ? populationEachKm2 .
} GROUP BY ?state
```

* Ergebnisse als Tabelle
Bundesland | Cars | Einwohnerzahl je Km2
------------ | ------------- | -------------
Nordrhein-Westfalen|3238|524
Brandenburg|357|84
Baden-Württemberg|1495|304
Niedersachsen|723|167
Bayern|2348|182
Sachsen|389|221
Rheinland-Pfalz|363|204
Hessen|717|293
Schleswig-Holstein|249|181
Thüringen|169|134
Sachsen-Anhalt|134|110
Berlin|357|3948
Mecklenburg-Vorpommern|53|69
Hamburg|268|2366
Saarland|25|388
Bremen|206|1599

* Ergebnisse Chart
![alt tag](https://raw.https://github.com/qnguyenl/htwk-sematicweb/master/data/result/chart2.png)

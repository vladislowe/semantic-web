from SPARQLWrapper import SPARQLWrapper, JSON

'''
в запиті беруть участь не тільки країни, а й регіони, етнічні групи, 
штати, держави, яких вже не існує, континенти, і навіть замки :(

Тому запит повертає континенти у якості "країн" з найбільшою площею
'''

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    SELECT ?country ?area
    WHERE {
        ?country rdf:type dbo:Country .
        ?country dbo:language dbr:English_language .
        ?country dbo:areaTotal ?area .
    }
    ORDER BY DESC(?area)
""")

sparql.setReturnFormat(JSON)
query_res = sparql.query().convert()

for result in query_res["results"]["bindings"]:
    print(f'Країна: {result["country"]["value"]}, площа: {result["area"]["value"]}')
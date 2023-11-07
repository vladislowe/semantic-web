from rdflib import Graph, URIRef

g = Graph()
g.parse("countrues_info.ttl")

continents_population = {} #pairs continent:population

for subj, pred, obj in g:
    if pred == URIRef("http://example.com/demo/population"):
        continent = g.value(subject=subj, predicate=URIRef("http://example.com/demo/part_of_continent"))

        # якщо континент уже є в словнику, інакше додаємо його
        if str(continent) in continents_population:
            continents_population[str(continent)] += int(obj)
        else:
            continents_population[str(continent)] = int(obj)


for key in continents_population:
    print(f"{key} - {continents_population[key]}")
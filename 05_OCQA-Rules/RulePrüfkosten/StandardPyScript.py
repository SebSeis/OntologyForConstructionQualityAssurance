from rdflib import Graph
from pyshacl import validate

shape_graph_file = \
    'C:/Users/verwalter/OneDrive - Technische Universität Ilmenau/03_Promotion/03_Veröffentlichungen/ECPPM_Judith/02_Rules/testdata.ttl'

shacl_ttl_file = \
    'C:/Users/verwalter/OneDrive - Technische Universität Ilmenau/03_Promotion/03_Veröffentlichungen/ECPPM_Judith/02_Rules/rulefiles.ttl'

shape_graph = Graph().parse(source=shape_graph_file, format="turtle")
data_graph = Graph().parse(source=shacl_ttl_file, format="turtle")
data_graph_orig = Graph()
for t in data_graph:
    data_graph_orig.add(t)  

conforms, result_graph, result_text = validate(data_graph, shacl_graph=shape_graph, advanced=True, inference='none', debug=True, js=True)
#assert not conforms
added_triples = data_graph - data_graph_orig
print('Added triples: ', len(added_triples))
print(data_graph.serialize(format="turtle"))
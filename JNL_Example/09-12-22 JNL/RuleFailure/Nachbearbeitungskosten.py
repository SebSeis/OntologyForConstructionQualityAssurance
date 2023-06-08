from rdflib import Graph
from pyshacl import validate

shape_graph_file = \
    'C:/Users/verwalter/Documents/GitHub/OntologyForConstructionQualityAssurance/07_JNL_Example/09-12-22 JNL/RuleFailure/221210_RegelNacharbeitungskosten.ttl'

shacl_ttl_file = \
    'C:/Users/verwalter/Documents/GitHub/OntologyForConstructionQualityAssurance/07_JNL_Example/09-12-22 JNL/RuleFailure/FailureCosts.ttl'
    #'C:/Users/verwalter/OneDrive - Technische Universität Ilmenau/03_Promotion/03_Veröffentlichungen/ECPPM_Judith/02_Rules/rulefiles.ttl'

shape_graph = Graph().parse(source=shape_graph_file, format="turtle")
data_graph = Graph().parse(source=shacl_ttl_file, format="turtle")
data_graph_orig = Graph()
for t in data_graph:
    data_graph_orig.add(t)  

conforms, result_graph, result_text = validate(data_graph, shacl_graph=shape_graph, advanced=True, inference='none', debug=True, js=True)
#assert not conforms
added_triples = data_graph - data_graph_orig
print('Added triples: ', len(added_triples))
print(added_triples.serialize(format="turtle"))

knows_query = """
            	base          <https://www.qualityAssurence.de/DuplexHouset#> 
prefix ifc:   <https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2/OWL#> 
prefix inst:  <https://www.qualityAssurence.de/DuplexHouset#> 
prefix list:  <https://w3id.org/list#> 
prefix express: <https://w3id.org/express#> 
prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix xsd:   <http://www.w3.org/2001/XMLSchema#> 
#prefix schema:   <https://schema.org#> 
prefix owl:   <http://www.w3.org/2002/07/owl#> 
prefix ex: <http://www.semanticweb.org/verwalter/ontologies/2022/1/Example_Screed_Sichtpruefung#>
prefix dico: <https://w3id.org/digitalconstruction/0.5/Processes#>
prefix ocqa:                <https://w3id.org/ocqa#>
prefix nivellement:                <https://w3id.org/ocqa/0.3/JNL2022Masterarbeit/Erweiterung/Nivellement#>
prefix erweiterung:                <https://w3id.org/ocqa/0.3/JNL2022Masterarbeit/Erweiterung#>

			SELECT #{
				?test ?propertyLohn ?Lohnkosten ?Dauer ?InspectionCost
                #ocqa:hasInspectionCost ?InspectionCost.
			#}
			WHERE {
                ?test   rdf:type nivellement:Nivellement;
				        ocqa:hasCharacteristicInspectionDuration ?propertyDauer;
                        ocqa:hasCharacteristicInspectionLohn ?propertyLohn.
				?propertyLohn schema:value ?Lohnkosten.
				?propertyDauer schema:value ?Dauer.
				BIND (?Lohnkosten * ?Dauer AS ?InspectionCost).
			}"""
#print(data_graph.serialize(format="turtle"))
print(shape_graph.serialize(format="turtle"))
qres = data_graph.query(knows_query)
print (qres)
for row in qres:
    #print(f"{row.this}")
	print(row)  


knows_query2 = """
            	base          <https://www.qualityAssurence.de/DuplexHouset#> 
prefix ifc:   <https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2/OWL#> 
prefix inst:  <https://www.qualityAssurence.de/DuplexHouset#> 
prefix list:  <https://w3id.org/list#> 
prefix express: <https://w3id.org/express#> 
prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix xsd:   <http://www.w3.org/2001/XMLSchema#> 
#prefix schema:   <https://schema.org#> 
prefix owl:   <http://www.w3.org/2002/07/owl#> 
prefix ex: <http://www.semanticweb.org/verwalter/ontologies/2022/1/Example_Screed_Sichtpruefung#>
prefix dico: <https://w3id.org/digitalconstruction/0.5/Processes#>
prefix ocqa:                <https://w3id.org/ocqa#>
prefix nivellement:                <https://w3id.org/ocqa/0.3/JNL2022Masterarbeit/Erweiterung/Nivellement#>
prefix erweiterung:                <https://w3id.org/ocqa/0.3/JNL2022Masterarbeit/Erweiterung#>

			SELECT #{
				?x ?propertyBauteilkosten ?propertyMehrkostenSatz ?PostPerformanceCosts
			#}
			WHERE {
                ?x   rdf:type erweiterung:VirtualDefect;
					ocqa:hasCharacteristicBauteilkosten ?propertyBauteilkosten;
                    ocqa:hasCharacteristicRepairPercentage ?propertyMehrkostenSatz.
				?propertyBauteilkosten schema:value ?Bauteilkosten.
				?propertyMehrkostenSatz schema:value ?Mehrkosten.
				BIND (?Bauteilkosten * ?Mehrkosten AS ?PostPerformanceCosts).
			}"""

qres2 = data_graph.query(knows_query2)
print (qres2)
for row in qres2:
    #print(f"{row.this}")
	print(row)  
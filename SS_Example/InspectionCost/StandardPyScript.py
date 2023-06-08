from rdflib import Graph
from pyshacl import validate

shape_graph_file = \
    'C:/Users/verwalter/Documents/GitHub/OntologyForConstructionQualityAssurance/06_Example/InspectionCost/RegelPruefkosten.ttl'
#C:\Users\verwalter\Documents\GitHub\OntologyForConstructionQualityAssurance\06_Example\InspectionCost
shacl_ttl_file = \
    'C:/Users/verwalter/Documents/GitHub/OntologyForConstructionQualityAssurance/06_Example/InspectionCost/merged2.ttl'
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
prefix rdfs:               <http://www.w3.org/2000/01/rdf-schema#>
#prefix schema:   <http://schema.org> 
prefix owl:   <http://www.w3.org/2002/07/owl#> 
prefix dico: <https://w3id.org/digitalconstruction/0.5/Processes#>
prefix ocqa:                <https://w3id.org/ocqa#>
prefix nivellement:                <https://w3id.org/ocqa/0.3/JNL2022Masterarbeit/Erweiterung/Nivellement#>
prefix ex:                 <http://www.semanticweb.org/exampleInspectionCost#>
prefix erweiterung:                <https://w3id.org/ocqa/0.3/JNL2022Masterarbeit/Erweiterung#>

			#SELECT 
			#	?test ?test2
			#
			#WHERE {
            #    ?test ocqa:hasInspectionEquipment/ocqa:hasCostPerUnitCharacteristic/ocqa:hasCharacteristicState/schema:value ?test2
			#}
            SELECT (SUM(?InspectionCost) AS ?test)
    			WHERE {
      					$this ocqa:hasLabourCostPerInspection  ?InspectionCost;
								#ocqa:hasFixCostPerInspection ?InspectionCost.
    				}"""
#print(data_graph.serialize(format="turtle"))

qres = data_graph.query(knows_query)
print (qres)
for row in qres:
    #print(f"{row.this}")
	print(row)  
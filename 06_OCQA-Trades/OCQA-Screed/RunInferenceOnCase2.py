from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery
import owlrl

def load_ontology(file_path):
    """
    Load ontology from a Turtle file.
    """
    g = Graph()
    g.parse(file_path, format="turtle")
    return g

def apply_reasoning(graph):
    """
    Perform OWL reasoning on the RDF graph.
    """
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(graph)

def query_graph(graph, query_string):
    """
    Execute a SPARQL query on the RDF graph.
    """
    query = prepareQuery(query_string)
    return graph.query(query)

if __name__ == "__main__":
    # Load OCQA ontology from a Turtle file
    ontology_file = "path/to/your/OCQA_ontology.ttl"
    g = load_ontology(ontology_file)
    
    # Apply OWL reasoning
    apply_reasoning(g)
    
    # Example SPARQL query to find all individuals of a certain class
    query_string = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX your_prefix: <http://www.example.org/your_ontology#>
    
    SELECT ?individual WHERE {
        ?individual rdf:type your_prefix:YourClass .
    }
    """
    
    results = query_graph(g, query_string)
    
    for row in results:
        print(f"Individual found: {row[0]}")

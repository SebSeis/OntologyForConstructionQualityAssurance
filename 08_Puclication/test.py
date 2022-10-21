from pylode import OntDoc
from pathlib import Path
# initialise
#od = OntDoc(ontology="C:/Users/verwalter/Documents/GitHub/OntologyForConstructionQualityAssurance/08_Puclication/OCQA03.ttl")
od = OntDoc(Path(__file__).parent / "OCQA_03.ttl")
# produce HTML
#html = od.make_html()

# or save HTML to a file
od.make_html(destination="OCQA_03some-resulting-html-file.html")
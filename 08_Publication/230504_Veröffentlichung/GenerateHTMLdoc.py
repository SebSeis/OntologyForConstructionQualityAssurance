#from pylode import OntDoc
from pylode import OntDoc, MakeDocco, APP_DIR
from pathlib import Path
from os.path import join, dirname, abspath

####ALTE VERSION####
#od = OntDoc(Path(__file__).parent / "OCQA_03.ttl")
## or save HTML to a file
#od.make_html(destination="OCQA_03_DOC.html")

####OBPA VERSION ####
TESTS_DIR = dirname(abspath(__file__))
print(TESTS_DIR)
print(join(TESTS_DIR, "OCQA_03.ttl"))
#od=OntDoc(default_language="en",source_info=input_rdf, g=input_rdf)
h = MakeDocco(input_data_file=join(TESTS_DIR, "OCQA_03.ttl"), outputformat="html")
# generate the HTML doc
h.document(destination=join(TESTS_DIR, "OCQA_03_DOC.html"))
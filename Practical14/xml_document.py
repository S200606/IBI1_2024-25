import xml.dom.minidom
import datetime
import xml.sax

start = datetime.datetime.now()
DOMTree = xml.dom.minidom.parse(r"C:\Users\jjbcs\Desktop\IBI\IBI_2024-25\IBI1_2024-25\Practical14\go_obo.xml")
root = DOMTree.documentElement

namespaces = ['molecular_function', 'biological_process', 'cellular_component']

results = {namespace: {'count': 0, 'max_term': None,"max_term_name":None, 'max_elsements': 0} for namespace in namespaces}


for term in root.getElementsByTagName('term'):
    tag_nodes = term.getElementsByTagName('namespace')
    if not tag_nodes or not tag_nodes[0].firstChild:
        continue
    tag = tag_nodes[0].firstChild.nodeValue
    if tag in namespaces:
        results[tag]['count'] += 1
        element_number = len(term.getElementsByTagName('is_a'))
        if element_number > results[tag]['max_elsements']:
            results[tag]['max_elsements'] = element_number
            id_nodes = term.getElementsByTagName('id')
            name_nodes = term.getElementsByTagName('name')
            if id_nodes and id_nodes[0].firstChild:
                results[tag]['max_term'] = id_nodes[0].firstChild.nodeValue
            if name_nodes and name_nodes[0].firstChild:
                results[tag]['max_term_name'] = name_nodes[0].firstChild.nodeValue


end_time = datetime.datetime.now()
elapsed_time = (end_time - start).total_seconds()

print("DOM results:")
for namespace in namespaces:
    print(f"Namespace: {namespace}")
    print(f"Number of terms: {results[namespace]['count']}")
    print(f"Term with the most is_a elements: {results[namespace]['max_term']}({results[namespace]['max_term_name']})")
    print(f"Number of is_a elements: {results[namespace]['max_elsements']}")
    print()

print(f"Elapsed time: {elapsed_time:.2f} seconds")


class OBOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.namespaces = ['molecular_function', 'biological_process', 'cellular_component']
        self.results = {namespace: {'count': 0, 'max_term': None, 'max_elsements': 0} for namespace in self.namespaces}
        self.in_term = False
        self.in_namespace = False
        self.in_name = False
        self.in_id = False
        self.current_namespace = ''
        self.current_name = ''
        self.current_id = ''
        self.current_is_a_count = 0

    def startElement(self, name, attrs):
        if name == 'term':
            self.in_term = True
            self.current_namespace = ''  
            self.current_name = ''
            self.current_id = ''
            self.current_is_a_count = 0
        elif self.in_term and name == 'namespace':
            self.in_namespace = True
        elif self.in_term and name == 'name':
            self.in_name = True
        elif self.in_term and name == 'is_a':
            self.current_is_a_count += 1
        elif self.in_term and name == 'id':
            self.in_id = True
    
    def endElement(self, name):
        if name == 'term' and self.current_namespace in self.namespaces:
            namespace = self.current_namespace
            self.results[namespace]['count'] += 1
            if self.current_is_a_count > self.results[namespace]['max_elsements']:
                self.results[namespace]['max_elsements'] = self.current_is_a_count
                self.results[namespace]['max_term_id'] = self.current_id
                self.results[namespace]['max_term_name'] = self.current_name
            self.in_term = False
        elif name == 'namespace':
            self.in_namespace = False   
        elif name == 'name':
            self.in_name = False
        elif name == 'id':
            self.in_id = False
    
    def characters(self, content):
        if self.in_namespace:
            self.current_namespace += content.strip()
        elif self.in_name:
            self.current_name += content.strip()
        elif self.in_id:
            self.current_id += content.strip()

if __name__ == "__main__":
    start = datetime.datetime.now()
    parser = xml.sax.make_parser()
    handler = OBOHandler()
    parser.setContentHandler(handler)
    parser.parse(r"C:\Users\jjbcs\Desktop\IBI\IBI_2024-25\IBI1_2024-25\Practical14\go_obo.xml")  

    print("SAX results:")
    for namespace in handler.namespaces:
        print(f"Namespace: {namespace}")
        print(f"Number of terms: {handler.results[namespace]['count']}")
        print(f"Number of is_a elements: {handler.results[namespace]['max_elsements']}")
        print(f"  Term with max elements: {handler.results[namespace]['max_term_name']}({handler.results[namespace]['max_term_id']})")
        print()

    end = datetime.datetime.now()
    elapsed_time = (end - start).total_seconds()
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

#sax is faster than dom
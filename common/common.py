from rdflib import *

dmop = Namespace('http://www.e-lico.eu/ontologies/dmo/DMOP/DMOP.owl#')
do = Namespace('https://diviloper.dev/ontology#')
dtbox = do
ds = Namespace('https://diviloper.dev/ontology/shapes#')
da = Namespace('https://diviloper.dev/ontology/ABOX#')
dabox = da
dd = Namespace('https://diviloper.dev/ontology/Data#')
dw = Namespace('https://diviloper.dev/ontology/Workflow#')


def get_graph():
    g = Graph()
    g.bind('dmop', dmop)
    g.bind('dtbox', do)
    g.bind('dshapes', ds)
    g.bind('dabox', da)
    g.bind('ddata', dd)
    g.bind('dworkflow', dw)
    return g
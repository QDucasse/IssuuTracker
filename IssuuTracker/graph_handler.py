'''
created on: 16/11/2019-12:45
by: QDucasse
'''

from graphviz import Digraph
from loader import *

def create_graph(df,base_visitor_uuid,base_document_uuid):
    '''
    Create a dot graph for the 'also likes' property.
    Parameters
    ==========
    df: Pandas.DataFrame
        Dataset extracted from the site.
    visitor_uuid: string
        UUID of the input visitor.
    doc_uuid: string
        UUID of the input document.

    Returns
    =======
    graph: Digraph
        Digraph object with the link established.
    '''
    # Graph definition
    graph = Digraph(name='al'+base_document_uuid[-4:])
    # Visitors list for the input document
    visitors = readers_of_list(df,base_document_uuid)

    # Iterates over visitors UUIDs to create their nodes and the ones of the documents
    # they have read.
    graph.attr('node', shape='square')
    for visitor in visitors:
        # Creation of the visitor node
        create_visitor_node(graph,visitor,base_visitor_uuid)

        # List of read documents by the current visitor
        docs = has_read_list(df,visitor)

        # Iterates over documents UUIDs to create their nodes.
        for document in docs:
            # Creation of the document node + visitor->document edge if the
            # document node is not already defined. Else, only the edge is created
            create_document_node(graph,document,base_document_uuid,visitor)
    graph.render('./graphs/'+graph.name,view=True)
    return graph

def create_visitor_node(graph,visitor_uuid,base_visitor_uuid):
    '''
    Check if the visitor UUID is the one of the base visitor and therefore needs
    to be drawn in green or simply adds the visitor node to the graph.
    Parameters
    ==========
    graph: Digraph
        Graph object where the node have to be added.
    visitor_uuid: string
        UUID of the current visitor being processed.
    base_visitor_uuid: string
        UUID of the base visitor UUID input to create the graph.
    '''
    # If the current visitor is the base one, it needs to be added in green.
    graph.attr('node',shape='square')
    if visitor_uuid == base_visitor_uuid:
        graph.attr('node',style='filled',color='green')
    graph.node(visitor_uuid[-4:])
    graph.attr('node',style='solid',color='black')

def create_document_node(graph,document_uuid,base_document_uuid,visitor_uuid):
    '''
    Check if the document UUID is the one of the base document and therefore needs
    to be drawn in green. Then check if the document node has already been added
    and create it if not. Then link the document node to the visitor node.
    Parameters
    ==========
    graph: Digraph
        Graph object where the node have to be added.
    document_uuid: string
        UUID of the current document being processed.
    base_document_uuid: string
        UUID of the base document UUID input to create the graph.
    visitor_uuid: string
        UUID of the visitor that has read the document.
    '''
    graph.attr('node',shape='circle')
    if document_uuid == base_document_uuid:
        graph.attr('node',style='filled',color='green')

    if not(document_uuid in graph.node_attr):
        graph.node(document_uuid[-4:])
        graph.edge(visitor_uuid[-4:],document_uuid[-4:])
    else:
        graph.edge(visitor_uuid[-4:],document_uuid[-4:])

    graph.attr('node',style='solid',color='black')


if __name__ == "__main__":
    full_df = load_dataset_json(path_base_dataset)
    smpl_df = load_dataset_json(path_smpl_dataset)
    # graph = create_graph(full_df,'bd378ce6df7cb9cd','130228184234-6fd07690237d48aaa7be4e20cb767b13')
    graph = create_graph(full_df,'2f63e0cca690da91','140219141540-c900b41f845c67cc08b58911155c681c')

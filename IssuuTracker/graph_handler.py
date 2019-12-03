'''
created on: 16/11/2019-12:45
by: QDucasse
'''

from graphviz import Digraph
from IssuuTracker.affinity_finder   import AffinityFinder

class GraphHandler:

    def __init__(self,dicts,base_visitor_uuid='',base_document_uuid=''):
        self.dicts = dicts
        self.af = AffinityFinder(dicts)
        self.base_visitor_uuid  = base_visitor_uuid
        self.base_document_uuid = base_document_uuid
        self.graph = Digraph()

    def create_graph(self,dicts=None,base_visitor_uuid=None,base_document_uuid=None):
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
        if dicts is None:
            dicts = self.dicts
        if base_visitor_uuid is None:
            base_visitor_uuid = self.base_visitor_uuid
        if base_document_uuid is None:
            base_document_uuid = self.base_document_uuid

        self.graph.name = 'al'+base_document_uuid[-4:]

        # Also likes document
        al = self.af.also_likes(doc_uuid=base_document_uuid,visitor_uuid=base_visitor_uuid)

        # Visitors list for the input document
        visitors = self.af.readers_of(doc_uuid=base_document_uuid,dicts=dicts)

        # Iterates over visitors UUIDs to create their nodes and the ones of the documents
        # they have read.
        self.graph.attr('node', shape='square')
        for visitor in visitors:
            # Creation of the visitor node
            self.create_visitor_node(visitor,self.graph,base_visitor_uuid)

            # List of read documents by the current visitor
            docs = self.af.has_read(visitor_uuid=visitor,dicts=dicts)

            # Iterates over documents UUIDs to create their nodes.
            for document in docs:
                # Creation of the document node + visitor->document edge if the
                # document node is not already defined. Else, only the edge is created
                if document in al:
                    self.create_document_node(document,visitor,self.graph,base_document_uuid)

        self.graph.render('./graphs/'+self.graph.name,view=True)
        return self.graph

    def create_visitor_node(self,visitor_uuid,graph=None,base_visitor_uuid=None):
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
        if graph is None:
            graph = self.graph
        if base_visitor_uuid is None:
            base_visitor_uuid = self.base_visitor_uuid
        # If the current visitor is the base one, it needs to be added in green.
        graph.attr('node',shape='square')
        if visitor_uuid == base_visitor_uuid:
            graph.attr('node',style='filled',color='green')
        graph.node(visitor_uuid[-4:])
        graph.attr('node',style='solid',color='black')

    def create_document_node(self,document_uuid,visitor_uuid,graph=None,base_document_uuid=None):
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
        if base_document_uuid is None:
            base_document_uuid = self.base_document_uuid

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
    # IMPORT TESTS
    from IssuuTracker.data_loader import DataLoader,path_base_dataset,path_100k_dataset,path_400k_dataset,path_600k_dataset,path_3m_dataset
    # BASE DATASET TESTS
    # ==================
    # dl_base = DataLoader()
    # dl_base.load_dataset_json(path_base_dataset)
    # gh = GraphHandler(dl_base.df)
    # gh.create_graph(dl_full.df,'bd378ce6df7cb9cd','130228184234-6fd07690237d48aaa7be4e20cb767b13')
    # gh.create_graph(dl_full.df,'2f63e0cca690da91','140219141540-c900b41f845c67cc08b58911155c681c')

    # # 100K DATASET TESTS
    # # ==================
    # dl_100k = DataLoader()
    # dl_100k.load_dataset_json(path_100k_dataset)
    # gh = GraphHandler(dl_100k.df)
    # gh.create_graph('00000000deadbeef','100806162735-00000000115598650cb8b514246272b5')
    # gh.create_graph('00000000deadbeef','aaaaaaaaaaaa-00000000df1ad06a86c40000000feadbe')

    # dl_100k = DataLoader()
    # dl_100k.load_dataset_from(path_100k_dataset)
    # gh = GraphHandler(dicts=dl_100k.dicts)
    # gh.create_graph(base_visitor_uuid='00000000deadbeef',base_document_uuid='100806162735-00000000115598650cb8b514246272b5')
    # gh.create_graph(base_visitor_uuid='00000000deadbeef',base_document_uuid='aaaaaaaaaaaa-00000000df1ad06a86c40000000feadbe')


    # # 400K DATASET TESTS
    # # ==================
    # dl_400k = DataLoader()
    # dl_400k.load_dataset_from(path_400k_dataset)
    # gh = GraphHandler(dl_400k.dicts)
    # gh.create_graph(base_document_uuid='140310170010-0000000067dc80801f1df696ae52862b')
    # gh.create_graph(base_document_uuid='140310171202-000000002e5a8ff1f577548fec708d50')

    # # 600K DATASET TESTS
    # # ==================
    # dl_600k = DataLoader()
    # dl_600k.load_dataset_json(path_600k_dataset)
    # gh = GraphHandler(dl_600k.df)
    # gh.create_graph(base_document_uuid='140207031738-eb742a5444c9b73df2d1ec9bff15dae9')
    #
    # # 3M DATASET TESTS
    # # ================
    # dl_3m = DataLoader()
    # dl_3m.load_dataset_json(path_100k_dataset)
    # gh = GraphHandler(dl_3m.df)
    # gh.create_graph(base_document_uuid='140109173556-a4b921ab7619621709b098aa9de4d736')

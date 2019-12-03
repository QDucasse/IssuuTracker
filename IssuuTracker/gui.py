'''
created on: 16/11/2019-12:48
by: QDucasse
'''

import tkinter as tk
from tkinter import filedialog
from IssuuTracker.data_loader     import DataLoader
from IssuuTracker.data_visualiser import DataVisualiser
from IssuuTracker.affinity_finder import AffinityFinder
from IssuuTracker.graph_handler   import GraphHandler

class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.al_list = []
        self.dl = DataLoader()
        self.dv = None
        self.af = None
        self.gh = None
        # GRAPHICAL INITIALISATION
        # ========================

        self.title("ISSUU Tracker")
        self.geometry("650x500")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.df_frame   = tk.Frame(self,padx = 3, pady = 10)
        self.stat_frame = tk.Frame(self,padx = 3, pady = 10)
        self.uuid_frame = tk.Frame(self,padx = 3, pady = 10)
        self.al_frame   = tk.Frame(self,padx = 3, pady = 10)
        self.df_frame.grid(row = 0)
        self.stat_frame.grid(row = 1)
        self.uuid_frame.grid(row = 2)
        self.al_frame.grid(row = 3)

        self.visitor_uuid_entry = tk.Entry(self.uuid_frame)
        self.visitor_uuid_entry.insert("end","2f63e0cca690da91")
        self.visitor_uuid_entry.grid(column = 2, row = 2)
        self.document_uuid_entry = tk.Entry(self.uuid_frame)
        self.document_uuid_entry.insert("end","140219141540-c900b41f845c67cc08b58911155c681c")
        self.document_uuid_entry.grid(column = 2, row = 3)

        self.init_df_frame()
        self.init_stat_frame()
        self.init_uuid_frame()
        self.init_al_frame()

    # Initialisation Functions:
    # =========================
    def init_df_frame(self):

        label_df = tk.Label(self.df_frame,text = "Dataset")
        label_df.grid(column = 0, columnspan = 10,row = 0)
        load_dataset_button = tk.Button(self.df_frame,text = "Choose Dataset",command = self.load_dataset)
        load_dataset_button.grid(column = 0, row = 1)

    def init_stat_frame(self):


        label_stat = tk.Label(self.stat_frame,text = "Statistical visualisations")
        label_stat.grid(column = 0, columnspan = 10,row = 0)

        plot_countries_button = tk.Button(self.stat_frame,text = "Plot Countries",command = self.gui_plot_countries)
        plot_countries_button.grid(column = 0, row = 1)

        plot_continents_button = tk.Button(self.stat_frame,text = "Plot Continents",command = self.gui_plot_continents)
        plot_continents_button.grid(column = 1, row = 1)

        plot_browsers_verbose_button = tk.Button(self.stat_frame,text = "Plot Browsers (Verbose)",command = self.gui_plot_browsers_verbose)
        plot_browsers_verbose_button.grid(column = 2, row = 1)

        plot_browsers_button = tk.Button(self.stat_frame,text = "Plot Browsers",command = self.gui_plot_browsers)
        plot_browsers_button.grid(column = 3, row = 1)


    def init_uuid_frame(self):
        label_uuid = tk.Label(self.uuid_frame,text = "UUIDs")
        label_uuid.grid(column = 0, columnspan = 10,row = 0)

        visitor_uuid_label = tk.Label(self.uuid_frame,text = "Visitor UUID: ")
        visitor_uuid_label.grid(column = 1, row = 2)

        document_uuid_label = tk.Label(self.uuid_frame,text = "Document UUID: ")
        document_uuid_label.grid(column = 1, row = 3)

    def init_al_frame(self):

        al_uuid = tk.Label(self.al_frame,text = "Also Likes")
        al_uuid.grid(column = 0, columnspan = 10,row = 0)

        al_list_button = tk.Button(self.al_frame,text = "List Documents",command = self.gui_also_likes_list)
        al_list_button.grid(column = 0, row = 1)

        al_graph_button = tk.Button(self.al_frame,text = "Plot Graph",command = self.gui_also_likes_graph)
        al_graph_button.grid(column = 0, row = 2)

    # Functions:
    # ==========
    def load_dataset(self):
        filename = filedialog.askopenfilename(title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))
        if not filename.endswith('.json'):
            messagebox.showinfo("Visualizer error", "Filetype must be a .json")
        else:
            self.dl.complete_load(filename)
            self.dv = DataVisualiser(self.dl.dicts)
            self.af = AffinityFinder(self.dl.dicts)
            self.gh = GraphHandler(self.dl.dicts)

    # DF FRAME FUNCTIONS
    def gui_plot_countries(self):
        self.dv.plot_countries()

    def gui_plot_continents(self):
        self.dv.plot_continents()

    def gui_plot_browsers_verbose(self):
        self.dv.plot_browsers_verbose()

    def gui_plot_browsers(self):
        self.dv.plot_browsers()

    def gui_also_likes_list(self):
        visitor_uuid = self.visitor_uuid_entry.get()
        document_uuid = self.document_uuid_entry.get()
        al_list = self.af.also_likes(document_uuid,visitor_uuid)
        for i,doc in enumerate(al_list):
            al_doc = tk.Label(self.al_frame,text = doc)
            al_doc.grid(column = 1, columnspan = 10,row = i+1)

    def gui_also_likes_graph(self):
        visitor_uuid = self.visitor_uuid_entry.get()
        document_uuid = self.document_uuid_entry.get()
        self.gh.create_graph(base_visitor_uuid=visitor_uuid,base_document_uuid=document_uuid)

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()

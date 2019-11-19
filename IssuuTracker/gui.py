'''
created on: 16/11/2019-12:48
by: QDucasse
'''

import tkinter as tk
from tkinter import filedialog

# ==============================================================================
# ========================== WINDOW GENERATION =================================

window = tk.Tk()
window.title("ISSUU Tracker")
window.geometry("650x500")

# ==============================================================================
# ========================= FRAMES DEFINITION ==================================

df_frame   = tk.Frame(window,padx = 3, pady = 10)
stat_frame = tk.Frame(window,padx = 3, pady = 10)
uuid_frame = tk.Frame(window,padx = 3, pady = 10)
al_frame   = tk.Frame(window,padx = 3, pady = 10)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

df_frame.grid(row = 0)
stat_frame.grid(row = 1)
uuid_frame.grid(row = 2)
al_frame.grid(row = 3)

# ==============================================================================
# =========================== DATASET FRAME ====================================

# Functions:
# ==========
def load_dataset():
    filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))

# Components:
# ===========
label_df = tk.Label(df_frame,text = "Dataset")
label_df.grid(column = 0, columnspan = 10,row = 0)

load_dataset_button = tk.Button(df_frame,text = "Choose Dataset",command = load_dataset)
load_dataset_button.grid(column = 0, row = 1)

# ==============================================================================
# ============================= STATS FRAME ====================================
# Functions:
# ==========
def gui_plot_countries():
    pass

def gui_plot_continents():
    pass

def gui_plot_browsers_verbose():
    pass

def gui_plot_browsers():
    pass
# Components:
# ===========
label_stat = tk.Label(stat_frame,text = "Statistical visualisations")
label_stat.grid(column = 0, columnspan = 10,row = 0)

plot_countries_button = tk.Button(stat_frame,text = "Plot Countries",command = gui_plot_countries)
plot_countries_button.grid(column = 0, row = 1)

plot_continents_button = tk.Button(stat_frame,text = "Plot Continents",command = gui_plot_continents)
plot_continents_button.grid(column = 1, row = 1)

plot_browsers_verbose_button = tk.Button(stat_frame,text = "Plot Browsers (Verbose)",command = gui_plot_browsers_verbose)
plot_browsers_verbose_button.grid(column = 2, row = 1)

plot_browsers_button = tk.Button(stat_frame,text = "Plot Browsers",command = gui_plot_browsers)
plot_browsers_button.grid(column = 3, row = 1)

# ==============================================================================
# ============================== UUID FRAME ====================================
# Functions:
# ==========

# Components:
# ===========
label_uuid = tk.Label(uuid_frame,text = "UUIDs")
label_uuid.grid(column = 0, columnspan = 10,row = 0)

visitor_uuid_label = tk.Label(uuid_frame,text = "Visitor UUID: ")
visitor_uuid_label.grid(column = 1, row = 2)
visitor_uuid_entry = tk.Entry(uuid_frame)
#visitor_uuid_entry.insert("end","")
visitor_uuid_entry.grid(column = 2, row = 2)

document_uuid_label = tk.Label(uuid_frame,text = "Document UUID: ")
document_uuid_label.grid(column = 1, row = 3)
document_uuid_entry = tk.Entry(uuid_frame)
#document_uuid_entry.insert("end","")
document_uuid_entry.grid(column = 2, row = 3)

# ==============================================================================
# ========================= 'ALSO LIKES' FRAME =================================
# Functions:
# ==========
def gui_also_likes_list():
    pass

def gui_also_likes_graph():
    pass
# Components:
# ===========
al_uuid = tk.Label(al_frame,text = "Also Likes")
al_uuid.grid(column = 0, columnspan = 10,row = 0)

al_list_button = tk.Button(al_frame,text = "List Documents",command = gui_also_likes_list)
al_list_button.grid(column = 0, row = 1)

al_list_text = tk.Text(al_frame,height=2, width=30)
al_list_text.grid(column = 1, row = 1)

al_graph_button = tk.Button(al_frame,text = "Plot Graph",command = gui_also_likes_graph)
al_graph_button.grid(column = 0, row = 2)


window.mainloop()

'''
created on: 18/11/2019 14:58
by: QDucasse
'''
import argparse

from IssuuTracker.data_loader     import DataLoader
from IssuuTracker.data_visualiser import DataVisualiser
from IssuuTracker.affinity_finder import AffinityFinder
from IssuuTracker.graph_handler   import GraphHandler
from IssuuTracker.gui             import GUI

def main():
    # COMPONENTS CREATION
    # ===================
    dl = DataLoader()

    # ARGUMENTS PARSING
    # =================
    parser = argparse.ArgumentParser(description='ISSUU Tracker')
    parser.add_argument("-u","--user_uuid", help = "UUID of the user")
    parser.add_argument("-d","--doc_uuid",  help = "UUID of the document")
    parser.add_argument("-t","--task_id",   help = "ID of the task (2a,2b,3a,3b,4d,5,6)")
    parser.add_argument("-f","--file_name", help = "JSON file of the dataset")
    args = parser.parse_args()

    if args.task_id == "2a":
        dl.complete_load(args.file_name)
        dv = DataVisualiser(dl.dicts)
        dv.plot_countries()

    elif args.task_id == "2b":
        dl.complete_load(args.file_name)
        dv = DataVisualiser(dl.dicts)
        dv.plot_continents()

    elif args.task_id == "3a":
        dl.complete_load(args.file_name)
        dv = DataVisualiser(dl.dicts)
        dv.plot_browsers_verbose()

    elif args.task_id == "3b":
        dl.complete_load(args.file_name)
        dv = DataVisualiser(dl.dicts)
        dv.plot_browsers()

    elif args.task_id == "4d":
        dl.load_dataset_from(args.file_name)
        af = AffinityFinder(dl.dicts)
        print(af.also_likes_list(args.doc_uuid))

    elif args.task_id == "5":
        dl.load_dataset_from(args.file_name)
        gh = GraphHandler(dl.dicts,args.user_uuid,args.doc_uuid)
        graph = gh.create_graph()

    elif args.task_id == "6":
        gui = GUI()
        gui.mainloop()


if __name__ == "__main__":
    main()

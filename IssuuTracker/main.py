'''
created on: 18/11/2019 14:58
by: QDucasse
'''
import argparse
#from gui           import *
from loader        import *
from graph_handler import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ISSUU Tracker')
    parser.add_argument("-u","--user_uuid", help = "UUID of the user")
    parser.add_argument("-d","--doc_uuid",  help = "UUID of the document")
    parser.add_argument("-t","--task_id",   help = "ID of the task (2a,2b,3a,3b,4d,5,6)")
    parser.add_argument("-f","--file_name", help = "JSON file of the dataset")
    args = parser.parse_args()

    if args.task_id == "2a":
        df = load_dataset_json(args.file_name)
        plot_countries(df)

    elif args.task_id == "2b":
        df = load_dataset_json(args.file_name)
        plot_continents(df)

    elif args.task_id == "3a":
        df = load_dataset_json(args.file_name)
        plot_browsers_verbose(df)

    elif args.task_id == "3b":
        df = load_dataset_json(args.file_name)
        plot_browsers(df)

    elif args.task_id == "4d":
        df = load_dataset_json(args.file_name)
        print(also_likes(df,args.doc_uuid,sort_func=sort_count_docs))

    elif args.task_id == "5":
        df = load_dataset_json(args.file_name)
        graph = create_graph(df,args.user_uuid,args.doc_uuid)

    elif args.task_id == "6":
        pass

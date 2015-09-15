import pandas as pd
from pandas import DataFrame
import numpy as np
from collections import Counter
import random

class SecretSanta(object):

    def __init__(self, file_name):
        """reads in csv file"""
        self.file_name = file_name

    def open_file(self):
        """ reads file and prints out results"""
        self.open_file = pd.read_csv(self.file_name, sep=',',header=None)
        self.full_names(self.open_file)

    def full_names(self, files):
        first_names = np.array(files[0])
        last_names = np.array(files[1])
        concat = DataFrame({"first": first_names, "last": last_names})
        names = np.array(concat["first"] + " " + concat["last"])
        self.master_list(names, last_names)

    def master_list(self, names, last_names):
        emails = np.array(self.open_file[2])
        master_list = zip(names, last_names, emails)
        self.delete_dups(master_list)

    def delete_dups(self, lists):
        master_nodups = []
        for i in lists:
            if i not in master_nodups:
                master_nodups.append(i)
        self.last_names_from_nondups(master_nodups)

    def last_names_from_nondups(self, nodups):
        new_last_names = []
        for i in nodups:
            new_last_names.append(i[1])
        self.dup_last_names(new_last_names, nodups)

    def dup_last_names(self, names, lists):
        dup_names = []
        my_dict = dict(Counter(names))
        for key, value in my_dict.iteritems():
            if value > 1:
                dup_names.append(key)
        self.move_to_groups(dup_names, lists)

    def move_to_groups(self, dups, master):
        same_surname = []
        diff_surname = []
        for i in master:
            for x in dups:
                if i[1] == x:
                    same_surname.append(i)
                else:
                    diff_surname.append(i)
        self.remove_tuple(same_surname, diff_surname)

    def remove_tuple(self, same, diff):
        same_name = []
        diff_name = []
        for i in same:
            same_name.append([i[0],i[2]])
        for i in diff:
            diff_name.append([i[0],i[2]])
        self.match_users(same_name, diff_name )

    def match_users(self, same, diff):
        x=0
        output = []
        for i in same:
            output.append([i,diff[x]])
            x+=1
        print output

x = SecretSanta("santalist.csv")
x.open_file()




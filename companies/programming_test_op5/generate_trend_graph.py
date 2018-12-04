import os
import sys
import random
import argparse

import numpy
import pandas as pd
import matplotlib.pyplot as plt


class GenerateTrendGraph(object):

    def __init__(self):

        self.parser = argparse.ArgumentParser()
        # Take the file as input
        self.parser.add_argument(
            'start_date', type=int, nargs='?',
            help='Pass the start date')
        self.parser.add_argument(
            'end_date', type=int, nargs='?',
            help='Pass the end date')
        self.parser.add_argument(
            'input_file', nargs='?', type=argparse.FileType('r'),
            help='Pass Input File As Command Line Argument')
        self.parser.add_argument(
            'ouput_file', nargs='?', type=argparse.FileType('w'),
            help='Pass Output File As Command Line Argument')
        if self.parser:
            self.data = self.parser.parse_args()
        else:
            print "Send the File As Command Line Argument"

    def is_check(self, name):
        if not name:
            print "Pass the correct input data."
            sys.exit(-1)

    def check_input_data(self):
        if not self.data:
            print "No value's is passed."

        self.is_check(self.data.start_date)
        self.is_check(self.data.end_date)
        self.is_check(self.data.input_file.name if self.data.input_file else None)
        self.is_check(self.data.ouput_file.name if self.data.ouput_file else None)
        # start_date = pd.to_datetime(''.format(self.data.start_date), unit='s')
        # end_date = pd.to_datetime(''.format(self.data.end_date), unit='s')
        sorted_dict = self.get_data_from_input_file(
            self.data.input_file.name,
            self.data.start_date,
            self.data.end_date
        )

        # plot the graph
        self.plot_graph(sorted_dict, self.data.ouput_file.name)

    def get_data_from_input_file(self, input_file_name, start_date, end_date):
        start_index, end_index, sorted_dict = None, None, None

        if os.path.isfile(input_file_name):
            data_frame = pd.read_csv(
                'testdata_small.txt', sep=" ",
                header=None, names=["days", "boolean_value"])

            file_data_in_dict = dict(zip(data_frame.days, data_frame.boolean_value))
            keys = sorted(file_data_in_dict.keys())
            if start_date in keys and end_date in keys:
                start_index = keys.index(start_date)
                end_index = keys.index(end_date)

                sorted_dict = dict(list(file_data_in_dict.items())[start_index:end_index])
        else:
            print "File: {} you sent is not exists in the path.".format(input_file_name)
            sys.exit(-1)

        return sorted_dict

    def get_random_list(self, dict_length):
        return [random.randint(1, 11)*dict_length for i in range(dict_length)]

    def plot_graph(self, sorted_dict, ouput_file_name):
        fig = plt.figure(figsize=[6.95,0.7])
        ax = fig.add_subplot(111)
        dict_length = len(sorted_dict)
        
        # x values
        x_values = self.get_random_list(dict_length)
        x_values.sort()

        # x rect values
        rect_x_values = [random.randint(1, 10)*1 for i in range(dict_length)]
        rect_x_values.sort()

        for index, key_value in enumerate(sorted_dict.items()):
            if key_value[1] and index == 0:
                rect1 = plt.Rectangle((0, 0), rect_x_values[index], 50, fc='green')
                ax.add_patch(rect1)
            else:
                if index == 0:
                    rect1 = plt.Rectangle((0, 0), rect_x_values[index], 50, fc='red')
                    ax.add_patch(rect1)

            if key_value[1] and index > 0:
                rect1 = plt.Rectangle((x_values[index], 0), rect_x_values[index], 50, fc='green')
                ax.add_patch(rect1)
            else:
                rect1 = plt.Rectangle((x_values[index], 0), rect_x_values[index], 50, fc='red')
                ax.add_patch(rect1)
        
        ax.set_xlim(0, 10*dict_length)
        ax.set_aspect('equal')
        plt.savefig('{}'.format(ouput_file_name), format='svg')


if __name__ == "__main__":
    GenerateTrendGraph().check_input_data()

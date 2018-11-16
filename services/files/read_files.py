class PlotValue:
    def __init__(self, id, number):
        self.id = id
        self.number = number


def read_plot_values_file():
    plot_values = open("sampleData/plot_values.txt", "r").read().splitlines()
    plot_value_array = []
    split_plot_value_array = []

    for i in plot_values:
        split_plot_value_array.append((i.split('\t', 1)))

    for i in split_plot_value_array:
        plot_value_array.append(PlotValue(i[0], i[1]))

    return plot_value_array


def read_time_traces_file():
    time_traces_file_data = open("sampleData/time_traces.txt", "r")
    rows = (row.strip().split() for row in time_traces_file_data)
    time_traces = zip(*(row for row in rows if row))
    time_traces_file_data.close()
    return time_traces
import pandas as pd
import os

class Data:
    def __init__(self, data_path, city):
        lines_file = os.path.join(data_path, city + '.lines.csv')
        stations_file = os.path.join(data_path, city + '.stations.csv')
        connections_file = os.path.join(data_path, city + '.connections.csv')

        self.lines = pd.read_csv(lines_file, index_col=0)
        self.stations = pd.read_csv(stations_file, index_col=0)
        self.connections = pd.read_csv(connections_file)

        # print(self.lines)
        # print(self.stations)
        # print(self.connections)

if __name__ == '__main__':
    data_path = 'data'
    city = 'london'
    tube_data = Data(data_path, city)
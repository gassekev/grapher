import sys
import os.path
import fileHandler

if __name__ == '__main__':
    print('Python version is: ' + sys.version)
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file_path = os.path.join(dir_path, 'data.txt')
    graph_path = os.path.join(dir_path, 'graphs')

    data = fileHandler.getDataFromFile(file_path)
    print(data)

    exit(0)

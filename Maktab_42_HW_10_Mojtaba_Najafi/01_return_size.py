import os
from functools import reduce


def size_of_files(path, itemlen=5):
    """takes a path as a argument and item length and prints the file size(s) in Bytes(s) """

    try:
        for file_name in os.listdir(path):

            full_path = os.path.join(path, file_name)
            if len(os.path.splitext(file_name)[0]) > itemlen and os.path.isfile(full_path):
                print(file_name, f' {os.path.getsize(full_path)} Byte(s)')
            else:
                print('No files found')
    except OSError as error:
        print(error)


dir = '/Users/moshnar/PycharmProjects/MaktabSharif/date_time'


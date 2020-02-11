import json
import os
from datetime import date
import json
import glob


def encode(vars, results, config, path='C:\\File_Manager_Test', name='None'):
    if not os.path.exists(path):
        os.makedirs(path)

    # TODO: Change this to not matter if path ends with \\ or not, and work for linux /
    if not os.path.exists(path + "\\" + name):
        os.makedirs(path + "\\" + name)

    if not os.path.exists(path + "\\" + name + "\\" + str(date.today())):
        os.makedirs(path + "\\" + name + "\\" + str(date.today()))

    if not len(results) == len(vars):
        raise Exception(
            "the amout of measurement can't be different from the amount of times you measured...")

    total_path = path + "\\" + name + "\\" + \
        str(date.today())
    count_files = len(glob.glob(total_path + "\\*")) + 1
    # print(count_files)
    total_path = total_path + "\\" + str(count_files) + ".data"
    # print(total_path)
    sav = []
    sav.append(vars)
    sav.append(results)
    sav.append(config)

    # print(sav)
    with open(total_path, 'w') as filehandle:
        json.dump(sav, filehandle)
    decode(total_path)


# TODO: The decode should be able to make back what was each variable and result from the config
def decode(path):
    # open output file for reading
    with open(path, 'r') as filehandle:
        basicList = json.load(filehandle)
    print(basicList)


encode([(1, 1), (0, 0)], [0, 2], {0: "devices and stuff"})

# define list of places

# define list with values
# places = [(0, 0), (1, 1), 0, 2]
# # basicList = [1, "Cape Town", 4.6]

# # open output file for writing
# with open('C:\\File_Manager_Test\\listfile.txt', 'w') as filehandle:
#     json.dump(places, filehandle)

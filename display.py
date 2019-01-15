def main_menu():
    print('MAIN MENU:')
    print("1: view all imported albums")
    print("2: find all albums by genre")
    print("3: find all albums from given time range")
    print("4: find shortest/longest album")
    print("5: find all albums created by given artist")
    print("6: find album by title")
    print("7: collection statistics")
    print("8: add new album")
    print("9: edit entry")
    print("0: exit")
    print('\n')


def table(albums_list):
    i = 1
    for item in albums_list:
        print("{:3}. {:14s} | {:25s} | {:4} | {:20s} | {:6s} |" .format(i, item[0], item[1], item[2], item[3], item[4]))
        i += 1


def tabe(dictionary):
        for key in dictionary:
                print("{},{}".format(key,dictionary[key]))

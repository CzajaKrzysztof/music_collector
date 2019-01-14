def main_menu():
    print("1: do you want to view all imported albums")
    print("2: do you want to find all albums by genre")
    print("3: do you want to find all albums from given time range")
    print("4: do you want to find shortest/longest album")
    print("5: do you want to find all albums created by given artist")
    print("6: do you want to find album by album name")
    print("7: do you want to get full report in form of set of given statistics")
    print("8: exit")
    print('\n')


def table(albums_list):
    
    for item in albums_list:
        print(":",item[0]," "*(15-len(item[0])),
        item[1]," "*(18-len(item[1])),
        item[2]," "*4,
        item[3]," "*(18-len(item[3])),
        item[4]," "*(13-len(item[4])),)

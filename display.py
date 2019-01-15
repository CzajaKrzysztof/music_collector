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
    print("9: exit")
    print('\n')


def table(albums_list):
    
    for item in albums_list:
        print(":",item[0]," "*(15-len(item[0])),
        item[1]," "*(18-len(item[1])),
        item[2]," "*4,
        item[3]," "*(18-len(item[3])),
        item[4]," "*(13-len(item[4])),)

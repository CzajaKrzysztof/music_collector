def import_data_from_file(filename='text_albums_data.txt'):
    content = []
    with open(filename, 'r') as my_file:
        for line in my_file:
            content.append(line.rstrip('\n').split(','))

    return content


def find_albums_by_condition(albums_list, condition, index):
    filtered_albums = []
    for album in albums_list:
        if condition in album[index]:
            filtered_albums.append(album)

    return filtered_albums


def temp_print(list):
    for i in list:
        print(i)

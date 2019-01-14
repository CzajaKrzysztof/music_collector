def import_data_from_file(filename='text_albums_data.txt'):
    albums_dictionary = {}
    content = []
    key = 1
    with open(filename, 'r') as my_file:
        for line in my_file:
            content.append(line.rstrip('\n').split(','))

    return content

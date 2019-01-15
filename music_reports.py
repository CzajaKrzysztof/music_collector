from datetime import datetime


def import_data_from_file(filename='text_albums_data.txt'):
    content = []
    with open(filename, 'r') as my_file:
        for line in my_file:
            line = line.rstrip('\n').split(',')
            line[2] = int(line[2])
            content.append(line)

    return content


def find_albums_by_literal_condition(albums_list, condition, index):
    filtered_albums = []
    for album in albums_list:
        condition = condition.lower().replace(' ', '')
        genre_in_list = album[index]
        genre_in_list = genre_in_list.lower().replace(' ', '')
        if list(condition) == list(genre_in_list):
            filtered_albums.append(album)

    return filtered_albums


def find_albums_by_condition(albums_list, condition, index):
    filtered_albums = []
    for album in albums_list:
        if condition.lower() in album[index].lower():
            filtered_albums.append(album)

    return filtered_albums


def albums_from_given_time_range(albums_list, time_start, time_end):
    filtered_albums = []
    for album in albums_list:
        if album[2] >= time_start and album[2] <= time_end:
            filtered_albums.append(album)

    return filtered_albums


def max_min_time(albums_list):
    temp_list = []
    result_list = []
    for album in albums_list:
        time_in_sec = album[4].split(':')
        time_in_sec[0] = int(time_in_sec[0]) * 60
        time_in_sec[1] = int(time_in_sec[1])
        time_in_sec = sum(time_in_sec)
        album.append(time_in_sec)
        temp_list.append(album)

    temp_list = list(sorted(temp_list, key=lambda x: x[5]))
    result_list.append(temp_list[0][:-1])
    result_list.append(temp_list[-1][:-1])

    return result_list


def get_young_old_album(albums_list):
    result_list = []
    temp_list = list(sorted(albums_list, key=lambda x: x[2]))

    result_list.append(temp_list[1])
    result_list.append(temp_list[-1])

    return result_list


def get_albums_count_by_given_genres(albums_list):
    genres_set = set()
    result_dict = {}
    for album in albums_list:
        genres_set.add(album[3])

    for genre in genres_set:
        temp_list = find_albums_by_literal_condition(albums_list, genre, 3)
        result_dict[genre] = len(temp_list)

    return result_dict


def get_unique_propositions(albums_list, album_list_by):
    if len(album_list_by) != 0:
        chosen_genre = album_list_by[0][3]
        albums_by_genre = find_albums_by_condition(albums_list, chosen_genre, 3)
        unique_set_one = set()
        unique_set_two = set()
        for element in album_list_by:
            unique_set_one.add(tuple(element))
        for element in albums_by_genre:
            unique_set_two.add(tuple(element))
        unique_set_with_propositions = (unique_set_two - unique_set_one)
        return unique_set_with_propositions


def get_user_string_input(question):
    result = input(question)

    return result


def get_user_int_input(question):
    while True:
        try:
            result = int(input(question))
        except ValueError:
            print('Please enter only numbers')
            continue
        else:
            return result


def get_new_album_data_from_user():
    new_album_data = []
    new_album_data.append(get_user_string_input('Enter artist name: '))
    new_album_data.append(get_user_string_input('Enter album title: '))
    new_album_data.append(get_user_int_input('Enter album release year: '))
    new_album_data.append(get_user_string_input('Enter album genre: '))
    new_album_data.append(get_user_string_input('Enter album length minutes:seconds: '))

    return new_album_data


def add_new_album(albums_list, new_album_list):
    print('New album data:')
    print('Artist: {0}, album title: {1}, release year: {2}, genre: {3}, length: {4}'.format(*new_album_list))
    reply = input('Are you sure? (y/n): ')
    if reply == 'y':
        albums_list.append(new_album_list)
        # export_new_album_to_file(albums_list)


def get_user_action():
    while True:
        try:
            user_action = int(input('\nWhat do you want to do: '))
        except ValueError:
            print('Please chose from options 1 to 8')
            continue
        else:
            return user_action


def get_dates_to_filter():
    while True:
        try:
            time_start = int(input('Enter start date: '))
        except ValueError:
            print('\nPlease enter intiger.')
            continue
        else:
            break

    while True:
        try:
            time_ent = int(input('Enter end date: '))
        except ValueError:
            print('\nPlease enter intiger.')
            continue
        else:
            break

    return time_start, time_ent

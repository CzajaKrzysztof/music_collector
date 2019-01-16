import display
import os


def import_data_from_file(filename='text_albums_data.txt'):
    content = []
    with open(filename, 'r') as my_file:
        for line in my_file:
            line = line.rstrip('\n').split(',')
            line[2] = int(line[2])
            content.append(line)

    content = sort_list_by_column(content, 0)
    return content


def sort_list_by_column(list_to_sort, colum_index):
    list_to_sort = list(sorted(list_to_sort, key=lambda x: x[colum_index]))

    return list_to_sort


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
    result = input('\n' + question)

    return result


def get_user_album_length_input(question):
    while True:
        try:
            result = input('\n' + question)
            if ':' not in result:
                raise ValueError
            result_list = result.split(':')
            if len(result_list) != 2:
                raise ValueError
            result_list[0] = int(result_list[0])
            result_list[1] = int(result_list[1])
            break
        except (ValueError, NameError, SyntaxError):
            print('Album length must be in format minutes:secundes!')
    print(result)
    return result


def ask_user_for_new_length_input(length_to_edit, question):
    while True:
        try:
            print('If you want to leave "{}" hit enter.'.format(length_to_edit))
            result = input('\n' + question)
            if result == '':
                result = length_to_edit
                break
            if ':' not in result:
                raise ValueError
            result_list = result.split(':')
            if len(result_list) != 2:
                raise ValueError
            result_list[0] = int(result_list[0])
            result_list[1] = int(result_list[1])
            break
        except (ValueError, NameError, SyntaxError):
            print('Album length must be in format minutes:secundes!')
    print(result)
    return result


def get_user_int_input(question):
    while True:
        try:
            result = int(input('\n' + question))
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
    new_album_data.append(get_user_album_length_input('Enter album length minutes:seconds: '))

    return new_album_data


def export_new_album_to_file(new_album_list):
    with open('text_albums_data.txt', 'a') as my_file:
        new_album_list[2] = str(new_album_list[2])
        new_album_string = '\n' + ','.join(new_album_list)
        my_file.write(new_album_string)


def add_new_album(albums_list, new_album_list):
    os.system('clear')
    display.main_menu()
    print('New album data:')
    display.show_single_album(new_album_list)
    reply = input('Are you sure? (y/n): ')
    if reply == 'y':
        albums_list.append(new_album_list)
        export_new_album_to_file(new_album_list)


def ask_user_for_new_string(str_to_edit, question):
    print('If you want to leave "{}" hit enter.'.format(str_to_edit))
    new_string = input(question)
    if new_string == '':
        new_string = str_to_edit

    return new_string


def ask_user_for_new_int(int_to_edit, question):
    print('If you want to leave "{}" hit enter.'.format(int_to_edit))
    while True:
        new_int = input(question)

        if new_int == '':
            new_int = int_to_edit
            return new_int
        elif new_int != '':
            try:
                new_int = eval(new_int)
            except (ValueError, NameError, SyntaxError):
                print('Entry need to be a number.')
                continue
            else:
                return new_int


def edit_album_entry(albums_list, album_index_to_edit):
    album_to_edit = albums_list.pop(album_index_to_edit - 1)
    os.system('clear')
    display.main_menu()
    album_to_edit[0] = ask_user_for_new_string(album_to_edit[0], 'Enter new artist name: ')
    os.system('clear')
    display.main_menu()
    album_to_edit[1] = ask_user_for_new_string(album_to_edit[1], 'Enter new album title: ')
    os.system('clear')
    display.main_menu()
    album_to_edit[2] = ask_user_for_new_int(album_to_edit[2], 'Enter new album year: ')
    os.system('clear')
    display.main_menu()
    album_to_edit[3] = ask_user_for_new_string(album_to_edit[3], 'Enter new album genre: ')
    os.system('clear')
    display.main_menu()
    album_to_edit[4] = ask_user_for_new_length_input(album_to_edit[4], 'Enter album length minutes:seconds: ')
    albums_list.append(album_to_edit)

    return albums_list


def export_list_to_file(albums_list, filename='text_albums_data.txt'):
    with open(filename, 'w') as my_file:
        for album in albums_list:
            album[2] = str(album[2])
            album_index = albums_list.index(album)
            if album_index == (len(albums_list) - 1):
                album_string = ','.join(album)
                my_file.write(album_string)
            else:
                album_string = ','.join(album) + '\n'
                my_file.write(album_string)


def get_max_column_length(album_list, colum_index):
    max_length = 0
    for element in album_list:
        current_length = len(str(element[colum_index]))
        if current_length > max_length:
            max_length = current_length

    return max_length


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

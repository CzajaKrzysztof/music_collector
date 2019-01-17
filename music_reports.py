import display
import os


def import_data_from_file(filename='text_albums_data.txt'):
    """
    Import data form text file. Default file name is text_albums_data.txt. Function return list of albums with 2nd
    index converted to in. Returning list is sorted by first elemtn whch is artist name.
    """
    content = []
    with open(filename, 'r') as my_file:
        for line in my_file:
            line = line.rstrip('\n').split(',')
            line[2] = int(line[2])
            content.append(line)

    content = sort_list_by_column(content, 0)
    return content


def sort_list_by_column(list_to_sort, colum_index):
    """
    Function sort given list in parametre list_to_sort by index given in parametre column_index.
    Function return sorted list.
    """
    list_to_sort = list(sorted(list_to_sort, key=lambda x: x[colum_index]))

    return list_to_sort


def find_albums_by_literal_condition(albums_list, condition, index):
    """
    Function search for albums that contains exacly condition at given index in list in parametre albums_list.
    Compered values ale lowercased and turned into lists. Function returns list of albums.
    """
    filtered_albums = []
    for album in albums_list:
        condition = condition.lower().replace(' ', '')
        genre_in_list = album[index]
        genre_in_list = genre_in_list.lower().replace(' ', '')
        if list(condition) == list(genre_in_list):
            filtered_albums.append(album)

    return filtered_albums


def find_albums_by_condition(albums_list, condition, index):
    """
    Function search for albums that contains condition at given index in list in parametre albums_list.
    Compered values ale lowercased. Function returns list of albums.
    """
    filtered_albums = []
    for album in albums_list:
        if condition.lower() in album[index].lower():
            filtered_albums.append(album)

    return filtered_albums


def albums_from_given_time_range(albums_list, time_start, time_end):
    """
    Function search for albums in albums_list that release date at
    index 2 is between years in parametres time_start and time_end.
    """
    filtered_albums = []
    for album in albums_list:
        if album[2] >= time_start and album[2] <= time_end:
            filtered_albums.append(album)

    return filtered_albums


def max_min_time(albums_list):
    """
    Function converts string value at index 4 from form:'mm:ss' to sectond as intiger and append to evenry entry in
    list of albums. Next list is sorted by length album represented by sectond. First and last entry is added to enpty
    list which is returned.
    """
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
    """
    Function sorts list of albums by relese year at index 2 and append to eplty list.
    New list containt youngest and oldest album and is returned from function.
    """
    result_list = []
    temp_list = list(sorted(albums_list, key=lambda x: x[2]))

    result_list.append(temp_list[1])
    result_list.append(temp_list[-1])

    return result_list


def get_albums_count_by_given_genres(albums_list):
    """ Function return dictionary containing genre names and albums count for every given genre. """
    genres_set = set()
    result_dict = {}
    for album in albums_list:
        genres_set.add(album[3])

    for genre in genres_set:
        temp_list = find_albums_by_literal_condition(albums_list, genre, 3)
        result_dict[genre] = len(temp_list)

    return result_dict


def get_unique_propositions(albums_list, album_list_by):
    """
    Function return set of unique albums as propositin for user. Function converts 
    lists of list: album_list, album_list_by to sets of tuples and return only unique 
    albums in albums list by genre minus albums finded for user.
    """
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
    """ Function return user input as string. """
    result = input('\n' + question)

    return result


def get_user_album_length_input(question):
    """ Function return album length to use in add new album function. Function fool-prools user entry. """
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

            if result_list[1] < 0 or result_list[1] > 60:
                raise ReferenceError
            if result_list[0] < 0:
                raise ReferenceError
            break
        except (ValueError, NameError, SyntaxError):
            print('Album length must be in format minutes:secundes!')
        except ReferenceError:
            print('Minutes can`t be less then 0. Seconds can`t be less then 0 and more then 60')

    return result


def ask_user_for_new_length_input(length_to_edit, question):
    """ Function return album length to use in edit album function. Function fool-prools user entry. """
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

            if result_list[1] < 0 or result_list[1] > 60:
                raise ReferenceError
            if result_list[0] < 0:
                raise ReferenceError
            break
        except (ValueError, NameError, SyntaxError):
            print('Album length must be in format minutes:secundes!')
        except ReferenceError:
            print('Minutes can`t be less then 0. Seconds can`t be less then 0 and more then 60')
    print(result)
    return result


def get_user_int_input(question):
    """ Function return user intiger input after fool-proofing. """
    while True:
        try:
            result = int(input('\n' + question))
        except ValueError:
            print('Please enter only numbers')
            continue
        else:
            return result


def get_user_index_input(question, albums_list):
    """ Function return intiger value after fool-proofing to use as base for index in editing albums function. """
    while True:
        try:
            result = int(input('\n' + question))
            if result == 0 or result > len(albums_list):
                raise NameError
        except ValueError:
            print('Please enter only numbers')
            continue
        except NameError:
            print('Only values between 0 and {} ale permitted'.format(len(albums_list)))
            continue
        else:
            return result


def get_new_album_data_from_user():
    """ Grouping function for geting values from user of new album data. """
    new_album_data = []
    new_album_data.append(get_user_string_input('Enter artist name: '))
    new_album_data.append(get_user_string_input('Enter album title: '))
    new_album_data.append(get_user_int_input('Enter album release year: '))
    new_album_data.append(get_user_string_input('Enter album genre: '))
    new_album_data.append(get_user_album_length_input('Enter album length minutes:seconds: '))

    return new_album_data


def export_new_album_to_file(new_album_list):
    """ Function append data of new album to database file. """
    with open('text_albums_data.txt', 'a') as my_file:
        new_album_list[2] = str(new_album_list[2])
        new_album_string = '\n' + ','.join(new_album_list)
        my_file.write(new_album_string)


def add_new_album(albums_list, new_album_list):
    """
    Function asks user if is sure to add new album and if 'yes' add new album data to albums 
    list user across music_collector application and calls for appending to database file function.
    """
    os.system('clear')
    display.main_menu()
    print('New album data:')
    display.show_single_album(new_album_list)
    
    while True:
        reply = input('Are you sure? (y/n): ')
        if reply in ['y', 'n', 'Y', 'N']:
            break

    if reply == 'y' or reply == 'Y':
        albums_list.append(new_album_list)
        export_new_album_to_file(new_album_list)


def ask_user_for_new_string(str_to_edit, question):
    """ Function asks user to provide new string value for editing function. If pressed enter old value is returned. """
    print('If you want to leave "{}" hit enter.'.format(str_to_edit))
    new_string = input(question)
    if new_string == '':
        new_string = str_to_edit

    return new_string


def ask_user_for_new_int(int_to_edit, question):
    """
    Function asks user to provide new intiger value for editing function. After
    fool-proofing new value is returned. If pressed enter old value is returned. 
    """
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
    """ Grouping function for getting data from user for new album """
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
    """ Function exports working in memory list of albums: albums_list to database text file."""
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
    """ Function return maximum length of value in form of string. """
    max_length = 0
    for element in album_list:
        current_length = len(str(element[colum_index]))
        if current_length > max_length:
            max_length = current_length

    return max_length


def get_user_action():
    """ Function return after fool-proofing intiger value which is action in main manu."""
    while True:
        try:
            user_action = int(input('\nWhat do you want to do: '))
            if user_action < 0 or user_action > 9:
                raise ValueError
            return user_action
        except ValueError:
            print('Please chose from options 0 to 9')



def get_dates_to_filter():
    """ Function return two user entered intiger values as yesrs for searching albums in given time period. """
    while True:
        try:
            time_start = int(input('Enter start date: '))
            time_end = int(input('Enter end date: '))
            if time_end < time_start:
                raise NameError
        except ValueError:
            print('\nPlease enter intiger.')
            continue
        except NameError:
            print('End date can`t be lowet then start date.')
            continue
        else:
            break

    return time_start, time_end

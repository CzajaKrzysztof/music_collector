from datetime import datetime


def import_data_from_file(filename='text_albums_data.txt'):
    content = []
    with open(filename, 'r') as my_file:
        for line in my_file:
            content.append(line.rstrip('\n').split(','))

    return content


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
    for i in albums_list:
        time_in_sec = i[4].split(':')
        time_in_sec[0] = int(time_in_sec[0]) * 60
        time_in_sec[1] = int(time_in_sec[1])
        time_in_sec = sum(time_in_sec)
        i.append(time_in_sec)
        temp_list.append(i)

    temp_list = list(sorted(temp_list, key=lambda x: x[5]))
    result_list.append(temp_list[0][:-1])
    result_list.append(temp_list[-1][:-1])

    return result_list


def get_user_action():
    user_action = int(input('What do you want to do: '))

    return user_action


def user_chosen_input(question):
    user_input = input('What music ganre you want to filter albums by: ')

    return user_input


def get_dates_to_filter():
    time_start = input('Enter start date: ')
    time_ent = input('Enter end date: ')

    return time_start, time_ent

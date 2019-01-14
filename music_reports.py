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


def albums_from_given_time_range(albums_list, time_start, time_end):
    filtered_albums = []
    for album in albums_list:
        if album[2] >= time_start and album[2] <= time_end:
            filtered_albums.append(album)

    return filtered_albums


def get_user_action():
    user_action = int(input('What do you want to do: '))

    return user_action


def user_chosen_genre():
    user_genre = input('What music ganre you want to filter albums by: ')

    return user_genre


def get_dates_to_filter():
    time_start = input('Enter start date: ')
    time_ent = input('Enter end date: ')

    return time_start, time_ent

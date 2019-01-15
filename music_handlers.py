import music_reports
import display
import os


def handle_view_all_albums(albums_list):
    os.system('clear')
    display.main_menu()
    display.table(albums_list)


def handle_find_albums_by_genre(albums_list):
    chosen_genre = music_reports.get_user_string_input('Enter music genre: ')
    albums_by_genre = music_reports.find_albums_by_condition(albums_list, chosen_genre, 3)
    os.system('clear')
    display.main_menu()
    display.table(albums_by_genre)


def handel_albums_in_time_range(albums_list):
    time = music_reports.get_dates_to_filter()
    os.system('clear')
    display.main_menu()
    albums_between_time = music_reports.albums_from_given_time_range(albums_list, *time)
    display.table(albums_between_time)


def handle_shortest_longest_albums(albums_list):
    max_min_list = music_reports.max_min_time(albums_list)
    os.system('clear')
    display.main_menu()
    display.table(max_min_list)


def handle_find_albums_by_artist(albums_list):
    chosen_artist = music_reports.get_user_string_input('Enter artist name: ')
    albums_by_artist = music_reports.find_albums_by_condition(albums_list, chosen_artist, 0)
    os.system('clear')
    display.main_menu()
    display.table(albums_by_artist)
    unique_set_with_propositions = music_reports.get_unique_propositions(albums_list, albums_by_artist)
    print('\nChosen for you:')
    display.table(unique_set_with_propositions)


def handle_find_albums_by_title(albums_list):
    chosen_album_title = music_reports.get_user_string_input('Enter album title: ')
    albums_by_album_title = music_reports.find_albums_by_condition(albums_list, chosen_album_title, 1)
    os.system('clear')
    display.main_menu()
    display.table(albums_by_album_title)
    unique_set_with_propositions = music_reports.get_unique_propositions(albums_list, albums_by_album_title)
    print('\nChosen for you:')
    display.table(unique_set_with_propositions)


def handle_show_statistics(albums_list):
    os.system('clear')
    display.main_menu()
    print('Albums statistics:\n')
    print('Shortest and longest albums:')
    longest_shortest_albums = music_reports.max_min_time(albums_list)
    display.table(longest_shortest_albums)
    print('\nYoungest and oldest albums:')
    youngest_oldest_albums = music_reports.get_young_old_album(albums_list)
    display.table(youngest_oldest_albums)
    print('\nAlbums count is: {}'.format(len(albums_list)))
    print('\nAlbums by given the genres')
    albums_count_by_given_genres = music_reports.get_albums_count_by_given_genres(albums_list)
    display.tabe(albums_count_by_given_genres)


def handle_adding_album(albums_list):
    os.system('clear')
    display.main_menu()
    new_album_list = music_reports.get_new_album_data_from_user()
    albums_list = music_reports.add_new_album(albums_list, new_album_list)


def handle_editing_entry(albums_list):
    os.system('clear')
    display.main_menu()
    display.table(albums_list)

import music_reports
import display
import os


def handle_view_all_albums(albums_list):
    os.system('clear')
    display.main_menu()
    albums_list = music_reports.sort_list_by_column(albums_list, 0)
    display.show_table(albums_list, 'All albums in collection')


def handle_find_albums_by_genre(albums_list):
    chosen_genre = music_reports.get_user_string_input('Enter music genre: ')
    albums_by_genre = music_reports.find_albums_by_condition(albums_list, chosen_genre, 3)
    os.system('clear')
    display.main_menu()
    display.show_table(albums_by_genre, 'Albums in ' + chosen_genre + ' genre')


def handel_albums_in_time_range(albums_list):
    time = music_reports.get_dates_to_filter()
    os.system('clear')
    display.main_menu()
    albums_between_time = music_reports.albums_from_given_time_range(albums_list, *time)
    display.show_table(albums_between_time, 'Albums between years ' + str(time[0]) + ' and ' + str(time[1]))


def handle_shortest_longest_albums(albums_list):
    max_min_list = music_reports.max_min_time(albums_list)
    os.system('clear')
    display.main_menu()
    display.show_table(max_min_list, 'Shortest and longest albums')


def handle_find_albums_by_artist(albums_list):
    chosen_artist = music_reports.get_user_string_input('Enter artist name: ')
    albums_by_artist = music_reports.find_albums_by_condition(albums_list, chosen_artist, 0)
    os.system('clear')
    display.main_menu()
    display.show_table(albums_by_artist, 'Albums by ' + chosen_artist)
    unique_set_with_propositions = music_reports.get_unique_propositions(albums_list, albums_by_artist)
    display.show_table(unique_set_with_propositions, 'Similar albums chosen for you')


def handle_find_albums_by_title(albums_list):
    chosen_album_title = music_reports.get_user_string_input('Enter album title: ')
    albums_by_album_title = music_reports.find_albums_by_condition(albums_list, chosen_album_title, 1)
    os.system('clear')
    display.main_menu()
    display.show_table(albums_by_album_title, 'Albums with title: ' + chosen_album_title)
    unique_set_with_propositions = music_reports.get_unique_propositions(albums_list, albums_by_album_title)
    display.show_table(unique_set_with_propositions, 'Similar albums chosen for you')


def handle_show_statistics(albums_list):
    os.system('clear')
    display.main_menu()
    print('Albums statistics:\n')
    print('Albums count is: {}'.format(len(albums_list)))
    longest_shortest_albums = music_reports.max_min_time(albums_list)
    display.show_table(longest_shortest_albums, 'Shortest and longest albums')
    youngest_oldest_albums = music_reports.get_young_old_album(albums_list)
    display.show_table(youngest_oldest_albums, 'Youngest and oldest albums')
    albums_count_by_given_genres = music_reports.get_albums_count_by_given_genres(albums_list)
    albums_count_by_given_genres_sorted = music_reports.sort_list_by_column(list(albums_count_by_given_genres.items()), 1)
    albums_count_by_given_genres_sorted.reverse()
    music_reports.show_dict_in_table(albums_count_by_given_genres_sorted)

    # display.show_table(albums_count_by_given_genres, 'Albums by given the genres') # TODO: zmienic na print dictionalry


def handle_adding_album(albums_list):
    os.system('clear')
    display.main_menu()
    new_album_list = music_reports.get_new_album_data_from_user()
    albums_list = music_reports.add_new_album(albums_list, new_album_list)
    os.system('clear')
    display.main_menu()


def handle_editing_entry(albums_list):
    os.system('clear')
    display.main_menu()
    albums_list = music_reports.sort_list_by_column(albums_list, 0)
    display.table(albums_list)
    album_index_to_edit = music_reports.get_user_int_input('Enter number of entry to edit: ')
    os.system('clear')
    display.main_menu()
    albums_list = music_reports.edit_album_entry(albums_list, album_index_to_edit)
    music_reports.export_list_to_file(albums_list)
    os.system('clear')
    display.main_menu()

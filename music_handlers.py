import music_reports
import display
import os


def handle_view_all_albums(albums_list):
    """ Handler for manu option to view all albums sorted in form of dynamic table. """
    music_reports.default_view()
    albums_list = music_reports.sort_list_by_column(albums_list, 0)
    display.show_table(albums_list, 'All albums in collection')


def handle_find_albums_by_genre(albums_list):
    """ Handler for manu option to search for albums with given by user genre. """
    music_reports.default_view()
    chosen_genre = music_reports.get_user_string_input('Enter music genre: ')
    albums_by_genre = music_reports.find_albums_by_condition(albums_list, chosen_genre, 3)
    music_reports.default_view()
    display.show_table(albums_by_genre, 'Albums in ' + chosen_genre + ' genre')


def handel_albums_in_time_range(albums_list):
    """ Handler for menu option to serach for albums between given by user years. """
    music_reports.default_view()
    time = music_reports.get_dates_to_filter()
    music_reports.default_view()
    albums_between_time = music_reports.albums_from_given_time_range(albums_list, *time)
    display.show_table(albums_between_time, 'Albums between years ' + str(time[0]) + ' and ' + str(time[1]))


def handle_shortest_longest_albums(albums_list):
    """ Handler for manu oprion to get shortest and longest albums in collection and display it as table."""
    music_reports.default_view()
    max_min_list = music_reports.max_min_time(albums_list)
    music_reports.default_view()
    display.show_table(max_min_list, 'Shortest and longest albums')


def handle_find_albums_by_artist(albums_list):
    """
    Handler for menu option to search albums by user given artist name and display it as table. Below search
    results handler displays table with albums with similar genre.
    """
    music_reports.default_view()
    chosen_artist = music_reports.get_user_string_input('Enter artist name: ')
    albums_by_artist = music_reports.find_albums_by_condition(albums_list, chosen_artist, 0)
    music_reports.default_view()
    display.show_table(albums_by_artist, 'Albums by ' + chosen_artist)
    unique_set_with_propositions = music_reports.get_unique_propositions(albums_list, albums_by_artist)
    display.show_table(unique_set_with_propositions, 'Similar albums chosen for you', 'yes')


def handle_find_albums_by_title(albums_list):
    """
    Handler for menu option to search albums by user given album title and display it as table. Below search
    results handler displays table with albums with similar genre.
    """
    music_reports.default_view()
    chosen_album_title = music_reports.get_user_string_input('Enter album title: ')
    albums_by_album_title = music_reports.find_albums_by_condition(albums_list, chosen_album_title, 1)
    music_reports.default_view()
    display.show_table(albums_by_album_title, 'Albums with title: ' + chosen_album_title)
    unique_set_with_propositions = music_reports.get_unique_propositions(albums_list, albums_by_album_title)
    display.show_table(unique_set_with_propositions, 'Similar albums chosen for you', 'yes')


def handle_show_statistics(albums_list):
    """ Handler for manu option to display satatistics regarding albums collection. """
    music_reports.default_view()
    print('Albums statistics:\n')
    print('Albums count is: {}'.format(len(albums_list)))
    longest_shortest_albums = music_reports.max_min_time(albums_list)
    display.show_table(longest_shortest_albums, 'Shortest and longest albums')
    youngest_oldest_albums = music_reports.get_young_old_album(albums_list)
    display.show_table(youngest_oldest_albums, 'Youngest and oldest albums')
    albums_count_by_given_genres = music_reports.get_albums_count_by_given_genres(albums_list)
    albums_count_by_given_genres_sorted = music_reports.sort_list_by_column(list(albums_count_by_given_genres.items()), 1)
    albums_count_by_given_genres_sorted.reverse()
    display.show_dict_in_table(albums_count_by_given_genres_sorted, 'Album counts in genres')


def handle_adding_album(albums_list):
    """
    Handler for manu option to add new album with user given data. After accepting data by user new  entry is added
    to albums list and text file with albums data is updated.
    """
    music_reports.default_view()
    new_album_list = music_reports.get_new_album_data_from_user()
    albums_list = music_reports.add_new_album(albums_list, new_album_list)
    music_reports.default_view()


def handle_editing_entry(albums_list):
    """
    Handler for menu option to pick and edit entry from albums collection. After editing, entry is added to albums
    list and text file with albums data is updated.
    """
    music_reports.default_view()
    albums_list = music_reports.sort_list_by_column(albums_list, 0)
    display.show_table(albums_list, 'All albums in collection')
    album_index_to_edit = music_reports.get_user_index_input('Enter number of entry to edit: ', albums_list)
    music_reports.default_view()
    albums_list = music_reports.edit_album_entry(albums_list, album_index_to_edit)
    music_reports.export_list_to_file(albums_list)
    music_reports.default_view()

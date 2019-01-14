import music_reports
import display
import os


def main():
    os.system('clear')
    albums_list = music_reports.import_data_from_file()
    display.main_menu()

    wiev_all_albums = 1
    find_albums_by_genre = 2
    albums_in_time_range = 3
    shortest_longest_albums = 4
    find_albums_by_artist = 5
    find_albums_by_title = 6
    show_statistics = 7
    leave_program = 8

    while True:
        user_chosen_action = music_reports.get_user_action()
        if user_chosen_action == wiev_all_albums:
            os.system('clear')
            display.main_menu()
            display.table(albums_list)
        elif user_chosen_action == find_albums_by_genre:
            chosen_genre = music_reports.user_chosen_input('Enter music genre: ')
            albums_by_genre = music_reports.find_albums_by_condition(albums_list, chosen_genre, 3)
            os.system('clear')
            display.main_menu()
            display.table(albums_by_genre)
        elif user_chosen_action == albums_in_time_range:
            time = music_reports.get_dates_to_filter()
            os.system('clear')
            display.main_menu()
            albums_between_time = music_reports.albums_from_given_time_range(albums_list, *time)
            display.table(albums_between_time)
        elif user_chosen_action == shortest_longest_albums:
            max_min_list = music_reports.max_min_time(albums_list)
            os.system('clear')
            display.main_menu()
            display.table(max_min_list)
        elif user_chosen_action == find_albums_by_artist:
            chosen_artist = music_reports.user_chosen_input('Enter artist name: ')
            albums_by_artist = music_reports.find_albums_by_condition(albums_list, chosen_artist, 0)
            os.system('clear')
            display.main_menu()
            display.table(albums_by_artist)
        elif user_chosen_action == find_albums_by_title:
            chosen_album_title = music_reports.user_chosen_input('Enter album title: ')
            albums_by_album_title = music_reports.find_albums_by_condition(albums_list, chosen_album_title, 1)
            os.system('clear')
            display.main_menu()
            display.table(albums_by_album_title)
        elif user_chosen_action == show_statistics:
            os.system('clear')
            display.main_menu()
            print('Shortest and longest albums:')
            longest_shortest_albums = music_reports.max_min_time(albums_list)
            display.table(longest_shortest_albums)
            print('\nYoungest and oldest albums:')
            youngest_oldest_albums = music_reports.get_young_old_album(albums_list)
            display.table(youngest_oldest_albums)
            print('\nAlbums count is: {}'.format(len(albums_list)))
            print('\nAlbums by given the genres')
            albums_count_by_given_genres = music_reports.get_albums_count_by_given_genres(albums_list)
            print(albums_count_by_given_genres)
        elif user_chosen_action == leave_program:
            break


if __name__ == '__main__':
    main()

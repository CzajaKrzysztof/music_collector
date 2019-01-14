import music_reports
import display
import os


def main():
    os.system('clear')
    albums_list = music_reports.import_data_from_file()
    display.main_menu()
    while True:
        user_chosen_action = music_reports.get_user_action()
        if user_chosen_action == 1:
            os.system('clear')
            display.main_menu()
            display.table(albums_list)
        elif user_chosen_action == 2:
            chosen_genre = music_reports.user_chosen_input('Enter music genre: ')
            albums_by_genre = music_reports.find_albums_by_condition(albums_list, chosen_genre, 3)
            os.system('clear')
            display.main_menu()
            display.table(albums_by_genre)
        elif user_chosen_action == 3:
            time = music_reports.get_dates_to_filter()
            os.system('clear')
            display.main_menu()
            albums_between_time = music_reports.albums_from_given_time_range(albums_list, *time)
            display.table(albums_between_time)
        elif user_chosen_action == 4:
            max_min_list = music_reports.max_min_time(albums_list)
        elif user_chosen_action == 5:
            chosen_artist = music_reports.user_chosen_input('Enter artist name: ')
            albums_by_artist = music_reports.find_albums_by_condition(albums_list, chosen_artist, 0)
            os.system('clear')
            display.main_menu()
            display.table(albums_by_artist)
        elif user_chosen_action == 6:
            chosen_album_title = music_reports.user_chosen_input('Enter album title: ')
            albums_by_album_title = music_reports.find_albums_by_condition(albums_list, chosen_album_title, 1)
            os.system('clear')
            display.main_menu()
            display.table(albums_by_album_title)
        elif user_chosen_action == 7:
            pass
        elif user_chosen_action == 8:
            break


if __name__ == '__main__':
    main()

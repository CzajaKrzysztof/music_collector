import music_handlers
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
            music_handlers.handle_view_all_albums(albums_list)
        elif user_chosen_action == find_albums_by_genre:
            music_handlers.handle_find_albums_by_genre(albums_list)
        elif user_chosen_action == albums_in_time_range:
            music_handlers.handel_albums_in_time_range(albums_list)
        elif user_chosen_action == shortest_longest_albums:
            music_handlers.handle_shortest_longest_albums(albums_list)
        elif user_chosen_action == find_albums_by_artist:
            music_handlers.handle_find_albums_by_artist(albums_list)
        elif user_chosen_action == find_albums_by_title:
            music_handlers.handle_find_albums_by_title(albums_list)
        elif user_chosen_action == show_statistics:
            music_handlers.handle_show_statistics(albums_list)
        elif user_chosen_action == leave_program:
            break


if __name__ == '__main__':
    main()

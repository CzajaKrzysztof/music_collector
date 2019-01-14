import music_reports
import display


def main():
    albums_list = music_reports.import_data_from_file()
    music_reports.temp_print(albums_list)
    print("\n\n")
    albums_by_genre = music_reports.find_albums_by_condition(albums_list, 'rock', 3)
    music_reports.temp_print(albums_by_genre)


if __name__ == '__main__':
    main()

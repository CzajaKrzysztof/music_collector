import music_reports


def main_menu():
    print('MAIN MENU:')
    print("1: view all imported albums")
    print("2: find all albums by genre")
    print("3: find all albums from given time range")
    print("4: find shortest/longest album")
    print("5: find all albums created by given artist")
    print("6: find album by title")
    print("7: collection statistics")
    print("8: add new album")
    print("9: edit entry")
    print("0: exit")
    print('\n')


def show_table(albums_list, table_title, sugestion='no'):
    if albums_list == None:
        if sugestion == 'yes':
            print('')
        else:
            print('No albums to show.')
    elif len(albums_list) == 0:
        if sugestion == 'yes':
            print('')
        else:
            print('No albums to show.')
    else:
        i = 1
        padding = 3
        lp_length = 4
        artis_length = music_reports.get_max_column_length(albums_list, 0) + padding
        title_length = music_reports.get_max_column_length(albums_list, 1) + padding
        year_length = music_reports.get_max_column_length(albums_list, 2) + padding
        genre_length = music_reports.get_max_column_length(albums_list, 3) + padding
        time_length = music_reports.get_max_column_length(albums_list, 4) + padding

        print('\n{:^{table_length}}\n'.format(table_title, table_length=(lp_length + artis_length + title_length
                + year_length + genre_length + time_length + 17)))
        print("{:^{width_lp}} | {:^{width_artist}s} | {:^{width_title}s} | {:^{width_year}} | {:^{width_genre}s} | {:^{width_time}s} |".format('lp.', 'Artist', 'Title', 'Year', 'Genre', 'Length', width_lp=lp_length, width_artist=artis_length, width_title=title_length, width_year=year_length, width_genre=genre_length, width_time=time_length))

        print('-' * (lp_length + artis_length + title_length + year_length + genre_length + time_length + 17))
        for item in albums_list:
            print("{:^{width_lp}} | {:^{width_artist}s} | {:^{width_title}s} | {:^{width_year}} | {:^{width_genre}s} | {:^{width_time}s} |".format(i, item[0], item[1], item[2], item[3], item[4], width_lp=lp_length, width_artist=artis_length, width_title=title_length, width_year=year_length, width_genre=genre_length, width_time=time_length))
            i += 1


def show_dict_in_table(data_from_dict, table_title):
    padding = 1
    aditional_signs = 3
    keys_length = music_reports.get_max_column_length(data_from_dict, 0) + padding
    value_length = music_reports.get_max_column_length(data_from_dict, 1) + padding

    print('\n{:^{table_length}}'.format(table_title, table_length=(padding + keys_length + value_length + 3)))
    print('-' * (padding + keys_length + value_length + aditional_signs))
    for element in data_from_dict:
        print('{:{len_key}} | {:{len_val}}'.format(*element, len_key=keys_length, len_val=value_length))


def show_single_album(album_entry):
    print('Artist: {}\nTitle:  {}\nYear:   {}\nGenre:  {}\nLength: {}'.format(*album_entry))

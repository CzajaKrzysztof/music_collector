import music_reports


def main_menu():
    """ Function displays main manu. """
    print('MAIN MENU:')
    print("1: view all imported albums")
    print("2: find all albums by genre")
    print("3: find all albums from time range")
    print("4: find shortest/longest album")
    print("5: find all albums created by artist")
    print("6: find album by title")
    print("7: collection statistics")
    print("8: add new album")
    print("9: edit entry")
    print("0: exit")
    print('\n')


def show_table(albums_list, table_title, sugestion='no'):
    """
    Function displays given albums_list in form of list of list as table. Function require list of
    albums, titlefor table. Optional parametre sugestion is used for displaying sugestions table
    """
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
        lp_len = 4
        additional_chars = 17
        artis_len = music_reports.get_max_column_length(albums_list, 0) + padding
        title_len = music_reports.get_max_column_length(albums_list, 1) + padding
        year_len = music_reports.get_max_column_length(albums_list, 2) + padding
        genre_len = music_reports.get_max_column_length(albums_list, 3) + padding
        time_len = music_reports.get_max_column_length(albums_list, 4) + padding

        table_string = "{:^{w_lp}} | {:^{w_artist}s} | {:^{w_title}s} | {:^{w_year}} | {:^{w_genre}s} | {:^{w_time}s} |"
        lengths_dictionary = {'w_lp': lp_len, 'w_artist': artis_len, 'w_title': title_len, 'w_year': year_len, 'w_genre': genre_len, 'w_time': time_len}
        summary_of_lengths = lp_len + artis_len + title_len + year_len + genre_len + time_len + additional_chars

        print('\n{:^{table_length}}\n'.format(table_title, table_length=summary_of_lengths))

        print(table_string.format('lp.', 'Artist', 'Title', 'Year', 'Genre', 'Length', **lengths_dictionary))

        print('-' * summary_of_lengths)
        for item in albums_list:
            print(table_string.format(i, *item, **lengths_dictionary))
            i += 1


def show_dict_in_table(data_from_dict, table_title):
    """ Function display given dictionary i form of table """
    padding = 1
    additional_signs = 3
    keys_length = music_reports.get_max_column_length(data_from_dict, 0) + padding
    value_length = music_reports.get_max_column_length(data_from_dict, 1) + padding
    tab_len = padding + keys_length + value_length + additional_signs

    print('\n{:^{table_length}}'.format(table_title, table_length=tab_len))
    print('-' * tab_len)
    for element in data_from_dict:
        print('{:{len_key}} | {:{len_val}}'.format(*element, len_key=keys_length, len_val=value_length))


def show_single_album(album_entry):
    """ Function display single album entry in form of table """
    print('Artist: {}\nTitle:  {}\nYear:   {}\nGenre:  {}\nLength: {}'.format(*album_entry))

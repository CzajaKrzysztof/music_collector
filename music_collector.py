import music_reports
import display

def main():
    albums_list = music_reports.import_data_from_file()
    print(albums_list)

if __name__ == '__main__':
    main()

def make_album(artist_name, album_title):
    album = {'Artist name': artist_name, 'Album title': album_title}
    return album
while True:
    print('\ntell me the name of the artist and the title of the album'.title())
    print("(enter 'q' to quit any time)")
    artist = input('Enter the name of the airtist: ')
    if artist == 'q':
        break
    title = input('Enter the name of the album: ')
    if title == 'q':
        break
print_album1 = make_album(artist, title)
print('\n')
print(print_album1)
print('\n')
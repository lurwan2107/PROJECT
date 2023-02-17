def make_album(artist_name, album_title, num_of_song = None):
    album = {'Artist name': artist_name, 'Album title': album_title}
    if num_of_song:
        album['Number of song'] = num_of_song
    return album
print_album1 = make_album('Rarara', 'Masu Gudu')
print_album2 = make_album('Gwanja', 'Sama Mata')
print_album3 = make_album('Naziru', 'Katin Zabe')
print_album4 = make_album('Ala', 'Jami\'a', num_of_song = 20)
print('\n')
print(print_album1)
print(print_album2)
print(print_album3)
print(print_album4)
print('\n')
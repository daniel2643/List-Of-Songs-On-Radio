def sortMenu(counter_digit):
    infile = open("raw_menu.txt", 'r')
    song_list = []
    for line in infile:
        song_list.append(line)
    if len(str(len(song_list))) <= counter_digit:
        counter_digit = len(str(len(song_list)))


    sorted_song_list = []

    for i in range(0, len(song_list)):
        no = ''
        for char in song_list[i]:
            try:
                no += str(int(char))
            except ValueError:
                break

        song_list[i] = song_list[i][len(no):]

        counter = str(i+1)
        for _ in range(counter_digit - len(counter)):
            counter = '0' + counter

        song_list[i] = counter + ' -- ' + song_list[i]
        sorted_song_list.append(song_list[i])
        #print(song_list)
        #input()



    infile.close()

    outfile = open('sorted_menu2.txt', 'w')
    for song in sorted_song_list:
        if song is not None:
            outfile.write(song)

    outfile.close()

    return song_list








if __name__ == '__main__':
    # Test usabilty
    #digit_no = int(input("How many format digits do you want"))
    #song_no = int(input("Song No. : "))
    #print(sortMenu(digit_no)[song_no])

    digit_no = int(input("How many format digits do you want"))
    sortMenu(digit_no)

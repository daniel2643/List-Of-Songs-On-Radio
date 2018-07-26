# List-of-songs-on-Radio
Create a readable media list that broadcast in a normal radio device. This is the version 2 without renaming raw media files after building the sorted media list.

Recently, due to a large groups of emerging technology, radios could not only broadcast news but also play musics and stories by inserting tf cards. Sometimes, a small tf card may store thousand of songs, which in turn, make people feel confused about which song to listen.

LoR(abbreviation of the project) creates a sorted list of all songs in played order to optimise user experience. 

## STEPS:
Preparation: the example gives a tf card with a folder '1298' which represents there are 1298 media files inside.
1. catch all names of songs from original tf card in terminal. The command shows below.
```
cd ~/1298                       # open tf card file
ls . >raw_menu.txt                  # input all file names into a txt file called "raw_menu.txt"
```

2. Run the core python file.
```
cd ..
python3 menu2.py
```

3. The sorted result is in the "sorted_menu2.txt" file
```
open sorted_menu2.txt
```

## Algorithms:
1. String Formatting
2. Direct Addressing

## TO DO:
rename muiltiple files in a folder with a generated txt file.

# Audio Manipulation Folder
---
**DateCreated**: 190507

**Objective**: this folder will house various sandbox projects to try and improve ability to manipulate audio files (primarily mp3) with Python for batch editing.

## Applications:
* batch metadata manipulation
* batch audio clip editing (replace one clip with another)
* conversion to mp3 file format
* rapid metadata editing tool

## Useful links: 
metadata manipulation lib: https://mutagen.readthedocs.io/en/latest/user/id3.html
possible audio manipulation lib: https://github.com/jiaaro/pydub#installation


## Goals (as of 190624)
* convert all music files to mp3 - done(190624)
* consider using "album artist" instead of "contributing artist" for "artist" field - nah, not worth (190701)
* create ui to easily manipulate each file - almost done (190701)
.......... div for what's done ..................
* make metadata backup of current files - in prog
* give every music file appropriate metadata (name, artist, album, etc) - inprog
* put all album songs in respective folders - inprog
* give every folder appropriate name (<Artist> - <Album>)
* standardize all music genres to set list - actually, give *appropriate* music genre
* remove unneeded comments from every music file
* give proper filename to every song (<Track> <Artist> - <Name>.mp3)

## Conventions
in comment tag: 
  good1: all properties correct
  good2: filename correct
  good3: in appropriate folder
  
YouTube Song Scraper
============

This is a skeleton for a scraper that pulls videos off of YouTube and converts them to audio files. The basic idea is as follows:

  * Utilizes the Python Mechanize library to open up webpages and interact
  * The user will enter an artist and the script will launch YouTube and search for the artist
  * All of the URLs for the videos are scraped and put into an online video to mp3 converter, with the resulting file downloaded to the users computer
  * I created a set of artists to use for result validation on YouTube and title parsing
  
Potential ideas for future extension included:

  * Utilizing a threadpool to handle multiple videos at a time
  * Creating a context free grammar to properly parse artist names and song titles for saving purposes
  * Build a map of artist names to songs/albums to avoid duplication
  
For fear of YouTube reprisals (especially if a threadpool was use, i.e. high volume of accesses), I've put development on hold, but the skeleton can be used for any number of other projects. 

# Tournament Runner
## You can use Tournament Runner to run Soccer Simulation 2D tournaments.
-----------------------



### :gear: Get started

First you should put all the binaries in `Bins` directory. All binaries must contain `localStartAll` and `start` script.

To run a tournament, put the list of the games in `Games.txt` and then, execute `Run.sh` with
```
./Run.sh
```
After the games are finished, you can see logs (.rcg and .rcl files) compressed to .tar.gz in Logs directory. 

Also, you can see Holes and Clashes table in the terminal when the games are done.

-------------------------------------------

### :hash: Test Game

A test game is a short 300 Cycle game against Helios2023. It ONLY has one half and no penalty or extra time.

You can run it with `./TestTeams.sh`

Note that for test games, you should put the teams list in `TestGames.txt` and Helios2023 should be available in Bins directory.   

-------------------------------------------

### :green_book: Note: This Repository uses [HoleAnalyzer](https://github.com/RCSS-IR/HoleAnalyzer) for analyzing Holes&Clashes.
Thanks go to [Nader Zare](https://github.com/naderzare), [Alireza Sadraii](https://github.com/sadraiiali), [Omid Amini](https://github.com/mroa4) and [Aref Sayareh](https://github.com/Arefsa78) for providing HoleAnalyzer.

--------------------------------------------

# :heavy_exclamation_mark: Issues
If you have any problem, do not hesitate to contact me via Email: mazloomsoroush@gmail.com 

OR

go to https://github.com/SoroushGit/Tournament-Runner and open an issue.

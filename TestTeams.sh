#!/bin/bash

echo Starting a major tournament...
mkdir TestLogs
for(( i=1; i <= $(wc -l < TestGames.txt); i++)) do
    TEAM=$(sed -n "$i"p TestGames.txt)
    if [ "$TEAM" = " " ]; then
	    continue
    fi
    if [ "$TEAM" = "" ]; then
	    continue
    fi
    TEAMT="Helios2023"
    VS=" vs "
    touch Mg
    echo $TEAM $VS $TEAMT > Mg
    python3 EditMoment.py
    rcssserver server::penalty_shoot_outs = false  server::fullstate_l = true server::fullstate_r = true server::auto_mode = true server::synch_mode = false server::half_time = 30 server::nr_normal_halfs = 1 server::nr_extra_halfs = 0 server::game_log_dir = `pwd` server::keepaway_log_dir = `pwd` server::text_log_dir = `pwd` & server::penalty_shoot_outs = false
    cd ../ScBot && ./Bot.sh && cd ../SummerCup2023-Tournament-Runner
    sleep 1
    server_pid=$!
    sleep 1
    cd Bins/$TEAM && ./localStartAll &
    sleep 1
    cd Bins/$TEAMT && ./localStartAll &
    wait $server_pid
    sleep 1
    python3 AnalyzeResult.py
    sleep 1
    cd ScBot && ./FgBot.sh && cd ..
    ./LogCompressor.sh
    mv *.rcg.tar.gz TestLogs
    mv *.rcl.tar.gz TestLogs
    rm Mg
done

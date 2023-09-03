#!/bin/bash

echo Starting a major tournament...
for(( i=1; i <= $(wc -l < Games.txt); i++)) do
    TEAM=$(sed -n "$i"p Games.txt)
	if [ "$TEAM" = -------------------- ]; then
	    continue
    fi
    i=$((i+1))
    TEAMT=$(sed -n "$i"p Games.txt)
    VS=" vs "
    touch Mg
    echo $TEAM $VS $TEAMT > Mg
    python3 EditMoment.py
    rcssserver server::fullstate_l = false server::fullstate_r = false server::auto_mode = true server::synch_mode = false server::game_log_dir = `pwd` server::keepaway_log_dir = `pwd` server::text_log_dir = `pwd` server::nr_extra_halfs = 0 server::penalty_shoot_outs = false &
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
    python3 ChangeLogDir.py
    rm Mg
done

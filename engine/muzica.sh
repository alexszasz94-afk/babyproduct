#!/bin/bash
# Pune muzica peste video: piesa pornește de la START (s), sunetul generat rămâne încet dedesubt.
# Rulare: engine/muzica.sh video.mp4 piesa.mp3 START out.mp4 [vol_muzica] [vol_sunet]
set -e
V=$1; M=$2; ST=$3; OUT=$4; VM=${5:-0.9}; VS=${6:-0.3}
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
FO=$(python3 -c "print(max(0,$D-0.8))")
ffmpeg -y -loglevel error -i "$V" -ss "$ST" -t "$D" -i "$M" -filter_complex \
 "[1:a]aresample=48000,aformat=channel_layouts=stereo,volume=$VM,afade=t=in:d=0.15,afade=t=out:st=$FO:d=0.8[m];[0:a]volume=$VS[s];[m][s]amix=inputs=2:duration=first:normalize=0[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -movflags +faststart "$OUT"

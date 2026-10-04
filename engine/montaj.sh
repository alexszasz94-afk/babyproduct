#!/bin/bash
# Montaj local: clipuri (în ordine) + text PNG peste tot videoul, păstrează sunetul generat.
# Rulare: engine/montaj.sh out.mp4 text.png clip1.mp4 clip2.mp4 ...
set -e
OUT=$1; TXT=$2; shift 2
IN=""; F=""; N=0
for c in "$@"; do
  IN="$IN -i $c"
  F="$F[$N:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,format=yuv420p[v$N];[$N:a]aresample=48000,aformat=channel_layouts=stereo[a$N];"
  N=$((N+1))
done
CAT=""; for i in $(seq 0 $((N-1))); do CAT="$CAT[v$i][a$i]"; done
ffmpeg -y -loglevel error $IN -i "$TXT" -filter_complex "${F}${CAT}concat=n=$N:v=1:a=1[v][a];[v][$N:v]overlay[vo]" \
  -map "[vo]" -map "[a]" -c:v libx264 -crf 17 -preset slow -c:a aac -b:a 192k -movflags +faststart "$OUT"

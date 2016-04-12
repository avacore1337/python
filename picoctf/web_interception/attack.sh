#!/bin/bash
# PADD='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
PADD='aaaaaaaaaaaa'
# ANS=''5f6f6e5f796f75725f66697273745f6563625f64
# PADD='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# echo $PADD
# ANS='20485454502f312e310a436f6f6b69653a20666c6167'
ANS='20485454502f312e310d0a436f6f6b69653a20666c61673d636f6e67726174735f6f6e5f796f75725f66697273745f6563625f64'
for (( i = 0; i < 38; i++ )); do
  #statements
  SOLUTION=$(echo $PADD | nc vuln2014.picoctf.com 65414 | tail -n+2 | tail -c+96 | head -c16)
  # echo $SOLUTION
  for i in 0 1 2 3 4 5 6 7 8 9 a b c d e f; do
    for j in 0 1 2 3 4 5 6 7 8 9 a b c d e f; do
      TEST=$(echo $PADD$ANS$i$j | nc vuln2014.picoctf.com 65414 | tail -n+2 | tail -c+96 | head -c16)
      # echo $TEST
      if [ "$TEST" == "$SOLUTION" ]; then
        # echo 0x$i$j | xxd -r
        echo $i$j
        ANS=$ANS$i$j
        PADD=${PADD#aa}
        # echo $PADD
      fi
      # echo $i
    done
  done
done
# 2f
# TEST=$(echo aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa20485454502f312e31$i$j | nc vuln2014.picoctf.com 65414 | tail -n+2 | tail -c+64 | head -c16)
# 3d636f6e677261
# 5f6f6e5f796f75725f66697273745f6563625f64

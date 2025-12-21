#!/bin/bash

DIAL=50
PWD=0

while read -r LINE
do
	PREV=$DIAL
	if [[ "$LINE" =~ ^[[:space:]]*$ ]]
	then
		continue
	fi
	DIRECTION=${LINE%%[0-9]*}
	VAL=${LINE##*[A-Z]}

	if (( VAL > 100 ))
	then
		(( PWD += (VAL / 100) ))
		(( VAL %= 100 ))
	fi

	if [[ "$DIRECTION" == "L" ]]
	then
		SIGN_VAL=$((-VAL))
	else
		SIGN_VAL=$((VAL))
	fi

	SUM=$(( DIAL + SIGN_VAL ))

	REM=$(( (SUM + 100) % 100 ))

	if (( SUM >= 100 || (SUM <= 0 && PREV != 0) ))
	then
		(( PWD += 1 ))
	fi

	DIAL=$REM

done <input

echo "PWD=$PWD"

#!/bin/bash

DIAL=50
PWD=0

while read -r LINE
do
	if [[ "$LINE" =~ ^[[:space:]]*$ ]]
	then
		continue
	fi
	DIRECTION=${LINE%%[0-9]*}
	VAL=${LINE##*[A-Z]}

	if [[ "$DIRECTION" == "L" ]]
	then
		SIGN_VAL=$((-VAL))
	else
		SIGN_VAL=$VAL
	fi

	REM=$(( (DIAL + SIGN_VAL) % 100 ))

	if (( REM < 0 ))
	then
		(( REM += 100 ))
	elif (( REM == 0 ))
	then
		(( PWD += 1 ))
	fi

	DIAL=$REM

done <input

echo "PWD=$PWD"

if command -v myProgram &> /dev/null; then
	echo "program found"
	exit
else
	echo "program not found"
	exit
fi


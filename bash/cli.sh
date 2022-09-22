#!/bin/bash

print_usage() {
   # Display Help
   echo "#############################################"
   echo "An Example bash script command line interface"
   echo
   echo "Syntax: $(basename "$0") [-r|j|c|h]"
   echo "options:"
   echo "r     Run"
   echo "c     Crawl"
   echo "j     Jump"
   echo "h     Print this help message"
   echo
}

# Parse CLI argument
# first check to make sure at least one option is provided
if [ $# -eq 0 ]; then
  echo "Please Provide at least one flag..."
  print_usage
  exit 1
fi

# Then go through the remainder of the flags 'rjch'
while getopts 'rjch' opt; do
  case "$opt" in
    r)
      echo "Run"
      ;;
    j)
      echo "Jump"
      ;;
    c)
      echo "Crawl"
      ;;
    # \? covers flags not listed
    \?|h)
      # show help message and exit
      print_usage
      exit 0
      ;;
  esac
done
shift $((OPTIND-1))
# shift $((OPTIND-1)) will remove a flag from so the option is not run over and over again.
# so for example, if both 'r' and 'c' flags are provided (e.g., -rc) it will "Run" then "Crawl"

#!/usr/bin/bash

# check if archive folder exists
if [ ! -d "archive" ]
then
    mkdir archive
fi

# get current date and time
time=$(date +"%Y%m%d-%H%M%S")

# new file name
newfile="grades_$time.csv"

# move and rename file
mv grades.csv archive/$newfile

# create a new empty grades.csv
touch grades.csv

# save log
echo "$time moved grades.csv to archive/$newfile" >> organizer.log

echo "Done archiving."

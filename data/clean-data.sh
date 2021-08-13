#!/bin/bash
# clean-data.sh
# v1 Jon Kleinberg, 2020
# v2 Lillian Lee, March 2021
cat a2c-census2020.csv | sed 's/Select your admission decision results for each school you applied to: /dec:/g'| sed 's/Which of the following did you apply to\? //g' | sed 's/University/U/g' | sed 's/U of /U/g' | sed 's/UCalifornia/UC/g' | sed 's/Applied //g' | sed 's/ - /-/g' | sed 's/ /_/g' | \
    # get rid of last weird line
    grep -v 'x,x'| \
    # discard people with both accept and reject
    grep -v 'Accepted;_Rejected' | \
    awk -F, -f clean-data-helper.awk | \
    sed 's/\[//g' | sed 's/\]//g'  |   \
    # remove double U Miami 
    sed 's/UMiami : Accepted ## UMiami : Accepted ##/UMiami : Accepted ##/g' |  \
    sed 's/UMiami : Rejected ## UMiami : Rejected ##/UMiami : Rejected ##/g' | \
    sed 's/UMiami : Wait-listed ## UMiami : Wait-listed ##/UMiami : Rejected ##/g' |\
    nl |\
    # # fix weird problem with 2821, 2822 and 2833
   sed 's/...2821./ /g' | sed 's/...2822./ /g' | sed 's/...2823./ /g' | less

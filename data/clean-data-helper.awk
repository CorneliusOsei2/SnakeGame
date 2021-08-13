# clean-data-helper.awk
# Jon Kleinberg, 2020, very minor mods Lillian Lee, Mar 2021
# NOTE: prints "BAD OUTCOMEEEEE " for unexpected outcomes
# Convert "Accepted;_Wait-listed" to "Accepted", and similarly for "Rejected;_Wait-listed"

NR == 1 {
 for (i = 33; i <= 263; ++i) {
   college[i-32] = $i;
   column[$i] = i
 }
}
NR > 1 && NF >= 505 && length($505) > 0 {
 nonempty = 0;
 for (i = 269; i <= 499; ++i) {
   if ($i != "") {
     if (nonempty == 0) {
       printf ">> "
     }
     if ($i == "Accepted;_Wait-listed") {
       $i = "Accepted"
     }
     if ($i == "Rejected;_Wait-listed") {
      $i = "Rejected"
     }
     printf college[i-268]" : "$i" ## "
     if (index("Accepted,Wait-listed,Rejected", $i) == 0) {
      printf("BAD OUTCOMEEEEE ")
     }
     nonempty = 1;
   }
 }
 if (nonempty) {
   printf "enr : " $505
   print " "
 }
}


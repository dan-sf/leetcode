# Write a bash script to calculate the frequency of each word in a text file

cat word_freq.txt \
| awk 'BEGIN{ORS=" "}{print "NONE "$0" NONE";}' \
| awk '{len=split($0,arr," "); output["NONE"] = 0;
        for (i=0;i<len;i++) { if (arr[i] in output) output[arr[i]]++; else output[arr[i]] = 1; }
        for (key in output) { if (key!=" " && key!="NONE" && key!="" && output[key] != 0) print key" "output[key] }}' \
| sort -rnk2,2


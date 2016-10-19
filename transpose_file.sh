# Given a text file file.txt, transpose its content.
# 
# You may assume that each row has the same number of columns and each field is
# separated by the ' ' character.
# 
# For example, if file.txt has the following content:

# Transpose a text file's contents
cat transpose_file.txt | awk '{for (i=1;i<=NF;i++) { if (NR==1) {col_arr[i]=$i;} else {col_arr[i]=col_arr[i]" "$i;} }}
                               END{for (val in col_arr) {print col_arr[val];}}'


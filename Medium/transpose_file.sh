# Read from the file file.txt and print its transposed content to stdout.
col=$(($(head -n1 file.txt | grep -o " " | wc -l)+1))

for ((k=1; k<=$col; k++))
do
    cut -d " " -f"$k" file.txt | paste -d " " -s
done
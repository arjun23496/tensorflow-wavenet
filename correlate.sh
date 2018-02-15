for filename in ../data/test-corpus/*.entropy; do
	echo "Processing : $filename"
	string=$(python splitter.py $filename)
	read -ra ADDR <<< "$string"
	index="${ADDR[0]}"
	count="${ADDR[1]}"
	python cross_correlation.py output/speaker_p$($index)_$($count).npy results/figures $($index) $($count) 
	break
done

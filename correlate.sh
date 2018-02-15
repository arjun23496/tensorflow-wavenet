for filename in ../data/test-corpus/*.entropy; do
	echo "Processing : $filename"
	string=$(python splitter.py $filename)
	read -ra ADDR <<< "$string"
	index="${ADDR[0]}"
	count="${ADDR[1]}"
	wav_out_path="results/output/speaker_p$index_$count.npy"
	wav_seed="$filename"
	figure_path="results/figures"
	echo $index
	echo $count
	echo $wav_out_path
	echo $wav_seed
	echo $figure_path
	python cross_correlation.py $wav_out_path $figure_path $index $count 
done

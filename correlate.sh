for filename in ../data/test-corpus/*.entropy; do
	echo "Processing : $filename"
	string=$(python splitter.py $filename)
	read -ra ADDR <<< "$string"
	index="${ADDR[0]}"
	count="${ADDR[1]}"
	# python generate.py --samples 8000 --wav_out_path results/output/speaker_p$($index)_$($count).npy --gc_cardinality=120 --gc_channels=119 --gc_id=$($index) --wav_seed ../data/test-corpus/$($filename) logdir/train/2018-02-06T21-26-11/model.ckpt-54350
	python cross_correlation.py output/speaker_p$($index)_$($count).npy results/figures $($index) $($count) 
done
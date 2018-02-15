for filename in ../data/test-corpus/*.entropy; do
	echo "Processing : $filename"
	string=$(python splitter.py $filename)
	read -ra ADDR <<< "$string"
	index="${ADDR[0]}"
	count="${ADDR[1]}"
	wav_out_path="results/output/speaker_p$(echo $index)_$(echo $count).npy"
	wav_seed="$filename"
	figure_path="results/figures"
	echo $index
	echo $count
	echo $wav_out_path
	echo $wav_seed
	echo $figure_path
	python generate.py --samples 20000 --wav_out_path $wav_out_path --gc_cardinality=120 --gc_channels=119 --gc_id $index --wav_seed $wav_seed logdir/train/2018-02-06T21-26-11/model.ckpt-54350
	python plotter.py $wav_out_path $figure_path $index $count 
done

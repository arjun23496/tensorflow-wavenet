for filename in ../data/test-corpus/*.entropy do:
	echo $filename
	# python generate.py --samples 8000 --wav_out_path speaker.npy --gc_cardinality=120 --gc_channels=119 --gc_id=1 --wav_seed ../data/test-corpus/$($filename) logdir/train/2018-02-06T21-26-11/model.ckpt-54350
done
# Training
python train.py --l2_regularization_strength 1e-5 --silence_threshold 0 --gc_channels 342 --data_dir ../data/corpus

# Testing
python generate.py --samples 8000 --wav_out_path speaker.npy --gc_cardinality=120 --gc_channels=119 --gc_id=1 --wav_seed ../data/test-corpus/p1_17.entropy logdir/train/2018-02-06T21-26-11/model.ckpt-54350
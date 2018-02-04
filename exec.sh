# Training
python train.py --l2_regularization_strength 1e-5 --silence_threshold 0 --data_dir ../data/corpus

# Testing
python generate.py --samples 8000 --wav_out_path speaker.npy --gc_cardinality=343 --gc_id=1 --wav_seed ../data/corpus/entropy_files/p1/p1_1.entropy logdir/train/2018-02-03T02-11-15/model.ckpt-75800
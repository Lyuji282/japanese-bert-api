#!/usr/bin/env bash

#bert-serving-start -model_dir ./models/jm/ &&\
#                   -num_worker 1 &&\
#                   -max_seq_len=128 &&\
#                   -pooling_strategy "REDUCE_MEAN" &&\
#                   -show_tokens_to_client 1 &&\
#                   -pooling_layer -2 &

python server.py
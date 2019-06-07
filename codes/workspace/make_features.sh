#!/usr/bin/env bash

export BERT_BASE_DIR="../models/jm"

python ../extract_features.py \
  --input_file=./input.txt \
  --output_file=./output.jsonl \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --do_lower_case False \
  --layers -2

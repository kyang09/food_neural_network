** Artificial Intelligence for Food **

## System Requirements

- Python 3
- Tensorflow > 0.12
- Numpy
- Virtualenv

## How to use

Use json_classify_yelp_dataset.py to pre-process Yelp food reviews data into positive and negative reviews.
Open json_classify_yelp_dataset.py and refer to the file names that the script uses to generate prepared data.

Train:

```bash
./train.py
```

## Evaluating

```bash
./eval.py --eval_train --checkpoint_dir="./runs/1529104734/checkpoints/"
```

where 1529104734 is the run ID found in the /runs directory.

## References

- [Text Understanding from Scratch](https://arxiv.org/pdf/1502.01710.pdf)
- [CNNs for Sentence Classification](https://arxiv.org/abs/1408.5882)

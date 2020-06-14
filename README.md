# Numbers recognition

In order to convert audio record into a number we propose to encode a target number into its verbal representation and convert it to encoded format.
For example:

```123456 -> сто двадцать три тысячи четыреста пятьдесят шесть -> 100 20 3 1000 4 100 50 6```

```` 500100 -> пятьсот тысяч сто -> 500 1000 100 ````

After that we apply ctc loss based training with tokens like "100", "1000" and etc

### Text pre-processing:
```python preprocess.py -i  {train_csv} -d {data_dir}```

### Training:
```python train.py --train-manifest data/train_manifest.csv --val-manifest data/valid_manifest.csv ```

### Inference:

```python transcribe.py --model-path models/deepspeech_final.pth --audio-path /path/to/audio.wav```
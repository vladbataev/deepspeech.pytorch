import argparse
import json
import os

import pandas as pd
import tqdm


from sklearn.model_selection import train_test_split

from convert import convert_to_tokens


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_csv", "-i", type=str, required=True)
    parser.add_argument("--data_dir", "-d", type=str, required=True)

    args = parser.parse_args()
    df = pd.read_csv(args.train_csv)

    text_paths = []
    vocab = {}
    text_dir = os.path.join(args.data_dir, "txt")
    os.makedirs(text_dir, exist_ok=True)
    for i, row in tqdm.tqdm(df.iterrows()):
        tokens = convert_to_tokens(row["number"])
        encoded_tokens = []
        for t in tokens:
            if t not in vocab:
                vocab[t] = chr(len(vocab) + ord("a"))
            encoded_tokens.append(vocab[t])
        text_path = os.path.join(text_dir, f"{i.zfill(6)}.txt")
        with open(text_path, "w") as fout:
            print("".join(encoded_tokens), file=fout)
        text_paths.append(text_path)

    df["text_path"] = text_paths
    df["path"] = df["path"].map(lambda x: os.path.join(args.data_dir, x))
    df = df[["path", "text_path"]]
    train_df, valid_df = train_test_split(df)

    train_manifest = os.path.join(args.data_dir, "train_manifest.txt")
    valid_manifest = os.path.join(args.data_dir, "valid_manifest.txt")
    train_df.to_csv(train_manifest, index=False, header=None)
    valid_df.to_csv(valid_manifest, index=False, header=None)

    print(f"Written train manifest to: {train_manifest}, valid manifest to: {valid_manifest}")

    inv_mapping = {v: k for k, v in vocab.items()}
    labels = ["_"]
    labels.extend(list(inv_mapping.keys()))
    labels.append(" ")

    with open("labels.json", "w") as fout:
        json.dump(labels, fout)

    with open("mapping.json", "w") as fout:
        json.dump(inv_mapping, fout)


if __name__ == "__main__":
    main()

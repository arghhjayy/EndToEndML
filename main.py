from src.preprocess import preprocess
from src.train import train
import pandas as pd


def main():
    train_df = pd.read_csv("dataset/train.csv")
    X_train, y_train = train_df.loc[:"y"], train_df["y"]
    y_train = y_train.replace({"no": 0, "yes": 1})
    X_train_preprocessed = preprocess(X_train)
    X_train_preprocessed.to_csv("intermediate/X_train_preprocessed.csv", index=False, header=False)
    y_train.to_csv("intermediate/y_train.csv", index=False, header=False)

    train()

    # print(X_train_preprocessed.head(10))
    # print(y_train.head(10))


if __name__ == "__main__":
    main()
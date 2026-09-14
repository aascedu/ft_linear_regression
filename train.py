#!/usr/bin/env python3
import argparse
import csv

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, type=argparse.FileType("r"), help="Path to the CSV file")
    parser.add_argument("-i", default=1000, type=int, help="Number of iterations during training")
    args = parser.parse_args()
    return args

def main():
    args = parser()
    km = []
    price = []
    reader = csv.DictReader(args.data)
    for row in reader:
        # if row['km'] is None or row["price"] is None or len(row['km']) == 0 or len(row['price']) == 0:
        #     print(f"Data is malformed: km:{row['km']} / price:{row['price']}")
        #     return
        try:
            km.append(int(row['km']))
            price.append(int(row['price']))
        except:
            print(f"Data is wrong: {row}")
            exit()
    m = len(km)

if __name__ == "__main__":
    main()
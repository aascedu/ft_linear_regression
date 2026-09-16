#!/usr/bin/env python3
import argparse
import csv
import json

class Model():
    normalized_km: list[float]
    price: list[int]
    m: int
    iterations: int
    learning_rate: float
    km_min: float = 0.0
    km_max: float = 0.0
    theta0: float = 0.0
    theta1: float = 0.0

    def __init__(self, args: argparse.Namespace) -> None:
        self.normalized_km = []
        self.price = []
        reader = csv.DictReader(args.data)
        km = []
        for row in reader:
            try:
                km.append(int(row['km']))
                self.price.append(int(row['price']))
            except:
                print(f"Data is wrong: {row}")
                exit()
        self.m = len(km)
        self.iterations = args.i
        self.learning_rate = args.rate
        self.km_min = min(km)
        self.km_max = max(km)
        for x in km:
            self.normalized_km.append((x - self.km_min) / (self.km_max - self.km_min))

    def train(self) -> None:
        for _ in range(self.iterations):
            tmp_theta0 = 0.0
            tmp_theta1 = 0.0
            for i in range(self.m):
                # print(self.normalized_km[i], self.price[i])
                estimate_price = self.theta0 + (self.theta1 * self.normalized_km[i])
                error = estimate_price - self.price[i]
                tmp_theta0 += error
                tmp_theta1 += error * self.normalized_km[i]
            tmp_theta0 = self.learning_rate * (1 / self.m) * tmp_theta0
            tmp_theta1 = self.learning_rate * (1 / self.m) * tmp_theta1
            self.theta0 -= tmp_theta0
            self.theta1 -= tmp_theta1

    def save(self):
        data = {
            "theta0": self.theta0,
            "theta1": self.theta1,
            "km_min": self.km_min,
            "km_max": self.km_max
        }
        with open("model.json", "w") as file:
            json.dump(data, file, indent=4)

def validate_float_input(value):
    value = float(value)
    if value < 0:
        raise argparse.ArgumentTypeError("must be >= 0")
    return value

def validate_int_input(value):
    value = int(value)
    if value < 0:
        raise argparse.ArgumentTypeError("must be >= 0")
    return value

def parser():
    parser = argparse.ArgumentParser(description="Train your linear regression model")
    parser.add_argument("--data", required=True, type=argparse.FileType("r"), help="Path to the CSV file")
    parser.add_argument("-i", default=1000, type=validate_int_input, help="Number of iterations during training (default 1000)")
    parser.add_argument("-r", "--rate", default=0.01, type=validate_float_input, help="Learning rate used by the gradient descent (default 0.01)")
    args = parser.parse_args()
    return args

def main():
    args = parser()
    model = Model(args)
    model.train()
    model.save()

if __name__ == "__main__":
    main()
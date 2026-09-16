#!/usr/bin/env python3

import json

def predict(data):
    try:
        mileage = input("Enter mileage: ")
        mileage = int(mileage)
    except:
        print("Error during input, maybe try with an int.")
        exit()
    normalized_mileage = (mileage - data['km_min']) / (data['km_max'] - data['km_min'])
    estimate_price = data['theta0'] + (data['theta1'] * normalized_mileage)
    print(f"The estimated price is: {estimate_price:0.2f} for {mileage} kms.")

def main():
    with open("model.json", "r") as file:
        model = json.load(file)
        try:
            float(model['theta0'])
            float(model['theta1'])
            int(model['km_min'])
            int(model['km_max'])
        except:
            print("Model value is wrong. Check model.json")
            exit()
    predict(model)

if __name__ == "__main__":
    main()
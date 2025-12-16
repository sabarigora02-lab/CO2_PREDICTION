import pickle
import numpy as np

# Load saved model
filename = 'Saved_Group_1.sav'
with open(filename, 'rb') as file:
    model = pickle.load(file)

print("CO₂ Emission Prediction App")
print("----------------------------")

while True:
    try:
        # Take user input
        volume = float(input("Enter Engine Volume (or -1 to exit): "))
        if volume == -1:
            print("Exiting application...")
            break

        weight = float(input("Enter Vehicle Weight: "))

        # Make prediction
        prediction = model.predict([[volume, weight]])

        print(f"Predicted CO₂ Emission: {prediction[0]:.2f}\n")

    except ValueError:
        print("Invalid input. Please enter numeric values.\n")


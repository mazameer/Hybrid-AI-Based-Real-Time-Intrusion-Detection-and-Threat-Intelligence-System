import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("Starting model training...")

# Generate dummy dataset (since real dataset not present)
data_size = 5000

packet_size = np.random.randint(60,2000,data_size)
protocol = np.random.randint(0,3,data_size)
packet_rate = np.random.randint(1,300,data_size)

X = np.column_stack((packet_size,protocol,packet_rate))

y = []

for r in packet_rate:

    if r > 200:
        y.append(1)

    elif r > 100:
        y.append(1)

    else:
        y.append(0)

y = np.array(y)

print("Dataset created")

# Train Test Split
X_train,X_test,y_train,y_test = train_test_split(
X,y,test_size=0.2,random_state=42
)

# Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Random Forest
rf = RandomForestClassifier(
n_estimators=200,
random_state=42
)

rf.fit(X_train,y_train)

print("Random Forest trained")

# Deep Learning Model
model = Sequential()

model.add(Dense(16,input_shape=(3,),activation="relu"))
model.add(Dense(8,activation="relu"))
model.add(Dense(2,activation="softmax"))

model.compile(
optimizer="adam",
loss="sparse_categorical_crossentropy",
metrics=["accuracy"]
)

model.fit(
X_train,
y_train,
epochs=10,
batch_size=64
)

print("Deep Learning model trained")

# Create models folder if not exists
if not os.path.exists("models"):
    os.makedirs("models")

# Save models
joblib.dump(rf,"models/rf.pkl")
joblib.dump(scaler,"models/scaler.pkl")
model.save("models/dl.keras")

print("Models saved successfully")
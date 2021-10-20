import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from sklearn.preprocessing import MinMaxScaler

labels = np.loadtxt("/content/drive/My Drive/z.txt", delimiter=' ')
labels = np.expand_dims(labels, axis=1)
erphases = np.loadtxt("/content/drive/My Drive/erphases.txt", delimiter=',')
sfphases = np.loadtxt("/content/drive/My Drive/sfphases.txt", delimiter=',')
input =np.concatenate((np.concatenate((erphases, sfphases)),labels), axis=1)

np.random.shuffle(input)
scaler = MinMaxScaler((-1,1))
input[:,0:100] = scaler.fit_transform(input[:,0:100])

X=input[0:470,0:100]
y=np.expand_dims(input[0:470,100], axis=1)

def build(no_features, first_hidden, second_hidden):
  model = Sequential()
  model.add(Dense(first_hidden, input_dim=no_features, activation='relu'))
  model.add(Dropout(0.2))
  model.add(Dense(second_hidden, input_dim=first_hidden, activation='relu'))
  model.add(Dropout(0.2))
  model.add(Dense(1, input_dim=second_hidden, activation='sigmoid'))
  model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
  return model

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=1)

model = build(100,50,10)

metrics = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100, verbose=0, batch_size=10)

plt.plot(metrics.history['accuracy'])
plt.plot(metrics.history['val_accuracy'])
plt.xlabel("Number of epochs", fontsize=14)
plt.ylabel("Accuracy ", fontsize=14)
plt.legend(['Training Accuracy', 'Testing Accuracy'], loc='lower right')
plt.show()

plt.plot(metrics.history['loss'])
plt.plot(metrics.history['val_loss'])
plt.xlabel("Number of epochs", fontsize=14)
plt.ylabel("Loss", fontsize=14)
plt.legend(['Training Loss', 'Testing Loss'], loc='upper right')
plt.show()

print("ACTUAL CLASSES")
print(input[470:500,100])

print("PREDICTED CLASSES")
pred=[]
for i in model.predict(input[470:500,0:100]):
  if i>=0.5: pred.append(1)
  else: pred.append(0)
print(pred)

import cv2 
import tensorflow as tf
import numpy as np
import os

categories = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
store_data = []


def prepare(image_path):
  img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  if(img is None):
    raise ValueError("Image not found or unable to load")
  
  img_resized = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
  
  img_normalized = img_resized / 255.0

  return img_normalized.reshape(-1, 28, 28, 1)

model = tf.keras.models.load_model('sudoku_02.h5')

for i in os.listdir("DIGIT"):
  prediction = model.predict([prepare(f'DIGIT/{i}')])
  s = np.argmax(prediction)
  store_data.append(s)

int_array = np.array(store_data, dtype=int).tolist()

sudoku_grid = np.array(int_array).reshape(9,9)

print(sudoku_grid)

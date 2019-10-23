import cv2
import os
import numpy as np
from PIL import Image
from data import facedetect
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root, file)
			label = os.path.basename(root).replace(" ", "-").lower()
			#print(label, path)
			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1
			id_ = label_ids[label]
			#print(label_ids)
			#y_labels.append(label) # some number
			#x_train.append(path) # verify this image, turn into a NUMPY arrray, GRAY
			pil_image = Image.open(path).convert("L") # grayscale
			size = (550, 550)
			final_image = pil_image.resize(size, Image.ANTIALIAS)
			image_array = np.array(final_image, "uint8")
			face, confidence = facedetect.detect_face(final_image)
			for idx, f in enumerate(face):
				box = (f[1], f[2], f[3], f[0])
				boxes.append(box)
			encodings = facedetect.face_encodings(rgb, boxes)

			for (x,y,w,h) in faces:
				roi = image_array[y:y+h, x:x+w]
				x_train.append(roi)
				y_labels.append(id_)


#print(y_labels)
#print(x_train)

with open("pickles/face-labels.pickle", 'wb') as f:
	pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("recognizers/face-trainner.yml")
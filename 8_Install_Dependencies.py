import glob

import numpy as np
from torch.nn import Sequential

cv2 = "New_Zealand_Boat.png"
filename = "coins-2.jpg"
img = "New_Zealand_Boat2.png"
images = []
labels = []
for filename in glob.glob("dataset/pos/*"):
 img = cv2.resize(img, (256,256))
images.append(img)
labels.append(1)
for _ in range(3):
 img = cv2
images.append(img)
labels.append(1)
for filename in glob.glob("dataset/neg/*"):
 img = cv2.imread(filename)
img = cv2
images.append(img)
labels.append(0)
for _ in range(3):
 img = cv2
images.append(img)
labels.append(0)
images = np.array(images)
labels = np.array(labels)


def train_test_split():
    pass


train_test_split()


class Conv2D:
    pass


class MaxPooling2D:
    pass


class Dense:
    pass


model = Sequential()
# Training
class EarlyStopping:
    pass


earlystopping = EarlyStopping()
model.compile()


class X_train:
    pass


class X_test:
    pass


model({X_test})
model("penny.h5")


print(model)
print({X_test})
print("penny.h5")




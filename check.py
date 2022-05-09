import os
import shutil

root = "/Users/kcmorris/Downloads/ML-Interpretability-Evaluation-Benchmark-master/Image/PASCAL_VOC_2012/human_attention_mask/"
pascal2012 = "/Users/kcmorris/Downloads/VOCdevkit/VOC2012/TrainImages/"
pascal2012_test = "/Users/kcmorris/Downloads/VOCdevkit/VOC2012/TestImages/"
pascal2012_ann = "/Users/kcmorris/Downloads/VOCdevkit/VOC2012/AnnotationsTrain/"
pascal2012_test_ann = "/Users/kcmorris/Downloads/VOCdevkit/VOC2012/AnnotationsTest/"
attention_masks = "/Users/kcmorris/Downloads/VOCdevkit/VOC2012/HumanAttentionMasks/"

dataset = []
dataset_test = []

masks = []

ann_train = []
ann_test = []

train_idx = open("/Users/kcmorris/Downloads/VOCdevkit/VOC2012/train_idx.txt", "w")
test_idx = open("/Users/kcmorris/Downloads/VOCdevkit/VOC2012/test_idx.txt", "w")

for path, subdirs, files in os.walk(pascal2012):
	for name in files:
		dataset.append(name.split(".")[0])
		train_idx.write(name.split(".")[0]+"\n")

train_idx.close()

for path, subdirs, files in os.walk(pascal2012_test):
	for name in files:
		dataset_test.append(name.split(".")[0])
		test_idx.write(name.split(".")[0]+"\n")

test_idx.close()

for path, subdirs, files in os.walk(pascal2012_ann):
	for name in files:
		ann_train.append(name.split(".")[0])

for path, subdirs, files in os.walk(pascal2012_test_ann):
	for name in files:
		ann_test.append(name.split(".")[0])

for path, subdirs, files in os.walk(attention_masks):
	for name in files:
		masks.append(name.split(".")[0])


train_count = 0

with open("/Users/kcmorris/Downloads/VOCdevkit/VOC2012/train_idx.txt") as train_file: 
	for line in train_file:
		train_count +=1 


test_count = 0
with open("/Users/kcmorris/Downloads/VOCdevkit/VOC2012/test_idx.txt") as test_file:
	for line in test_file:
		test_count += 1

print("DIFFERENCE BETWEEN TRAIN SETS: ", str(list(set(dataset) - set(ann_train))))
print("DIFFERENCE BETWEEN TEST SETS: ", str(list(set(dataset_test) - set(ann_test))))
print("DIFFERENCE BETWEEN TEST SETS: ", str(list(set(dataset_test) - set(masks))))
print("TRAIN COUNT: ",str(train_count))
print("TEST COUNT: ", str(test_count))

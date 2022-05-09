import os
import shutil

root = "/Users/kcmorris/Downloads/ML-Interpretability-Evaluation-Benchmark-master/Image/PASCAL_VOC_2012/human_attention_mask/"
pascal2012 = "/Users/kcmorris/Downloads/VOCdevkit/VOC2012/TrainImages/"
pascal2012_test = "/Users/kcmorris/Downloads/VOCdevkit/VOC2012/TestImages/"
pascal2012_ann = "/Users/kcmorris/Downloads/VOCdevkit/VOC2012/AnnotationsTrain/"
pascal2012_test_ann = "/Users/kcmorris/Downloads/VOCdevkit/VOC2012/AnnotationsTest/"
attention_masks = "/Users/kcmorris/Downloads/VOCdevkit/VOC2012/HumanAttentionMasks/"
count = 0
bad = 0

dataset = []

for path, subdirs, files in os.walk(pascal2012):
	for name in files:
		dataset.append(name)

for path, subdirs, files in os.walk(root):
	for name in files:
		check = os.path.join(path, name)
		ann_name = name.split(".")[0]+".xml"
		if name == '.DS_Store':
			pass
		else:
			try:
				if name in dataset:
					src_path = pascal2012+name
					src_ann = pascal2012_ann+ann_name
					#copy file to test
					shutil.copy(src_path, pascal2012_test)
					shutil.copy(src_ann, pascal2012_test_ann)
					#remove from train
					os.remove(src_path)
					os.remove(src_ann)

				shutil.copy(check, attention_masks)
			except:
				print("COULD NOT COPY IMAGE: ", check)
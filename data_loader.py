import os
import nltk
import numpy as np
import tensorflow as tf
import pandas as pd

def load_dataset(dataset_path_train,word2idx):

	with open(dataset_path_train,'r') as file1:
		
		sentence_one = []
		sentence_two = []
		y_true = []

		max1 = 0
		max2 = 0

		for index, line in enumerate(file1):
			
			if index == 0:
				continue

			s_1 = []
			s_2 = []

			values = line.split("\t")
			
			#Sentence 1
			
			words = nltk.word_tokenize(values[3])
			words = [word.lower() for word in words]

			s_1.extend([word2idx.get(word,word2idx['UNK']) for word in words])

			#Sentence 2
			# words = values[4].split(" ")
			words = nltk.word_tokenize(values[4])
			words = [word.lower() for word in words]

			s_2.extend([word2idx.get(word,word2idx['UNK']) for word in words])
			

			if len(s_1) > max1:
				max1 = len(s_1)

			if len(s_2) > max2:
				max2 = len(s_2)

			y_true.append(np.asarray(values[0]))

			sentence_one.append(np.pad(s_1,(0,41-len(s_1)),'constant',constant_values=(0)))
			sentence_two.append(np.pad(s_2,(0,41-len(s_2)),'constant',constant_values=(0)))


			# self.sentence_one.append(np.asarray(s_1[0:self.sen_len]))
			# self.sentence_two.append(np.asarray(s_2[0:self.sen_len]))

	sentence_one = np.stack(sentence_one)
	sentence_two = np.stack(sentence_two)
	y_true = np.stack(y_true)

	#print self.weights

	print "Max_train:",max1,max2

	print sentence_one.shape,sentence_two.shape,y_true.shape
	
	

	return sentence_one,sentence_two,y_true


def load_dataset_test(dataset_path_test,word2idx):

	with open(dataset_path_test,'r') as file1:
		
		sentence_one_test = []
		sentence_two_test = []
		y_true_test = []

		max1 = 0
		max2 = 0

		for index, line in enumerate(file1):
			
			if index == 0:
				continue

			s_1 = []
			s_2 = []

			values = line.split("\t")
			
			#Sentence 1
			# words = values[3].split(" ")
			words = nltk.word_tokenize(values[3])
			words = [word.lower() for word in words]

			s_1.extend([word2idx.get(word,word2idx['UNK']) for word in words])

			#Sentence 2
			# words = values[4].split(" ")
			words = nltk.word_tokenize(values[4])
			words = [word.lower() for word in words]

			s_2.extend([word2idx.get(word,word2idx['UNK']) for word in words])
			
			if len(s_1) > max1:
				max1 = len(s_1)

			if len(s_2) > max2:
				max2 = len(s_2)


			y_true_test.append(np.asarray(values[0]))

			sentence_one_test.append(np.pad(s_1,(0,41-len(s_1)),'constant',constant_values=(0)))
			sentence_two_test.append(np.pad(s_2,(0,41-len(s_2)),'constant',constant_values=(0)))

			

	print "Max_test:",max1,max2

	sentence_one_test = np.stack(sentence_one_test)
	sentence_two_test = np.stack(sentence_two_test)
	y_true_test = np.stack(y_true_test)

	
	print sentence_one_test.shape,sentence_two_test.shape,y_true_test.shape

	return sentence_one_test,sentence_two_test,y_true_test
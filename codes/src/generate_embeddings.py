# author: Mohammad Minhazul Haq
# generate and save embeddings for all images

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import facenet
import os
import math
import pickle


def main(model, dataset):
    with tf.Graph().as_default():
        with tf.Session() as sess:
            # load the model
            facenet.load_model(model)

            # get input and output tensors
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

            image_size = 160
            embedding_size = embeddings.get_shape()[1]

            # generate person_list and image_paths
            persons = os.listdir(dataset)
            person_list = []
            image_paths = []

            for person in persons:
                if os.path.isdir(dataset + '/' + person):
                    images_batch = os.listdir(dataset + '/' + person)
                    for image in images_batch:
                        person_list.append(person)
                        image_paths.append(dataset + '/' + person + '/' + image)

            # save persons list by pickling
            with open("data/persons.txt", "wb") as fp:
                pickle.dump(person_list, fp)

            # run forward pass to calculate embeddings
            print('runnning forward pass on dataset images...')

            # compute embeddings for each of the given images
            total_images = len(image_paths)
            batch_size = 100
            total_batches = int(math.ceil(1.0 * total_images / batch_size))
            embedding_array = np.zeros((total_images, embedding_size))

            for i in range(total_batches):
                start_index = i * batch_size
                end_index = min((i + 1) * batch_size, total_images)
                image_paths_batch = image_paths[start_index : end_index]

                images_batch = facenet.load_data(image_paths_batch, False, False, image_size)
                feed_dict = {images_placeholder: images_batch, phase_train_placeholder: False}

                embedding_array[start_index:end_index, :] = sess.run(embeddings, feed_dict=feed_dict)

            # save embeddings to a file
            np.save('data/embedding_array.npy', embedding_array)
            print('embedding_array saved successfully...')


if __name__ == '__main__':
    saved_model_path = 'models/facenet/20170512-110547'
    dataset_path = 'datasets/lfw/lfw_mtcnnpy_160'

    main(saved_model_path, dataset_path)

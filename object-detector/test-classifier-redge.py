# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:45:13 2019

@author: Redge
"""

# Import the required modules
from sklearn.externals import joblib
import glob
import os
from config import *
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from skimage.io import imread
from skimage.feature import hog

if __name__ == "__main__":
    # Parse the command line arguments

    pos_feat_path =  '../data/features/pos'
    neg_feat_path = '../data/features/neg'

    # Classifiers supported
    clf_type ='LIN_SVM'

    fds = []
    labels = []
    # Load the positive features
    for feat_path in glob.glob(os.path.join(pos_feat_path,"*.feat")):
        fd = joblib.load(feat_path)
        fds.append(fd)
        labels.append(1)

    # Load the negative features
    for feat_path in glob.glob(os.path.join(neg_feat_path,"*.feat")):
        fd = joblib.load(feat_path)
        fds.append(fd)
        labels.append(0)

    from sklearn.svm import SVC
    if clf_type is "LIN_SVM":
        clf = SVC(kernel = 'linear', random_state = 0)
        print ("Training a Linear SVM Classifier")
        clf.fit(fds, labels)
        # If feature directories don't exist, create them
        if not os.path.isdir(os.path.split(model_path)[0]):
            os.makedirs(os.path.split(model_path)[0])
        joblib.dump(clf, model_path)
        print ("Classifier saved to {}".format(model_path))




if __name__ == "__main__":


#Extract HOG Features from Test images	
    des_type = "HOG"

    # If feature directories don't exist, create them
    if not os.path.isdir(tpos_feat_ph):
        os.makedirs(tpos_feat_ph)

    # If feature directories don't exist, create them
    if not os.path.isdir(tneg_feat_ph):
        os.makedirs(tneg_feat_ph)

    print ("Calculating the descriptors for the  positive test samples and saving them")
    for im_path in glob.glob(os.path.join(tpos_im_path, "*")):
        im = imread(im_path, as_grey=True)
        if des_type == "HOG":
            fd = hog(im,  orientations, pixels_per_cell, cells_per_block)
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(tpos_feat_ph, fd_name)
        joblib.dump(fd, fd_path)
    print ("Positive test features saved in {}".format(tpos_feat_ph))
    print ("Completed calculating features from test images")
    
    fd=[]
    
    print ("Calculating the descriptors for the  negetive test samples and saving them")
    for in_path in glob.glob(os.path.join(tneg_im_path, "*")):
        im = imread(in_path, as_grey=True)
        if des_type == "HOG":
            fd = hog(im,  orientations, pixels_per_cell, cells_per_block)
        fd_name = os.path.split(in_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(tneg_feat_ph, fd_name)
        joblib.dump(fd, fd_path)
    print ("Negetive test features saved in {}".format(tneg_feat_ph))
    print ("Completed calculating features from test images")

# Fit Features in Trained SVM Model 
    
    fds = []
    tlabels = []
    predict=[]
    # Load the positive features
    for feat_path in glob.glob(os.path.join(tpos_feat_ph,"*.feat")):
        fd = joblib.load(feat_path)
        fds.append(fd)
        tlabels.append(1)

    # Load the negative features
    for feat_path in glob.glob(os.path.join(tneg_feat_ph,"*.feat")):
        fd = joblib.load(feat_path)
        fds.append(fd)
        tlabels.append(0)

    print ("Testing a Linear SVM Classifier")
    predict = clf.predict(fds)
    cm = confusion_matrix(tlabels, predict)

    
    
    




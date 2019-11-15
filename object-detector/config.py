'''
Set the config variable.
'''


min_wdw_sz = [50, 20] # Changed refer to config file for ooriginal details. Confirm what values to be used here
step_siz = [10, 10]
orientations = 9
pixels_per_cell = [8, 8]
cells_per_block = [3, 3]
visualize = False
normalize = True
pos_feat_ph = "../data/features/pos" #Enter path for positive training features here
neg_feat_ph = "../data/features/neg"#Enter path for negetive training features here
model_path = "../data/models/svm.model" #Enter path for model to be saved here
threshold = .3


#Enter path for positive and negetive testing features here
tpos_feat_ph = "../data/features/testpos"
tneg_feat_ph = "C:/Users/Redge/Desktop/hog_svm_object_detect/data/features/testneg"

#Enter Path for positive and negetive training images here
pos_im_path = "C:/Users/Redge/Desktop/hog_svm_object_detect/ped"
neg_im_path = "C:/Users/Redge/Desktop/hog_svm_object_detect/nonped"


#Enter Path for positive and negetive test images here
tpos_im_path = "C:/Users/Redge/Desktop/hog_svm_object_detect/test/ped"
tneg_im_path = "C:/Users/Redge/Desktop/hog_svm_object_detect/test/nonped"

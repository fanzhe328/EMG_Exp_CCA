# *-* coding=utf-8 *-*
# !/usr/bin/python
'''
	classify_all_channel
	所有通道全部作为训练数据和测试数据
'''

import numpy as np
import os
import time
import data_load
import classifier
from preprocess import data_preprocess, data_normalize
# from data_plot import plot_result


root_path = os.getcwd()


def train_dataset_feature_intra(
        train_dir='train1', subject_list=['subject_1'], type='TD4',
        dataset='data1', fold_pre='250_100', z_score=False, chan_num=2, channel_pos_list=['O']):
    # my_clfs = ["LDA", "SVC_linear", "SVC_rbf", "Logistic", "QDA", "GaussianNB"]
    # my_clfs = ["LDA", "QDA", "GaussianNB", "SVC_linear", "SVC_rbf", "Logistic"]

    my_clfs = ["LDA"]

    start_time = time.time()
    for sub in subject_list:
        trains, classes = data_load.load_feature_dataset(train_dir, sub)
        if z_score:
            trains = data_normalize(trains)
            sub = 'norm_' + sub
        # print trains.mean(axis=0), trains.std(axis=0)
        # sys.exit(0)
        # for 
        classifier.training_lda_TD4(
            my_clfs, trains, classes, log_fold=fold_pre + '/' + type + '_' + dataset + '_' + sub, channel_pos='O', num=1)
#
    # classifier.training_lda_TD4_cross(my_clfs, trains1, classes1, trains2, classes2, log_fold = 'TD4_data4_'+subject+'_1to2', num=1)
    # classifier.training_lda_TD4_cross(my_clfs, trains2, classes2, trains1, classes1, log_fold = 'TD4_data4_'+subject+'_2to1', num=1)
    print "Total times: ", time.time() - start_time, 's'


def train_dataset_signal():
    my_clfs = ["LDA"]
    # subject = 'subject_1'
    subject_list = ['subject_' + str(i) for i in range(1, 2)]
    # trains, classes = load_feature_dataset('train1', 'subject_1')

    # trains1, classes1, trains2, classes2 = load_feature_dataset('train4', subject)
    # print trains.shape, classes.shape

    start_time = time.time()

    for sub in subject_list:
        trains, classes = load_signal_dataset('train1', sub)
        print trains.shape, classes.shape
        classifier.training_lda_signal(
            my_clfs, trains, classes, log_fold='signal_data1_' + sub, num=1)

    # classifier.training_lda_TD4_cross(my_clfs, trains1, classes1, trains2, classes2, log_fold = 'TD4_data4_'+subject+'_1to2', num=1)
    # classifier.training_lda_TD4_cross(my_clfs, trains2, classes2, trains1, classes1, log_fold = 'TD4_data4_'+subject+'_2to1', num=1)
    print "Total times: ", time.time() - start_time, 's'


def main():
    pass

if __name__ == '__main__':
    winsize = 200
    incsize = 100
    samrate = 1024
    fold_pre = str(winsize) + '_' + str(incsize)
    feature_type = 'TD4'

    z_score = False
    chan_num = 2

    train_dir = 'train1_' + fold_pre
    input_dir = 'data1'
    subject_list = ['subject_' + str(i) for i in range(1, 3)]
    channel_pos_list = [ 'O',								# 中心位置
    	'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',		# 八方位 1cm 模拟：右，右下，下，左下，左，左上，上，右上
    	'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2']		# 八方位 2cm 模拟：同上

    for idx, channel_pos in enumerate(channel_pos_list):
    	print idx, channel_pos
    # data_preprocess(
    #     input_dir, train_dir, feature_type,
    #     subject_list, winsize, incsize, samrate)

    # z_score = False
    # train_dataset_feature_intra(
    #     train_dir, subject_list, feature_type,
    #     input_dir, fold_pre, z_score, chan_num， channel_pos_list)

    # z_score = True
    # train_dataset_feature_intra(train_dir, subject_list,
    # feature_type, input_dir, fold_pre, z_score, chan_num)

    # train_dir = 'train4_' + fold_pre
    # input_dir = 'data4'
    # subject_list = ['subject_' + str(i) for i in range(1, 6)]
    # chan_num = 4

    # data_preprocess(input_dir, train_dir, feature_type, \
    # subject_list, winsize, incsize, samrate)
    # z_score = False
    # train_dataset_feature(train_dir, subject_list,
    #                       feature_type, input_dir, fold_pre, z_score)
    # z_score = True
    # train_dataset_feature(train_dir, subject_list,
    #                       feature_type, input_dir, fold_pre, z_score)
    # train_dataset_signal()

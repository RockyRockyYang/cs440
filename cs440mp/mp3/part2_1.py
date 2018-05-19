import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
from import_data import import_train_data, import_test_data
from import_data import import_train_data2
from naive_bayes import train, test, evaluation, output_result, run
from feature_map import feature_map_part1_1, feature_map_part1_2
import itertools

(train_yes_data, train_yes_label) = import_train_data("audiodata/yes_train.txt", "audiodata/yes_train_label.txt")
(test_yes_data, test_yes_label) = import_test_data("audiodata/yes_test.txt", "audiodata/yes_test_label.txt")
(train_no_data, train_no_label) = import_train_data("audiodata/no_train.txt", "audiodata/no_train_label.txt")
(test_no_data, test_no_label) = import_test_data("audiodata/no_test.txt", "audiodata/no_test_label.txt")

def run_part2_audio(k):
    print("================AUDIO - BINARY FEATURE================")
    print("Importing data...")
    
    train_audio_dataset = ( np.concatenate((train_yes_data, train_no_data)), np.concatenate((train_yes_label, train_no_label)) )
    test_audio_dataset = ( np.concatenate((test_yes_data, test_no_data)), np.concatenate((test_yes_label, test_no_label)) )

    train_dataset = feature_map_part1_1(train_audio_dataset, {' ': 1, '%': 0}, (25, 10), 2)
    test_dataset = feature_map_part1_1(test_audio_dataset, {' ': 1, '%': 0}, (25, 10), 2)
    
    run(k, train_dataset, test_dataset)    
    print("=====================================================\n")

run_part2_audio(3.0)


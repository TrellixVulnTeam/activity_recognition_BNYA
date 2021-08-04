import matplotlib.pyplot as plt


def make_confusion_matrix(cf,
                          group_names=None,
                          categories='auto',
                          count=True,
                          percent=True,
                          cbar=True,
                          xyticks=True,
                          xyplotlabels=True,
                          sum_stats=True,
                          figsize=None,
                          cmap='Blues',
                          title=None):
    '''
    This function will make a pretty plot of an sklearn Confusion Matrix cm using a Seaborn heatmap visualization.
    Arguments
    ---------
    cf:            confusion matrix to be passed in
    group_names:   List of strings that represent the labels row by row to be shown in each square.
    categories:    List of strings containing the categories to be displayed on the x,y axis. Default is 'auto'
    count:         If True, show the raw number in the confusion matrix. Default is True.
    normalize:     If True, show the proportions for each category. Default is True.
    cbar:          If True, show the color bar. The cbar values are based off the values in the confusion matrix.
                   Default is True.
    xyticks:       If True, show x and y ticks. Default is True.
    xyplotlabels:  If True, show 'True Label' and 'Predicted Label' on the figure. Default is True.
    sum_stats:     If True, display summary statistics below the figure. Default is True.
    figsize:       Tuple representing the figure size. Default will be the matplotlib rcParams value.
    cmap:          Colormap of the values displayed from matplotlib.pyplot.cm. Default is 'Blues'
                   See http://matplotlib.org/examples/color/colormaps_reference.html

    title:         Title for the heatmap. Default is None.
    '''

    # CODE TO GENERATE TEXT INSIDE EACH SQUARE
    blanks = ['' for i in range(cf.size)]

    if group_names and len(group_names) == cf.size:
        group_labels = ["{}\n".format(value) for value in group_names]
    else:
        group_labels = blanks

    if count:
        group_counts = ["{0:0.0f}\n".format(value) for value in cf.flatten()]
    else:
        group_counts = blanks

    if percent:
        row_sum = np.sum(cf, axis=1)
        cf_row_sum = np.array([[value] * len(row_sum) for value in row_sum]).flatten()
        #         print(cf_row_sum)
        group_percentages = ["{0:.2%}".format(value) for value in cf.flatten() / cf_row_sum]
    else:
        group_percentages = blanks

    box_labels = [f"{v1}{v2}{v3}".strip() for v1, v2, v3 in zip(group_labels, group_counts, group_percentages)]
    box_labels = np.asarray(box_labels).reshape(cf.shape[0], cf.shape[1])

    # CODE TO GENERATE SUMMARY STATISTICS & TEXT FOR SUMMARY STATS
    if sum_stats:
        # Accuracy is sum of diagonal divided by total observations
        accuracy = np.trace(cf) / float(np.sum(cf))

        # if it is a binary confusion matrix, show some more stats
        if len(cf) == 2:
            # Metrics for Binary Confusion Matrices
            precision = cf[1, 1] / sum(cf[:, 1])
            recall = cf[1, 1] / sum(cf[1, :])
            f1_score = 2 * precision * recall / (precision + recall)
            stats_text = "\n\nAccuracy={:0.3f}\nPrecision={:0.3f}\nRecall={:0.3f}\nF1 Score={:0.3f}".format(
                accuracy, precision, recall, f1_score)
        else:
            stats_text = "\n\nAccuracy={:0.3f}".format(accuracy)
    else:
        stats_text = ""

    # SET FIGURE PARAMETERS ACCORDING TO OTHER ARGUMENTS
    if figsize == None:
        # Get default figure size if not set
        figsize = plt.rcParams.get('figure.figsize')

    if xyticks == False:
        # Do not show categories if xyticks is False
        categories = False

    # MAKE THE HEATMAP VISUALIZATION
    plt.figure(figsize=figsize)
    sns.heatmap(cf / np.sum(cf, axis=1), annot=box_labels, fmt="", cmap=cmap, cbar=cbar, xticklabels=categories,
                yticklabels=categories)

    if xyplotlabels:
        plt.ylabel('True label')
        plt.xlabel('Predicted label' + stats_text)
    else:
        plt.xlabel(stats_text)

    if title:
        plt.title(title)


make_confusion_matrix(cm, group_names=[''])

in_file = 'data/data-clean/refrigerator/no_interaction/2/no_interaction_10_1614039254_1.mp4'

#
# flg = False
# if flg:
#     import os
#     cmd = 'python3.7 feature_extraction.py --video_list data/video.txt  --network vgg --framework tensorflow --output_path out/ --tf_model ./slim/vgg_16.ckpt'
#     # eval(cmd)
#     os.system(cmd)

import numpy as np

# f = 'out/play_music_1_1615410036_1_vgg.npy'
# f = 'out/ask_time_1_1614904536_1_vgg.npy'
fs = [  # 'out/camera2_mkv/ask_weather_4_1616183946_2_vgg.npy',
    'out/data_20210625/camera1_mp4/ask_time_1_1614904536_1_vgg.npy',  # ( my results by CNN)
]
fs2 = [
    'out/uChicago/20210625/output_mp4/ask_time_1_1614904536_1_vgg.npy', '(jinjin results by cnn (avg))'
    # 'out/uChicago/20210630/output_mp4/ask_time_1_1614904536_1_vgg.npy',
    # 'out/output_mkv/ask_time_1_1614904536_2_vgg.npy',
    # 'out/output_mkv/ask_time_1_1614904536_2_vgg.npy',
]
for f1, f2 in zip(fs, fs2):
    print('\n')
    print(f1)
    data = np.load(f1)
    print(data.shape)
    n, d = data.shape
    print(data)
    # average
    data = np.sum(data, axis=0)
    # print(data/d)
    print(data / n)  # average
    # for i in range(len(data)):
    #     print(f'frame_{i+1}: {data[i, :]}')
    # print(data/sum(data))
    # a = np.quantile(data/sum(data), [0, 0.1, 0.5, 0.9, 1])

    print(f2)
    data = np.load(f2)
    print(data.shape)
    print(data)
    # b = np.quantile(data, [0, 0.1, 0.5, 0.9, 1])
    # print(b)
    # print([v2/v1 for v1, v2 in zip(a, b)])

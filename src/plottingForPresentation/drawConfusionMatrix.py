# -*- coding: utf-8 -*-


from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

# import some data to play with

file_handle = open("/home/skhokhar/workspace/finalHMMintegratingWorkFromHome/finalHMM_atHome/rsc/resultsFolder/resultsAtDist[-15]", "r")
file_text = file_handle.read()
file_line_list = file_text.split("\n")
y_test = []
y_pred = []
for i in file_line_list:
    if len(i) == 0:
        continue
    numeric_line = i.split(",")    
    y_test.append(int(numeric_line[0]))
    y_pred.append(int(numeric_line[1]))

cm = confusion_matrix(y_test, y_pred)

print(cm)

# Show confusion matrix in a separate window
plt.matshow(cm)
plt.title('Confusion matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()
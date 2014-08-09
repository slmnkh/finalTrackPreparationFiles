python /home/skhokhar/workspace/trackPreparation/src/svm/collect_road_features_from_texts.py

./svm-scale -l -1 -u 1 -s ~/workspace/trackPreparation/src/svm/scale_range ~/workspace/trackPreparation/src/svm/training_svm.txt > ~/workspace/trackPreparation/src/svm/training_svm.scale

./svm-scale -r ~/workspace/trackPreparation/src/svm/scale_range ~/workspace/trackPreparation/src/svm/testing_svm.txt > ~/workspace/trackPreparation/src/svm/testing_svm.scale



./svm-train -s 1 -t 1 -b 1 ~/workspace/trackPreparation/src/svm/training_svm.scale 



./svm-predict -b 1 ~/workspace/trackPreparation/src/svm/testing_svm.scale training_svm.scale.model ~/workspace/trackPreparation/src/svm/prediction.output


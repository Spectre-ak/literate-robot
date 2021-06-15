# literate-robot

#### Application using the model is available at https://literate-robot.azurewebsites.net/ and refer to [app](https://github.com/Spectre-ak/literate-robot/tree/main/app)

#### A model which is trained on detecting obstacles from a cleaning robot Point Of View (POV).

1. Training Notebook: [literate_robot.ipynb](https://colab.research.google.com/drive/1wMAVb21JKEOi11FrCKrOkdAox7XIyVJC?usp=sharing)
2. Test Notebook: [literate-robot-model-test.ipynb](https://colab.research.google.com/drive/141ngYZT8YGBsAk1O_JAZyLvNxT31OkTx?usp=sharing)
3. Predictions: [literate-robot/PredictedResults](https://github.com/Spectre-ak/literate-robot/tree/main/PredictedResults)
4. saved_model: [frozen_inference_graph.pb](https://github.com/Spectre-ak/literate-robot/blob/main/graphs/frozen_inference_graph.pb)
5. labelmap: [labelmap.pbtxt](https://github.com/Spectre-ak/literate-robot/blob/main/graphs/labelmap.pbtxt)
6. Labelling tool: [LabelImg](https://tzutalin.github.io/labelImg/)

Detected classes represents following
1. fr = furniture(legs/polls)
2. dr = doors
3. cb = cables/wires
4. gr = small garments 


Model used: [faster_rcnn_inception_v2_coco](http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz) from Tensorflow 1

Trained using Tensorflow [object detection API](https://github.com/Spectre-ak/models)

Predictions

![](https://github.com/Spectre-ak/literate-robot/blob/main/PredictedResults/Images/predcited_IMG_20210606_175342.jpg)

![](https://github.com/Spectre-ak/literate-robot/blob/main/PredictedResults/Images/predcited_Grand%20Theft%20Auto%20V%202021-06-07%2014-09-53.mp4%20-%20PotPlayer%206_7_2021%205_45_24%20PM.jpg)


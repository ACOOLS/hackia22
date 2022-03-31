# Fire
## Introduction
During the first challenge we had to develop a model able to detect wild fire from video footage. This problem is different in several ways:
1. The detection must now focus on urban fires
2. The model should be really fast and light because the inference will be in real time
The model developed during the first challenge with the best results was based on VGG16 and weighed around 140 MB. Because
1. We didn't know how much we could shrink this size to fit in the Jetson Xavier very limited memory,
2. The other problems involved locating objects
3. The allowed time for developing the model was very short
We decided to (try to) do a joint development with Yolo.
## Development
In the quest for the best fire localization model, I came accross the [YoloV5](https://github.com/ultralytics/yolov5) implementation.
The features offered such as nice performance, small footprint, ability to export multi-format models were very compelling, so I decided to give it a try.
# Trainings
TODO
The YoloV5 implementation gives the ability to publish the training results in real time with very interesting [figures](https://wandb.ai/winners-hackia22/fireyolo5/reports/Real-time-urban-fires-localization--VmlldzoxNzY4MDIw?accessToken=vmq82d86cxw7wkbv18tjrmenrt40ob39uz796j7opzf352b7g82a6cx9u124ii98).
The import of YoloV5m based model into Jetson Xavier compatible format was problematic: possible with vanilla pretrained models, not with retrained ones.
Trained a Darknet YoloV4 model with precision as good as Yolov5
Tried a localy exported model and observed a perceptible decrease of precision (video x)
Trained a model based on the YoloV5s and exported it to ONNX format but had no time enough to import it in to the Jetson
## Conclusion

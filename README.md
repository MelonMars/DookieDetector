# DookieDetector:
DookieDetector is a novel AI, which is able to identify two different distinct types of dookie in an image. It can identify something as either Elk or Dog. The Dog class was trained slolely on dog feces, however it is also capable of identifying bull and such crap, as they have similar excrements. Elk was trained on, and can identify, elk, deer, goose, and mouse scat. 

Project structure:
The VOCdevkit is the dataset, in a Pascal VOC format, ready for possible training on the jetson-inference, as per the [tutorial by dusty-nv](https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-ssd.md)

The rest is pretty simple, as all you need to do to train it yourself is download the labeled dataset, and then run `padding.py`, which makes every image the same shape, in order to allow pytorch to better understand it, and to prevent bias I think. 

Installation:

Download the code
Install detectnet from [jetson-inference](https://github.com/dusty-nv/jetson-inference)
VOCdevkit should contain the dataset. There may be a couple trivial errors to work out (ex. Some entries in the testtrain.txt and val.txt might correspond to non-existent xml/jpg files, just delete the entries)

With detectnet installed, run one of the following:

`detectnet --model=<onnx_path> –labels=<label_path> --input-blob=input_0 --output-cvg=scores –output-bbox=boxes –confidence=0.5 <file_to_analalyze> <outputfile.jpg>`

for testing one image, or alternatively for camera input:

`detectnet –model=<onnx_path> --labels=<label_path> --input-blo=input_0 –output-cvg=scores –output-bbox=boxes –confidence=0.5 /dev/video0`

`/dev/video0` may not work, and you may have to use `csi://0`. Feel free to modify the confidence, it is represented as a decimal percent (i.e. .5 = 50% confidence)

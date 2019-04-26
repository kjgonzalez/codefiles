# Using a Modified Point Net to Generate 3D Bounding Box Proposals with Stereo Disparity Map (Thesis)
Author: Kristian Gonzalez

---

### Working Topic:
Creating 3D bounding boxes from a modified pointnet with stereo data.
### Problem: 
There are many sensors available to detect objects, but how competitive are stereo cameras?
### Idea: 
Stereo vision cameras are relatively cheap and emulate human senses when driving. They can even address some issues that lidar has with reflective surfaces and point cloud density. 
### Objective: 
Demonstrate how competitive stereo vision can be by combining multiple networks including PSMNet (a CNN-based disparity map estimation method) and FPNet (a pointnet-based 3D localization method)

### General Procedure:
1. modify psmnet to generate estimates from a stereo pair
2. be able to generate point cloud from disparity map
3. modify fpnet to accept stereo-generated pointcloud data
4. collect results

### Performance Metric
Compare mAP of 3D bb's against current state of the art stereo methods. may also want to consider items such as: 
1. time complexity / speed
2. recall, precision

### Tasks to Complete

| Description  | Status |
| ---          | ---    |
| download / configure psmnet (disparity estimation) | completed Apr01 (?)
| modify psmnet to output like a function | completed Apr 01 (?)
| disparity-to-PointCloud conversion ability | (still not fully complete, Apr 26)
| download / configure fpointnet | completed Apr10
| modify pointnet to accept self-trained model | completed Apr21
| modify pointnet to accept self-preprocessed data | completed Apr25


### General Timeline
```
* Apr01: Start of Project
* May10: Scientific Paper draft for Elser?
* May20: Thesis first draft review
* Jul29: Thesis second draft review
* Aug26: Thesis submission & presentation 
```

---
## KJG QUICKNOTES: 

#### `= 190426 ================================`
Have made a great deal of progress so far, but need to do so much more. need to rethink whether `190321` writing below is still relevant. also, will make this document less about the contents of the paper and more of an "info desk" about the paper.

#### `= 190321 ================================`
may want to rethink a little bit: why exactly are you moving everything into pointcloud data? what if you considered keeping the structure of the stereo data, but still transformed the single-layer disparity map into a 3-layer x/y/z map? must also consider how to compare with a lidar scan and get some estimate of "error".

towards comparing error: perhaps for every lidar point, get closest stereo xyz point and get sum of squared errors? or just 2norm distance error?
recall error formula: err=(estimate-true)/true

---
## Miscellaneous

### How to Install TeXstudio on Linux:
(instructions untested)
1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo apt-get install texstudio

### How to Install TeXstudio on Windows:
(to be added)
1. ensure miktex already installed (?)
2. go to WebsiteHere
3. download install file
4. install, enable as many packages as necessary
5. ensure 




---

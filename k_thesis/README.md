# KJG Thesis
Working Topic: creating 3D bounding boxes from a modified pointnet with stereo data.
Working Title: Tradeoff Comparison between Stereo and Lidar Depth Estimation in 3D Object Detection
Author: Kristian Gonzalez
Problem: There are many sensors available to detect objects, but which are truly necessary for "good" detection performance?
Goal: Want to detect 3D objects with stereo data. will try using a pointnet, but feed a stereo generated pointcloud. reasoning: stereo data is 2.5D data, but in reality is a denser, less precise set of coordinate points that must be tranformed into the physical space rather than the disparity space. 
Objective: Find a dataset / network that can take disparity maps and generate 3D bb proposals.
Procedure:
1. modify psmnet to generate estimates from a stereo pair
2. be able to generate point cloud from disparity map
3. modify fpnet to accept stereo-generated pointcloud data
4. collect results
Metric: compare mAP of 3D bb's against current state of the art stereo methods.

## KJG QUICKNOTES: 
= 190321 =====================
may want to rethink a little bit: why exactly are you moving everything into pointcloud data? what if you considered keeping the structure of the stereo data, but still transformed the single-layer disparity map into a 3-layer x/y/z map? must also consider how to compare with a lidar scan and get some estimate of "error".

towards comparing error: perhaps for every lidar point, get closest stereo xyz point and get sum of squared errors? or just 2norm distance error?
recall error formula: err=(estimate-true)/true


## How to Install TeXstudio on Linux:
(instructions untested)
1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo apt-get install texstudio

## How to Install TeXstudio on Windows:
(to be added)
1. go to WebsiteHere
2. download install file
3. install, enable as many packages as necessary
4. miktex?



--eof--

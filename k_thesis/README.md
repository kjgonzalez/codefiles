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


### General Timeline
```
* Apr01: Start of Project
* May10: Scientific Paper draft for Elser?
* May20: Thesis first draft review
* Jul29: Thesis second draft review
* Aug26: Thesis submission & presentation 
```

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


---

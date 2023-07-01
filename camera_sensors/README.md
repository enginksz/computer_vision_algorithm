## Sensors (zed , realsense, oak-d cameras)
_SensorPy_ is a collection of sensor wrappers written in Python. It does not aim to include every sensor but to provide convenient (easy-to-use) interfaces for sensors used. The sensor interface was inspired by OpenCV `cv::VideoCapture`.

-----------------------
camera_calibration
-----------------------
Geometric camera calibration, also referred to as camera resectioning, estimates the parameters of a lens and image sensor of an image or video camera. You can use these parameters to correct for lens distortion, measure the size of an object in world units, or determine the location of the camera in the scene. These tasks are used in applications such as machine vision to detect and measure objects. They are also used in robotics, for navigation systems, and 3-D scene reconstruction.

python3 ....py

-----------------------
realsense-camera
-----------------------
Installing the packages:

--Register the server's public key: sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE In case the public key still cannot be retrieved, check and specify proxy settings: export http_proxy="http://:" , and rerun the command. See additional methods in the following link.

--Add the server to the list of repositories: sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u

--Install the libraries (see section below if upgrading packages): sudo apt-get install librealsense2-dkms sudo apt-get install librealsense2-utils

The above two lines will deploy librealsense2 udev rules, build and activate kernel modules, runtime library and executable demos and tools.

--Optionally install the developer and debug packages: sudo apt-get install librealsense2-dev sudo apt-get install librealsense2-dbg With dev package installed, you can compile an application with librealsense using g++ -std=c++11 filename.cpp -lrealsense2 or an IDE of your choice.

Reconnect the Intel RealSense depth camera and run: realsense-viewer to verify the installation.

Verify that the kernel is updated : modinfo uvcvideo | grep "version:" should include realsense string

sudo apt-get update

the;

python3 realsense_camera.py

-----------------------
oak-d camera
-----------------------
reference;

https://learnopencv.com/object-detection-with-depth-measurement-with-oak-d/

modifi python3 oak-d_camera.py


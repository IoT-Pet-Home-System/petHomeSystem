# module observe

## Module observer

### class Request
- **description**: An object with a message and the user who sent it

### class Observer

```python
def reSet(self, push)
```
- **input**: Redefining mPush
- **output**: Initialize request list
- **description**: Initializes the request list stored in the PI

```python
def run(self)
```
- **description**: Perform a loop on the observer thread

```python
def insertRQ(self, user, msg)
```
- **input**: Message and User who sent it
- **output**: User's message insert into request list
- **description**: A function that inserts a message from a user into a list

```python
def popRQ(self)
```
- **output**: First element of request list
- **description**: It pulls out the first entry in the list of user requests.

## Module Vi

### class Vi

```python
def optFlow(self, frame. prvs. hsv)
```
- **input**: frame(frame), prvs(frame), hsv
- **output**: prvs(frame), new hsv, bgr(frame)
- **description**: Detection of Moving Objects in an Image Using the Dense Optical Flow of OpenCV

```python
def getCenterOfContour(self, image)
```
- **input**: Optical flow image
- **output**: Insert center points into optical flow image
- **description**: Use the optflow () to retrieve the center point of the contour by acquiring the contour in the detected image.
   
```python
def capture(self)
```
- **output**: Generate current frame as 'model name' + '.PNG' file
- **description**: Creates an image file in png format with model name.

```python
def signalHandler(self, signum, frame)
```
- **description**: Safe shutdown function to be performed on signal
   
```python
def register_all_signal(self)
```
- **description**: Performs a signalHandler on all signals.
   
```python
def modeFinder(self, list)
```
- **input**: A collection of areas where pets are found(list)
- **description**: Sorts the values in the list in descending order by frequency and returns a new list containing the frequencies.
   
```python
def areaDetection(self, x, y)
```
- **input**: Center point
- **description**: Function to find the position of a center point in a partition of an image
   
```python
def petTracking(self)
```
- **description**: Using the above functions, periodically observe the movements of animals and give an alarm if they are not visible for a given time.


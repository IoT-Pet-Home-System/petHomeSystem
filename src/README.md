# **Module Description**

## Module server

### class MobileSystem

```python
def parshResponseByNL(self, res)
```

  - **input**: res
 
```python
def parshResponseBySP(self, res)
```

```python
def loadSerail(self)
 ```
 
```python
def bootUp(self)
 ```
 
```python
def getRequest(self, wating)
```
 
```python
def runMobile(self)
```
 
 
## Module push

### class Push

```python
def setUpObserverList(self)
```
 
```python
def setUpThread(self)
```
 
```python
def insertMSG(self, user, str)
```
 
```python
def getMSG(self)
```
 
```python
def startTh(self)
```

## Module observer

### class Request

### class Observer

```python
def reSet(self, push)
```

```python
def run(self, push)
```

```python
def insertRQ(self, user, msg)
```

```python
def popRQ(self)
```

## Module Vi

### class Vi

```python
def optFlow(self, frame. prvs. hsv)
```
- input: frame(frame), prvs(frame), hsv
- outpu: prvs(frame), new hsv, bgr(frame)
- description: Detection of Moving Objects in an Image Using the Dense Optical Flow of OpenCV

```python
def getCenterOfContour(self, image)
```
- input: optical flow image
- output: insert center points into optical flow image
- description: Use the optflow () to retrieve the center point of the contour by acquiring the contour in the detected image.
   
```python
def capture(self)
```
- output: Generate current frame as 'model name' + '.PNG' file
- description: Creates an image file in png format with model name.

```python
def signalHandler(self, signum, frame)
```
- description: Safe shutdown function to be performed on signal
   
```python
def register_all_signal(self)
```
- description: Performs a signalHandler on all signals.
   
```python
def modeFinder(self, list)
```
- input: A collection of areas where pets are found(list)
- description: Sorts the values in the list in descending order by frequency and returns a new list containing the frequencies.
   
```python
def areaDetection(self, x, y)
```
- input: center point
- description: Function to find the position of a center point in a partition of an image
   
```python
def petTracking(self)
```
- description: Using the above functions, periodically observe the movements of animals and give an alarm if they are not visible for a given time.

## Module Translator

### class Translator

```python
def getIMAG_URL(self, user)
```

```python
def getPostBodyMessage(self, user, text)
```

```python
def sendMsg(self, url, user, msg)
```

```python
def pushToUser(self, user, msg)
```

```python
def pushToAllUser(self, msg)
```

```python
def pushImage(self, user, path)
```

### Module FeedOperation

   The class that drives the feed motor

### Module DoorOpeartion

   The class that drives the door motor

## Module push

### class Push

```python
def setUpObserverList(self)
```
- **description**: Preparing to use observer list

```python
def setUpThread(self)
```
- **description**: Insert observer list elements into thread list

```python
def insertMSG(self, user, str)
```
- **input**: User and message to send to user
- **description**: Create a request object with arguments and insert the object into queue

```python
def getMSG(self)
```
- **output**: the first object element in queue
- **description**: Fetch a request object from queue

```python
def startTh(self)
```
- **description**: Perform threads of thread list

## Module Translator

### class Translator
```python
def sendOpPush(self, user, operation_list)
```
- **input**: user and command List
- **description**: Encodes users and commands in json format and posts them

```python
def getIMAG_URL(self, user)
```
- **input**: User
- **output**: Image adress of user
- **description**: extract Image adress of user

```python
def getPostBodyMessage(self, user, text)
```
- **input**: user and text content
- **output**: message of json type
- **description**: Return a json-type message containing user and text content

```python
def sendMsg(self, url, user, msg)
```
- **input**: Information of the user to receive the message and contents of the message
- **description**: Transfer message to user

```python
def pushToUser(self, user, msg)
```
- **input**: message and user
- **description**: Transfer message to user using sendMsg function

```python
def pushToAllUser(self, msg)
```
- **input**: message
- **description**: Transfer message to all user using pushToUser

```python
def pushImage(self, user, path)
```
- **input**: User and path of image
- **description**: Transfer image to user 


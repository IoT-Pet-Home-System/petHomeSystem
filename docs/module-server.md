# **Main module**

## Module server

### class PetHome

```python
def parshResponseByNL(self, res)
```
- **input**: Response message
- **output**: Separate response messages by lines and remove spaces
- **description**: Separates strings entered as arguments by line and removes whitespace
 
```python
def parshResponseBySP(self, res)
```
- **input**: Response message
- **output**: Remove response message spaces
- **description**: Removes whitespace from string as arguments

```python
def loadSerail(self)
 ```
- **description**: Load serial number from text file

```python
def bootUp(self)
 ```
- **description**: Store the information obtained during the user registration process

```python
def getRequest(self, wating)
```
- **input**: Delay
- **output**: User's request list
- **description**: Parses user requests into lists and returns them

```python
def runPetHome(self)
```
- **description**: PI's main server function for operating the pet home system



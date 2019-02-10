## Celeste

### Addressing [See Our Sun](https://github.com/amnh/HackTheSolarSystem/wiki/See-Our-Sun)

### Created by Solar Express
* Joshua Learn - jjrylearn
* Megan Learn - learnmp
* Joe Tatusko - joetats
* Ian Anderson - andersis
* Put your name and github handle

### Solution Description

Our goal was to build an extension of the Helioviewer API to allow multiple images of the sun to be downloaded with their metadata for use in OpenSpace.

We acheived this by building a Flask webserver that accepts a date range and a telescope source ID. This generates a list of calls to the Helioviewer API which collects the images and metadata into a zip file to be placed in the correct OpenSpace directory.

The project includes a web frontend to facilitate access to the data.

### Installation Instructions

Clone the repo into a folder and run 

```pip install -r requirements.txt```

Then begin the server by calling 

```python app.py```

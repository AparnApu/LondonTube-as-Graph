# LondonTube-as-Graph


## Table of Contents

- [Introduction](#Introduction)
- [Motivation](#Motivation)
- [Working](#Working)
- [Contributions](#Contributions)
- [Acknowledgments](#Acknowledgments)

<!-- toc -->


## Introduction
This program plots the London Tube system as a graph. It also plots and highlights the shortest path between two given stations using networkx.

## Motivation
I undertook studying python after my Grade 12 final exams and this was the first major project I did! 
Having studied JAVA for the last four years of high school, I was blown away by the simplicity of the programming style in python!
I was inspired by Mark Dunne's 'The London Tube as a Graph' and decided to write my own code for plotting the very elaborate train system. 
The whole project was a great way to learn pandas, dictionaries, networkx and basic plotting.


## Working
The basic idea behind this is that the stations become nodes and the connections become edges. 
The line names/ time of commute become edge details while the coordinates of the stations(latitude/ longitude) become node details.
To run the code, you can either fork it (link: (https://github.com/AparnApu/LondonTube-as-Graph/fork) or click the clone/ download button to download the zip file.
Run the file 'tubeGraph_starter.py'. I have already included two test cases (lines 46 - 57) which you can modify.
There are no packages to install.

### Code snippet to modify:

```
# test case 1

StationFrom = "Chesham"
StationTo = "Morden"

# test case 2

#StationFrom = "Chesham"
#StationTo = "Epping"
```

![](LondonTube_Images/LondonTubeImg1.png) 
|:--:| 
| ***Graph of whole London Tube system*** |

![](LondonTube_Images/LondonTubeImg2.png)
|:--:| 
| ***Graph of the highlighted shortest path (pictured: path from Chesham to Morden with the connecting lines)*** |



## Contributions
Open to contributions!
Fork the repo, edit it and commit your change.


## Acknowledgments
I must acknowledge @MarkDunne (http://markdunne.github.io/2016/04/10/The-London-Tube-as-a-Graph/) for the idea and @nicola (https://github.com/nicola/tubemaps) for providing the databases.

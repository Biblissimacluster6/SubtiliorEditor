# SubtiliorEditor
SubtiliorEditor is a Python program that enhances MEI encoding and Verovio output for the atypical notations characteristic of ars subtilior (late 14th century). 

![code](https://github.com/Biblissimacluster6/SubtiliorEditor/blob/main/img/Decorum.png)

## English documentation

### What exactly does SubtiliorEditor do?

SubtiliorEditor is a Python program for improving the encoding (MEI) and visualisation (SVG) of certain atypical musical notations encountered during the 14th century. While most of the figures concerned are borrowed from ars subtilior sources (such as Modena A), SubtiliorEditor can also provide practical solutions for encoding early pieces with dragmae or semibreves caudatae (also called semibrevis maior). 

### How do I use it?

SubtiliorEditor is both a syntax and a tool. It assists the encoder in a number of ways. It relieves the encoder of the perilous MEI encoding of the "caudatae" - some forms of which are illustrated in the table below. While MEI allows the shape of each note to be encoded precisely (via the <stem> element), this is done at the cost of a fairly long encoding process. With SubtiliorEditor, all you have to do is specify the values shown in the reference table in @dur, making sure of course that you also enter the duration and pitch of the note, or any other relevant information. 

![code](https://github.com/Biblissimacluster6/SubtiliorEditor/blob/main/img/subtilior%20editor%20table.jpg)

In addition to these new values for @dur, three other solutions are proposed for @colored, namely 'hollowed', 'red' or 'red and hollowed'. Once the MEI file has been encoded according to these conventions, simply load it into SubtiliorEditor using the command line below in your terminal. To do this, you need to clone this directory on your machine and ensure that the following modules are installed in the directory or environment you are using: argparse, xml.etree.ElementTree, verovio and bs4.

Python SubtiliorEditor.py Path_to_my_MEI_file/My_MEI_file.mei

SubtiliorEditor does several things. First, it generates a correct MEI file (accurateMEI.xml) in the directory where SubtiliorEditor is located. This file follows conventional encoding rules and describes the precise shape of each caudata using the <stem> element and its various attributes. The colouring attributes are also replaced by values recognised in the official schema, although these are often ambiguous in this context. In addition, SubtiliorEditor generates an SVG file (subtilior.svg), from Verovio, enriched with new symbols to visualise the most complex figures! For the moment, SubtiliorEditor supports the notes shown in the table below. Other forms and syntaxes will be published shortly. The following example shows the SVG projection of Senleches' famous ballad 'En attendant esperance' (cantus) generated using SubtiliorEditor. Of course, anyone can also improve the fonts in the Font folder by manipulating the associated xml definitions.

![code](https://github.com/Biblissimacluster6/SubtiliorEditor/blob/main/img/En%20attendant%20esperance%202.jpg)

You can also test SubtilioEditor with the corresponding MEI file in the demo file.

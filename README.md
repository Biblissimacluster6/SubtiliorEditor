# SubtiliorEditor

<img src="https://github.com/Biblissimacluster6/DIAMMtoIIIF/blob/main/img/biblissima-baseline-sombre-france2030.png" width="400"><img src="https://github.com/Biblissimacluster6/DIAMMtoIIIF/blob/main/img/Icon.jpg" width="400">

<img src="https://github.com/Biblissimacluster6/SubtiliorEditor/blob/main/img/Logo%20Musica2.jpg" width="200">

SubtiliorEditor is a Python program that enhances MEI encoding and Verovio output for the atypical notations characteristic of ars subtilior (late 14th century). It is the result of a collaboration between Biblissima+ Cluster 6 and the working group MEI (WG1) of the Musica2 consortium (Huma-Num). 

![code](https://github.com/Biblissimacluster6/SubtiliorEditor/blob/main/img/Decorum.png)

## English documentation

### What exactly does SubtiliorEditor do?

SubtiliorEditor is a Python program for improving the encoding (MEI) and visualisation (SVG) of certain atypical musical notations encountered during the 14th century. While most of the figures concerned are borrowed from ars subtilior sources (such as Modena A), SubtiliorEditor can also provide practical solutions for encoding early pieces with dragmae or semibreves caudatae (also called semibrevis maior). 

### How do I use it?

SubtiliorEditor is both a vocabulary and a tool. It assists the encoder in a number of ways. It relieves the encoder of the perilous MEI encoding of the "caudatae" - some forms of which are illustrated in the table below. While MEI allows the shape of each note to be encoded precisely (via the <stem> element), this is done at the cost of a fairly long encoding process. With SubtiliorEditor, all you have to do is specify the values shown in the reference table in @dur, making sure of course that you also enter the duration and pitch of the note, or any other relevant information. 

![code](https://github.com/Biblissimacluster6/SubtiliorEditor/blob/main/img/subtilior%20editor%20table.jpg)

In addition to these new values for @dur, three other solutions are proposed for @colored, namely 'hollowed', 'red' or 'red and hollowed'. As a result, the value of @colored is no longer Boolean, contrary to the official MEI schema. Once the MEI file has been encoded according to these conventions, simply load it into SubtiliorEditor using the command line below in your terminal. To do this, you need to clone this directory on your machine and ensure that the following Python modules are installed in the directory or environment you are using: argparse, xml.etree.ElementTree, verovio and bs4.

Python SubtiliorEditor.py Path_to_my_MEI_file/My_MEI_file.mei

SubtiliorEditor does several things. First, it generates a correct MEI file (accurateMEI.xml) in the directory where SubtiliorEditor is located. This file follows conventional encoding rules and describes the precise shape of each caudata using in particular the <stem> element and its various attributes. The colouring attributes are also replaced by values recognised in the official schema, although these are often ambiguous in this context (for <note>, @colored becomes Boolean again). In addition, SubtiliorEditor generates an SVG file (subtilior.svg), from Verovio, enriched with new symbols to visualise the most complex figures! For the moment, SubtiliorEditor supports the notes shown in the table below. Other forms and syntaxes will be published shortly. The following example shows the SVG projection of Senleches' famous ballad 'En attendant esperance' (cantus) generated using SubtiliorEditor. Of course, anyone can also improve the fonts in the Font folder by manipulating the associated xml definitions.

![code](https://github.com/Biblissimacluster6/SubtiliorEditor/blob/main/img/En%20attendant%20esperance%202.jpg)

You can also test SubtilioEditor with the corresponding MEI file in the demo file.

### How can I ensure that SubtiliorEditor is working properly?

In addition to the technical prerequisites, it is necessary to respect the spelling of the values provided in the table above for the figurae. Make sure you do not misspell these values. The easiest way to do this is to work with an existing MEI file, encoded using the "mensural" module, and make the appropriate changes using a code editor (search/replace function). The grammar proposed is deliberately simplistic so that complex figures can be encoded quickly. SubtiliorEditor will generate the conventional MEI file automatically. Make sure you clone the entire directory so that the SubtilioEditor.py script is in the same directory as the Font folder. If you intervene in the SVG definition of the symbols, make sure not to rename the xml files. Similarly, each MEI element must have an @xml:id. If your file does not have xml identifiers, you can automatically generate them using the Mei-Friend web application.

## French documentation

### Que fait exactement SubtiliorEditor ?

SubtiliorEditor est un programme Python permettant d’améliorer l’encodage MEI et la visualisation SVG de certaines notations musicales atypiques rencontrées au cours du XIVe siècle. Si la plupart des figures concernées sont empruntées aux sources de l’ars subtilior (comme Modena A), SubtiliorEditor peut également apporter des solutions pratiques pour l’encodage de pièces plus anciennes disposant de dragmae ou de semibreves caudatae (ou semibrevis maior). 

### Comment l'utiliser ?

SubtiliorEditor est à la fois un vocabulaire et un outil. Il assiste ainsi l’encodeur de différentes manières. Il le décharge d’un codage périlleux en MEI des notes caudatae dont quelques formes sont illustrées dans le tableau ci-dessus. Si la MEI permet d’encoder précisément la forme de chaque note (via notamment l’élément <stem>), cela se fait au prix d’un encodage assez long. Avec SubtiliorEditor, il suffit de spécifier dans @dur les valeurs indiquées dans le tableau de référence (ci-dessus), tout en veillant évidemment à renseigner également la durée et la hauteur des notes, ou toute autre information pertinente. En plus de ces nouvelles valeurs pour @dur, trois autres solutions sont proposées pour l'attribut @colored (coloration), à savoir « hollowed », « red » ou « red and hollowed ». Dès lors, la valeur de @colored n'est donc plus booléenne, contrairement au schéma MEI officiel. Une fois le fichier MEI encoder suivant ces conventions, il suffit de le charger dans SubtiliorEditor grâce à la ligne de commande ci-dessous dans votre terminal. Il est nécessaire pour cela de cloner ce répertoire dans votre machine et de veiller à ce que, dans le répertoire ou l’environnement que vous utilisez, les modules Python suivants soient installés : argparse, xml.etree.ElementTree, verovio et bs4.

Python SubtiliorEditor.py Chemin_ver_mon_fichier_MEI/Mon_fichier.mei

SubtiliorEditor fait plusieurs choses. D’une part, il génère un fichier MEI correct (accurateMEI.xml) dans le répertoire où se trouve SubtiliorEditor. Ce fichier répond aux règles d’encodage conventionnelles et décrit la forme précise de chaque caudata à l’aide de l’élément <stem> et de ses divers attributs. Les attributs de coloration sont également remplacés par des valeurs reconnues dans le schéma officiel, bien que celles-ci s’avèrent dans ce contexte souvent ambiguës (pour <note>, l'attribut @colored redevient par exemple booléen). En outre, SubtiliorEditor génère un fichier SVG (subtilior.svg), à partir de Verovio, enrichi de nouveaux symboles afin de visualiser les figures les plus complexes! Pour l’instant, SubtiliorEditor prend en charge les notes représentées dans le tableau ci-dessous. D’autres formes et syntaxes seront prochainement publiées. L’exemple suivant montre la projection SVG de la célèbre ballade « En attendant esperance » (cantus) de Senleches générée à l’aide de SubtiliorEditor. Bien entendu, chacun peut également améliorer les fonts présentes dans le dossier Font, en manipulant les définitions xml associé

Vous pouvez également tester SubtilioEditor avec le fichier MEI correspondant qui se trouve dans le fichier demo.

### Comment garantir le bon fonctionnement de SubtiliorEditor ?

Outre les prérequis techniques, il est nécessaire de respecter la graphie des valeurs fournies dans le tableau ci-dessus pour les figurae. Il faut ainsi veiller à ne pas mal orthographier ces valeurs. Le plus facile reste d’intervenir dans un fichier MEI déjà existant, encodé suivant le module « mensural », et y effectuer les modifications adéquates via un éditeur de code (fonction rechercher/remplacer). La grammaire proposée est volontairement simpliste afin d’encoder rapidement des figures complexes. SubtiliorEditor se charge de générer le fichier MEI conventionnel automatiquement. Veillez également à bien cloner tout le répertoire pour que le script SubtilioEditor.py se trouve dans le même répertoire que le dossier Font. Si vous intervenez dans la définition SVG des symboles, veillez à ne pas renommer les fichiers xml. De même, chaque élément MEI doit disposer d’un @xml:id. Si votre fichier est dépourvu d'identifiants xml, vous pouvez automatiquement en générer en utilisant l’application web Mei-Friend.

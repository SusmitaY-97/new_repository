extract_text_from_image module provide following functionality
1. It helps to extract text from an image and stores the result into file

#################################################################
Below packages are need to be installed before module to be used
#################################################################
1. pytesseract
steps to install
   
1. pip3 install pytesseract

#################################################################
Below application need to be installed
#################################################################
1. tesseract (application)
#################################################################
steps to install 
1. click on the below link
   
https://digi.bib.uni-mannheim.de/tesseract/
2. Select any executable according to your machine for example w32 or w64
3. Download it
4. install it

use below link for additional information
https://medium.com/quantrium-tech/installing-and-using-tesseract-4-on-windows-10-4f7930313f82#:~:text=Select%20the%20directory%20where%20you%20want%20to%20install,installed%20Tesseract%20on%20your%20machine.%20This%20is%20important.

###########
How to run
###########
Before running you need to modify run configuration
1. Run extract_text_from_image.py
2. Provide image name or path, initial, extension for file with space separated
or
1. goto your terminal
2. use below command
python extract_text_from_image.py image.jpg JSON .json
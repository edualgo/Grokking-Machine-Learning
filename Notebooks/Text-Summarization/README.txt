### <ins>About<ins>

  Text Summarizer written from scratch, based on the **extraction** algorithm. It extracts the important sentences from any type of text i.e articles, blog, pdf, story etc.
Need to run the script with the input file path having the text for summarization, it will output the summarized text to the default file (named empty_file.txt).
  
  You may extract any numbers of prioritise sentences by providing thresold value from the command line (default is 1.0).
  
  For increasing the summarized text **decrease** thresold value from 1.0 to 0.0.
  
  For decreasing the summarized text **increse** thresold value from 1.0 to >1.0.
 
 
 ### <ins>Default prarameters<ins>
 
|   Variable<ins> | <ins>Required<ins>| <ins>Default<ins>|
|--------------------|------------------|-------------------|
| -i or --input      | Yes              | empty_file.txt  |
| -o or --output     | No               | empty_file.txt  |
| -t or --thresold   | No               | 1.0             |
    
 
 ### <ins>Example<ins>
  - for help run this command `python summarize.py --help`
  
  ![alt text](https://github.com/Rohit-bisht-rise/datascience-mashup/blob/Rohit-bisht-rise-patch-1/Text%20Summarization/images/help.png)
  
  - for summarizing run this command `python summarize.py -i <input_file_path> -o <output_file_path> -t <thresold>`
  
    Example command: `python summarize.py -i file.txt -t 0.95`
  
  ![alt text](https://github.com/Rohit-bisht-rise/datascience-mashup/blob/Rohit-bisht-rise-patch-1/Text%20Summarization/images/run.png)
  
  - deafalt run by only giving input file name or path
    command `python summarize.py -i file.txt`
   
  ![alt text](https://github.com/Rohit-bisht-rise/datascience-mashup/blob/Rohit-bisht-rise-patch-1/Text%20Summarization/images/rundefault.png)
    
  
### <ins>ERROR<ins>
  
  **Errors you may find while running**
  - if you try to run without giving input file name or path
    command `python summarize.py`
    
  ![alt text](https://github.com/Rohit-bisht-rise/datascience-mashup/blob/Rohit-bisht-rise-patch-1/Text%20Summarization/images/inputfile.png)
 
  - if you give input file name the default i.e empty_file.txt
    command `python summarize.py -i empty_file.txt`
    
  ![alt text](https://github.com/Rohit-bisht-rise/datascience-mashup/blob/Rohit-bisht-rise-patch-1/Text%20Summarization/images/samefile.png)
  
### <ins>Clone<ins>

  1. clone the repository **Text Summarization** or download the summarize.py
  2. create an empty file name **empty_file.txt**
  3. run the above command
  4. change the thresold according to your intereset
  5. get the output in the output file
  

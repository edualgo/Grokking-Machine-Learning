# Sentimental-Anaylysis
A basic python script for understanding working behind SA algo

# How to use
|**STEPS** | **Working**|
|----------|------------|
|**step 1** | clone the repo|
|**step 2** | install nltk libary command `pip3 install nltk`|
|**step 3** | copy the text into *read.txt* file|
|**step 4** | run the script if useing cmd, then command is `python3 sentimental.py`|

# Algorithm 
1. getting text of any article or blog
2. making word ready for the tokenizing
   - removing special characters
   - converting into lowercase
   - conerting **\n** to space
3. Tokenizing
4. having the dictornary of emotional words
   - getting it into main file
5. Steps in this case:
   - for each tokenize word check is it emotinal words
   - if yes add emotion of this word it into list of emotions
6. get the frequency of different emotion from the emotinal list
7. plotting the bar graph showing the exact frequency of each emotion
8. Using SentimentIntensityAnalyzer for score
   - importing nltk 
     command : `from nltk.sentiment.vader import SentimentIntensityAnalyzer`
   - calculating differnt sentinal score i.e positive, negative, neutral

# A plot for the Steve Jobs' 2005 Stanford Commencement Address
![sentimentGraph](https://github.com/Rohit-bisht-rise/Sentimental-Analysis/blob/main/sentimentGraph.png)


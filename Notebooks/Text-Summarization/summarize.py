# importing required modules
import argparse

stop_words = {'i', 'with', 'he', 'down', 'itself', 'm', 'shan', 'no', 'yourself', 'but', 'the', 'y', 'again', 'more', 'o', "she's", 'theirs', 'my', "isn't", 'are', 're', 'their', 'own', 'during', 'don', 'such', 'me', "you'll", 'have', 'has', 'an', 'isn', 'wouldn', 'between', 'just', 'this', 'himself', 'very', 'further', 'by', 'doing', 'so', "it's", "won't", 'out', 'not', 'ours', 'didn', 'on', 'were', 'that', 's', 'which', "don't", 'll', 'nor', "needn't", 'some', 'above', 'any', "shouldn't", "hadn't", "mightn't", 'needn', 'after', 'ourselves', 'a', "didn't", 'hers', 'until', "that'll", 'once', 'mustn', 'mightn', 'hadn', 'in', 'being', 'few', 'or', "doesn't", 't', 'been', "wasn't", 'can', 'themselves', 'up', 'to', 'it', 'for', 'had', 'haven', 'am', 'through', 'she', 'too', 'herself', 'than', 'as', 'yourselves', 'before', 'and', 'because', 'where', 'doesn', 'weren', 'under', 'whom', 'same', 'ain', 'was', 'should', 'there', 'hasn', 'shouldn', 'off', 'other', 'couldn', 'at', 'those', 'over', 'myself', "hasn't", 'your', 'be', 'do', 'why', 'does', 'below', "you've", 'd', 'aren', 'who', "should've", "mustn't", 'from', 'of', 've', "haven't", 'will', 'its', 'what', 'did', 'won', 'yours', 'you', 'him', 'if', 'each', 'both', 'while', 'how', 'they', 'about', 'we', "you'd", 'most', "couldn't", "weren't", "you're", 'here', 'wasn', 'all', 'them', 'now', "shan't", 'against', 'ma', "wouldn't", 'his', 'is', 'then', 'only', 'when', 'having', "aren't", 'into', 'these', 'our', 'her'}

def word_tokenize(text_string) -> list:
    '''
    tokenize the text_string into individuals words
    :param text_string: string
    :return words: list of string
    '''
    words = text_string.split(' ')
    words = [word.strip(' ').strip('.').strip(',').strip('"').lower() for word in words]
    return words

def sent_tokenize(text_string) -> list:
    '''
    tokenize the text_string into individuals sentences
    :param text_string: string
    :return sent: list of string
    '''
    sent = text_string.split('.')
    sent = [s.strip(' ') for s in sent]
    return sent[:-1]


def _create_frequency_table(text_string) -> dict:
    '''
    creates frequency table for words
    :param text_string: string
    :return frequency_table: dict
    '''
    # from global stop words
    global stop_words
    words = word_tokenize(text_string)
    # # Reducing words to their root form
    # Creating dictionary for the word frequency table
    frequency_table = dict()
    for wd in words:
        if wd in stop_words:
            continue
        if wd in frequency_table:
            frequency_table[wd] += 1
        else:
            frequency_table[wd] = 1
    return frequency_table


def _calculate_sentence_scores(sentences, words_frequency) -> dict:
    '''
    calculates average score for each sentences
    :param sentences: list
    :param words_frequency: dict
    :return sentence_weight: dict
    '''
    sentence_weight = dict()
    for sentence in sentences:
        sentence_wordcount_without_stop_words = 0
        for word in words_frequency:
              if word in sentence.lower():
                    sentence_wordcount_without_stop_words += 1
                    if sentence[:7] in sentence_weight:
                        sentence_weight[sentence[:7]] += words_frequency[word]
                    else:
                        sentence_weight[sentence[:7]] = words_frequency[word]

        sentence_weight[sentence[:7]] = sentence_weight[sentence[:7]] / sentence_wordcount_without_stop_words
    return sentence_weight


def _calculate_average_weight(sentence_weight) -> float:
    '''
    calculate average weight
    :param sentence_weight: dict
    :return: float
    '''
    weight_sum = 0
    for s_w in sentence_weight:
        weight_sum += sentence_weight[s_w]
    
    try:
        average = weight_sum / len(sentence_weight)
    except:
        average = 0
    return average


def _get_article_summary(sentences, sentence_weight, threshold):
    '''
    create summary for output
    :param sentences: list
    :param sentence_weight: dict
    :param threshold: float
    :return:
    '''
    sentence_counter = 0
    article_summary = ''
    for sentence in sentences:
        if sentence[:7] in sentence_weight and sentence_weight[sentence[:7]] >= (threshold):
            article_summary += " "+ sentence+ "."
            sentence_counter += 1
    return article_summary


class textSummarizer:
    def __init__(self, i_filename, o_filename, thres):
        self.o_filename = o_filename
        self.thresold = thres
        with open(i_filename, 'r') as f:
            self.text_string = f.read()
            f.close()

    def _process(self):
        self.sentences = sent_tokenize(self.text_string)
        self.frequency_table = _create_frequency_table(self.text_string)
        self.sentence_weight = _calculate_sentence_scores(self.sentences, self.frequency_table)
        self.average_weight = _calculate_average_weight(self.sentence_weight)

    def _summary(self):
        self.thresold = self.average_weight * self.thresold
        print(f'thresold = {self.thresold}')
        print(f'average = {self.average_weight}')
        summary = _get_article_summary(self.sentences, self.sentence_weight, self.thresold)
        with open(self.o_filename, 'w') as f:
            f.write(summary)
            f.close()


def summary_parse():
    summary_parser = argparse.ArgumentParser(
        add_help = True,
        prog = 'Text Summarizer',
        usage = 'python summarize.py -i <input_file_path> -o <output_file_path> -t <thresold>',
        description = 'A basic text summarization script from scratch',
        epilog = 'Example: python summarize.py -i file1.txt -o file2.txt -t 1.2'
    )
    summary_parser.add_argument('--input', '-i', required=True, type=str, dest='inp', default='empty_file.txt',
                                help = '--input | -i  <input_file path>: text is stored before'
                                )
    summary_parser.add_argument('--output', '-o', required=False, type=str, dest='out', default='empty_file.txt',
                                help = '--output | -o  <output_file path>: text will be stored after'
                                )
    summary_parser.add_argument('--thresold', '-t', required=False, type=float, dest='thres', default=1.0, 
                                help = '--thresold | -t <thresold>: it will be multiplied with average'
                                )
    return summary_parser.parse_args()


if __name__ == '__main__':
    args = summary_parse()
    if(args.inp == args.out):
        print('ERROR: cannot summarize content of same file to itself')
        print('       input and output file name should be differnt')
        exit(1)
    summarizer = textSummarizer(args.inp, args.out, args.thres)
    summarizer._process()
    summarizer._summary()
    print(f'\nDONE: {args.inp} summarized to {args.out}')

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer




def generate_summary_lexrank(text, max_number_of_characters):

    #instantiate LexRank summarizer
    summarizer_lex = LexRankSummarizer()


    if max_number_of_characters < 1:
    	max_number_of_characters = 1200
    
    
    final_summary = ''
    
    if text.strip()=="":
        #print(basename + '\x1b[31m EMPTY!\x1b[0m')
        return ""
    
    try:
        #if the text is larger the minimum doc size, take the beginning and the end and run the summarization algorithm only on those parts
        summary_limit = 10000 if len(text) > 15000 else len(text)
        text_for_summary = text[2000:summary_limit] + text[-2000:]
        
        #initialize the parser and tokenizer, and the LexRank summarizer, and then create a summary of 15 sentences
        parser = PlaintextParser.from_string(text_for_summary,Tokenizer("english"))
        summary= summarizer_lex(parser.document, 15)
        
        #remove sentences that are too long, too short or probably contain references
        sentences = [sentence for i,sentence in enumerate(summary) if ((len(str(sentence)) > 35) 
                                                                              & (' . ' not in str(sentence))
                                                                              & ('...' not in str(sentence))
                                                                              & (sum(c.isdigit() for c in str(sentence)) < len(str(sentence))/8)
                                                                              & (len(str(sentence)) < 400)
                                                                              & ('http' not in str(sentence))
                                                                              & ('www' not in str(sentence))
                                                                              & ('source' not in str(sentence).lower())
                                                                              & ('table' not in str(sentence).lower())
                                                                              & ('figure' not in str(sentence).lower())
                                                                              & ('appendi' not in str(sentence).lower())
                                                                              & ('annex' not in str(sentence).lower())
                                                                              & ('issn' not in str(sentence).lower())
                                                                              & ('box' not in str(sentence).lower())
                                                                              & ('(p.' not in str(sentence).lower())
                                                                              & ('tel.' not in str(sentence).lower())
                                                                              & ('...' not in str(sentence).lower())
                                                                              & ('  ' not in str(sentence).lower())
                                                                              & ('see' not in str(sentence).lower()))]
  

        #if the summary doesn't contain enough sentences, do it again, but discard more characters from the front
        if len(sentences) < 5:
            summary_limit = 50000 if len(text) > 100000 else len(text)
            text_for_summary = text[30000:summary_limit]# + text[-2000:]
            parser = PlaintextParser.from_string(text_for_summary,Tokenizer("english"))
            summary= summarizer_lex(parser.document, 20)
            sentences = [sentence for i,sentence in enumerate(summary)]
            #print('discarded sentences: ', sentences)
            #print('-------------------------------------------')
            
        #if the summary still doesn't contain enough sentences, do it again, but without cleaning up the list of sentences to return raw summary      
        if len(sentences) < 5:
            parser = PlaintextParser.from_string(text,Tokenizer("english"))
            summary= summarizer_lex(parser.document, 20)
            sentences = [sentence for i,sentence in enumerate(summary)]

        #start building the summary by adding sentences until the summary exceeds the length limit
        no_of_chars = 0
               
        for i, sentence in enumerate(sentences):
            if no_of_chars < max_number_of_characters: #1200:
                final_summary += str(sentence)
                #print(str(sentence))
                i += 1
                no_of_chars += len(str(sentence))   
                #print(no_of_chars)

        #summary = summarize(text,word_count=300)
        #print(basename + '\x1b[32m OK\x1b[0m')

    except Exception as e:
        #print (e)
        final_summary = "error"
        #print(basename + '\x1b[31m ERROR!\x1b[0m ' +str(e) )
    
    return final_summary

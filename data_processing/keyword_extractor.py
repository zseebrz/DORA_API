import yake


def yake_extractor(text, number_of_keywords):
    """
    Uses YAKE to extract the top 25 bigram keywords from a text
    Arguments: text (str)
    Returns: list of keywords (list)
    """
    
    #Initialise yake
    language = "en"
    max_ngram_size = 3
    deduplication_thresold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    if number_of_keywords == 0:
    	numOfKeywords = 20
    else:
    	numOfKeywords = number_of_keywords

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    
    keywords = custom_kw_extractor.extract_keywords(text)
    
    results = []
    for scored_keywords in keywords:
        for keyword in scored_keywords:
            if isinstance(keyword, str):
                results.append(keyword)
    return results
     

def extract_keywords(text, number_of_keywords):
    
    enrichments = []   
    # Use KeyBERT to extract keywords
    if len(text.strip()) > 20: # Text has to have a minimum length
	# For each keyword (keyword, score)
    	try:         
    	    kw_list = yake_extractor(text, number_of_keywords)
    	    #we don't need to deal with duplicate detection, as it is already implemented in the algorithm itself
    	    #kw_1gram_list = list(set([words for segments in kw_list for words in segments.split()]))
    	    #kw_1_2gram_list = kw_list + kw_1gram_list
    
    	    #for kw in kw_1_2gram_list:
    	    for kw in kw_list:
        		enrichments.append({'feature_type': 'keyword',
        		                    'feature': kw})
    	except Exception as e:
    	    enrichments.append({'feature_type': 'keyword',
    		                'feature': 'error: '+str(e)})
    return  enrichments

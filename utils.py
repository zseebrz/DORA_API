from response import *
#from data_processing.text_preprocessing import *
from data_processing.lexrank_summary import generate_summary_lexrank
#from data_processing.eurovoc_classifier import generate_eurovoc_classifications
from data_processing.keyword_extractor import extract_keywords
from data_processing.pdf_title_extractor import extract_title

response_obj = ResponseData()


def test():
	response_obj.set_status(200)
	response_obj.set_content("ECA NLP API")

	return response_obj.get_response()

def summarize_text(text_content, max_number_of_characters):

	summary = generate_summary_lexrank(text_content, max_number_of_characters)

	response_obj.set_status(200)
	response_obj.set_content(summary)

	return response_obj.get_response()
    
    
def eurovoc_classification(text_content):

	eurovoc_classification_results = extract_keywords(text_content, 5)

	response_obj.set_status(200)
	response_obj.set_content(eurovoc_classification_results)

	return response_obj.get_response()
 
 
def keyword_extraction(text_content, max_number_of_keywords):

	keyword_extraction_results = extract_keywords(text_content, max_number_of_keywords)

	response_obj.set_status(200)
	response_obj.set_content(keyword_extraction_results)

	return response_obj.get_response()
        

def title_extraction(pdf_file):

	title_extraction_results = extract_title(pdf_file)

	response_obj.set_status(200)
	response_obj.set_content(title_extraction_results)

	return response_obj.get_response()

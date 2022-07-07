from main import app
from schemas import Text_data
from utils import test, summarize_text, eurovoc_classification, keyword_extraction, title_extraction
from fastapi import File, UploadFile

@app.get('/')
async def index():
    data = test()

    return data


@app.post('/api/v1/summarize')
async def summarize_text_data(payload: Text_data):
    text_content = payload.text
    #num_words = payload.num_words
    #num_sentences = payload.num_sentences
    #num_characters = payload.num_characters
    max_number_of_characters = payload.num_characters
    text_summary = summarize_text(text_content, max_number_of_characters)

    return text_summary

@app.post('/api/v1/eurovoc')
async def eurovoc_classification_data(payload: Text_data):
    text_content = payload.text
    classification = eurovoc_classification(text_content)

    return classification

@app.post('/api/v1/title')
async def title_detection_data(file: UploadFile = File(...)):
    file_object = file.file
    title = title_extraction(file_object)

    return title

@app.post('/api/v1/keywords')
async def keyword_extraction_data(payload: Text_data):
    text_content = payload.text
    max_number_of_keywords = payload.num_words
    keyword_list = keyword_extraction(text_content, max_number_of_keywords)

    return keyword_list


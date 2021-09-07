import os
import pandas as pd
import spacy
from spacy import displacy
# import streamlit.components.v1 as components
# from IPython.core.display import display, HTML



path_to_files = os.path.abspath('./data/transcriptions')

def open_txt_file(path:str) ->str: 
    with open(path) as f:
        lines = f.readlines()
    return lines[0]

def read_file(path_to_files, chapter):
	"""
	chapter: number of episode 1 to ...
	"""
	files = os.listdir(path_to_files)
	try:
		text = open_txt_file(path_to_files+'/'+'episode_'+chapter+'.txt')
		print(path_to_files+'/'+'episode_'+chapter+'.txt')
		return text
	except:
		return 'Episode not available in database'

	
def render_text(text, language):
	
	"""Language: 'en_core_web_sm'
				'fr_core_news_sm'
	"""

	nlp_spacy = spacy.load(language)
	
	# .pipe() method for batch processing on large text
	# doc = list(nlp_spacy.pipe(text))
	doc = nlp_spacy(text)
	#displacy.render(doc, style="ent", jupyter = True)
	html = displacy.render(doc, style="ent", page =True)

	return html


def tagging_text(text, language):
    nlp = spacy.load(language)
    doc = nlp(text)
    df = pd.DataFrame({'text':[],'lemma':[],'tag':[]})
    
    #List for saving results
    tokens = []
    lemmatization = []
    tags = []
    entity= []
    
    #Tagging
    for token in doc:
        tokens.append(token.text)
        lemmatization.append(token.lemma_)
        tags.append(token.tag_)
        entity.append(token.ent_type_)

	#[See more token attributes](https://spacy.io/api/token#attributes)
        
    # Saving on dataframe and dropping duplicates
    df = pd.DataFrame({'text':tokens,'lemma':lemmatization,'tag':tags, 'entity':entity})
    df = df.drop_duplicates(subset=['text'])
    return df
    




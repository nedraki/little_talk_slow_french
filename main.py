import os 
import pandas as pd
import spacy
from spacy import displacy
import streamlit as st
import streamlit.components.v1 as components
from IPython.core.display import display, HTML
import reader as rd

# [theme]
# base="light"

### Selector:

mark_title = st.empty()
my_title = mark_title.title('Podcast transcriptions')
mark_sub = st.empty()
my_subheader = mark_sub.subheader("Little talk in slow french")


## Sidebar selection options:

sidebar_title = st.sidebar.title("Little talk in small french")
my_sidebar = st.sidebar.markdown("by Naguisse")

select_chapter = st.sidebar.number_input("Episode number" , step=1)
select_task = st.sidebar.selectbox('I want to:',['Read transcriptions', 'Explore Vocabulary'])



# Reading files and dataframe:
path_to_files = os.path.abspath('./data/transcriptions')
df = pd.read_csv(os.path.abspath('./data/dataframe.csv'), index_col='number_episode')
text = rd.read_file(path_to_files, str(int(select_chapter)))

## Dataframe with episode's names: 
chapter_name = df['episode'][select_chapter]
my_title = mark_title.title(chapter_name)

if select_task == 'Read transcriptions':
	
	# Options to get transcription: 
	select = st.sidebar.selectbox('Options', ['Transcription',
											'Transcription with annotations',
											'Vocabulary'])

	if select == 'Transcription':
		transcription = st.write(text)
	
	if select == 'Transcription with annotations':
		transcription_spacy = rd.render_text(text, 'fr_core_news_sm')
		components.html(transcription_spacy, width = 800, height = len(text)) ## how to get ideal len ?



if select_task == 'Explore Vocabulary':
	df_vocabulary = rd.tagging_text(text,"fr_core_news_sm")
	vocabulary_options = ['VERB','PROPN','PRON','NOUN','ADJ','ADV']
	select_vocabulary = st.sidebar.selectbox('Vocabulary', vocabulary_options)


	st.table( df_vocabulary[df_vocabulary['tag'] == select_vocabulary ] )
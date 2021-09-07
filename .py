import os

path_to_files = os.path.abspath('./data/transcriptions')
path_to_files

def open_txt_file(path:str) ->str: 
    with open(path) as f:
        lines = f.readlines()
    return lines[0]

def tagging_text(text, language):
    nlp = spacy.load(language)
    doc = nlp_fr(text)
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
        
    # Saving on dataframe and dropping duplicates
    df = pd.DataFrame({'text':tokens,'lemma':lemmatization,'tag':tags, 'entity':entity})
    df = df.drop_duplicates(subset=['text'])
    return df
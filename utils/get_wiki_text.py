#coding:utf-8


from gensim.corpora import WikiCorpus
from utils.config import Config

def get_text_from_wiki():
    config = Config()
    wiki_corpus = WikiCorpus(config.get_wiki_text_path, dictionary={})
    text_index = 0
    with open("./wiki_text/wiki_text.txt", 'w', encoding='utf-8') as output:
        for text in wiki_corpus.get_texts():
            output.write(' '.join(text) + '\n')
            text_index += 1
            if text_index % 1000 == 0:
                print('It had processed ' + str(text_index) + 'articles')

if __name__ == "__main__":
    get_text_from_wiki()

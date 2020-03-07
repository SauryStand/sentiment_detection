

# torch_learning_rate = 0.04
# torch_min_learning_rate = 0.001

class Config():
    def __init__(self):
        self.torch_learning_rate = 0.04
        self.torch_min_learning_rate = 0.001
        #win
        self.torch_bce_model = 'model/torch/pytorch_bce.model'
        self.word2vec_model = 'model/w2v/word2vec.model'
        self.dict_big_txt = 'D:\source_codes\python\Sentiment\sentiment_detection\data\dict\\tw\dict.txt.big'
        self.dict_my_dict = 'D:\source_codes\python\Sentiment\sentiment_detection\data\dict\\tw\my_dict'
        self.zh_dict_big_txt = 'D:\source_codes\python\Sentiment\sentiment_detection\data\dict\\zh\dict.txt.big'
        self.zh_dict_my_dict = 'D:\source_codes\python\Sentiment\sentiment_detection\data\dict\\zh\\categories\\my_dict_zh.txt'


        #mac



        #zh 字典
        self.zh_dict_txt_big = 'data/dict/zh/'
        self.zh_my_dict = 'data/dict/zh/'
        self.zh_categories = 'data/dict/zh/categories'


        self.tw_seg_txt = 'D:\source_codes\python\Sentiment\sentiment_detection\data\\f_wikidata\wiki_seg.txt'
        self.tw_wiki_txt = 'D:\source_codes\python\Sentiment\sentiment_detection\data\\f_wikidata\wiki_zh_tw.txt'


        self.zh_seg_txt = 'D:\source_codes\python\Sentiment\sentiment_detection\data\\f_wikidata\\wiki_seg_zh.txt'
        self.zh_wiki_txt = 'D:\source_codes\python\Sentiment\sentiment_detection\data\\f_wikidata\\wiki_texts_zh.txt'

        self.get_wiki_text_path = 'D:\source_codes\python\Sentiment\sentiment_detection\data\\f_wikidata\\zhwiki-latest-pages-articles.xml.bz2'
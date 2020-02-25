

# torch_learning_rate = 0.04
# torch_min_learning_rate = 0.001

class Config():
    def __init__(self):
        self.torch_learning_rate = 0.04
        self.torch_min_learning_rate = 0.001
        #win
        self.torch_bce_model = 'model/torch/pytorch_bce.model'
        self.word2vec_model = 'model/w2v/word2vec.model'
        self.dict_big_text = 'data/dict/dict.txt.big'
        self.dict_my_dict = 'data/dict/my_dict'
        #mac

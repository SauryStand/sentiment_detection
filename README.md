# sentiment_detection


# 建置流程
1. 先處理wiki data，準備製作w2v模型
    - 使用檔案:`w2v_seg.py`
2. 使用處理好的wiki data訓練w2v模型
    - 使用檔案:`w2v_train.py`
3. 取得waimai資料集句向量
    - 使用檔案:`make_w2v_set.py`
4. 訓練神經網路
    -  使用檔案:`jwp_train_bce.py`
5. 測試
    - 使用檔案:`demo.py`
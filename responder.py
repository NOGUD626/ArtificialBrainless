from random import choice

class Responder:
    """AIの応答を制御する思考エンジンの基底クラス。
    
    メソッド：
    responder(str) -- ユーザの入力strを受け取り、思考結果を返す
    
    プロパティ:
    name -- Responderオブジェクトの名前
    
    memo:
    *args: 複数の引数をタプルとして受け取る
    **kwargs: 複数のキーワード引数を辞書として受け取る
    """
    
    def __init__(self,name):
        """文字列を受け取り、自身のnameに設定する。"""
        self._name = name
        
    def response(self,*args):
        """文字列を受け取り、思考した結果を返す"""
        pass
    
    @property
    def name(self):
        """応答オブジェクトの名前"""
        return self._name

class WhatResponder(Responder):
    """AIの応答を制御する思考エンジンクラス
    入力に対して疑問形で聞き返す。"""
    def response(self,text):
        """文字列をtextを受け取り、'{text}ってなに？'という形式で返す。"""
  
class RandomResponder(Responder):
    """AIの応答を制御する思考エンジンクラス。
    登録された文字列からランダムなものを返す。
    
    クラス変数：
    RESPONSES -- 応答する文字列のリスト
    """
    
    RESPONSES = ["今日は寒いね",'チョコたべたい',"きのう10円拾った"]
    
    def response(self,_):
        """ユーザーからの入力は受け取るが、使用せずにランダムな応答を返す。"""
        return choice(RandomResponder.RESPONSES)
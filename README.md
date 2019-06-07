# jumanpp-bert-api


## 概要


黒橋・河原研究所が作成したBERTの事前学習モデルをAPI化したものである。


[BERT日本語Pretrainedモデル - KUROHASHI-KAWAHARA LAB](http://nlp.ist.i.kyoto-u.ac.jp/index.php?BERT%E6%97%A5%E6%9C%AC%E8%AA%9EPretrained%E3%83%A2%E3%83%87%E3%83%AB)


Dockerを使った環境を提供することで、使用者はこのレポジトリを`git clone`したのちに`docker-compose up -d`と打ち込むだけで、bertモデルから特徴量を生成するAPIを設置できる。



## 仕様


ポートは80ポートに割り当てられているので、TCP/IPを用いて、


- POST
- content-type: application/json、
- http://localhost/text


に以下のパラメータ


```
{"texts":["sentence1","sentence2","sentenceN"]} 
```


をリクエストすることで、特徴量を受け取ることができる。


bert-as-serviceを使用しているので、BERTの12/24層のうちからどのように特徴量を獲得するのかの設定は、[こちら](https://github.com/hanxiao/bert-as-service)を参考にして欲しい。




`codes/setup.sh`が起動コマンドで、デフォルトの設定では、

```
bert-serving-start -model_dir ./models/jm/ -num_worker 1 max_seq_len=300000
```

という設定で立ち上がる。# jumanpp-bert-api

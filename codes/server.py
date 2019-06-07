# -*- encoding: utf-8 -*-

from flask import Flask, request, jsonify
from bert_serving.client import BertClient
from tokenization import JumanPPTokenizer
import numpy as np

from bert_juman import BertWithJumanModel
bert = BertWithJumanModel("./models/jm/",is_tokenized=True)


MAX_SEQ_LEN = 126
jpp = JumanPPTokenizer()

# bc = BertClient()

app = Flask(__name__)

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def vector_average(v):
    v_len = len(v)
    if v_len <= 1:
        return v
    for i in range(v_len):
        if i == v_len - 1:
            res_v = (res_v / (v_len - 1)).tolist()
            break
        elif i == 0:
            res_v = np.array(v[i])
            continue
        res_v = res_v + np.array(v[i])
    return res_v

@app.route("/text", methods=["POST"])
def bert_api():
    try:
        texts_list = request.json['texts']
        layer_num = int(request.json['layer'])
        pooling_strategy =  request.json['pooling_strategy']
        whole_tokens_list = [jpp.tokenize(t) for t in texts_list]
        vectorized_texts_list = []

        for tokens in whole_tokens_list:
            div_num = len(tokens) // MAX_SEQ_LEN
            if div_num > 1:
                tokens_list = list(chunks(tokens, MAX_SEQ_LEN))
            else:
                tokens_list = [tokens]

            tt = []
            for t in tokens_list:
                vectorized_texts = bert.get_sentence_embedding(t,
                                            pooling_layer=layer_num,
                                            pooling_strategy=pooling_strategy).tolist()
                tt.append(vectorized_texts)

            # vectorized_texts = bc.encode(tokens_list, is_tokenized=True).tolist()
            vectorized_texts = vector_average(tt)
            vectorized_texts_list.append(vectorized_texts)

        response = {
            'vectorized_texts': vectorized_texts_list,
            'status': 200
        }

    except BaseException as e:
        response = {
            'vectorized_texts': None,
            'error': str(e),
            'status': 400
        }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

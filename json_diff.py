import os, sys, json

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
json_ = sys.argv[1].endswith("json")
label_index = sys.argv[2] if json_ else int(sys.argv[2])
score_index = sys.argv[3] if json_ else int(sys.argv[3])
with open(sys.argv[1], mode='r') as f:
    for line in f:
        if sys.argv[1].endswith('json'):
            data = json.loads(line)
        else:
            data = line.split('\t')
        true_label = int(data[label_index])
        score = float(data[score_index])
        if score > float(sys.argv[4]):
            predict_label = 1
        else:
            predict_label = 0
        if true_label != predict_label:
            print(line.strip())
#print(f"accuracy: {accuracy}, precision: {precision}, recall: {recall}, f1: {f1}")

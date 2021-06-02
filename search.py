import re
import time


def getOccurrences(query, sentence):
    lst = re.findall(query, sentence.lower())
    return len(lst)

example1 = '/content/drive/MyDrive/data1.txt'
file1 = open(example1,'r')
sentences = file1.readlines()
inpQuery = input("Please input your query string: ").lower()
init_time = time.time()

occurrenceSentence = {}
precision = 0.5/len(sentences)  # to handle  sentences with same relevance

for s in sentences:
    if s.find(inpQuery) != -1:
        occurrence = getOccurrences(inpQuery, s) + precision
        item = {occurrence: s}
        occurrenceSentence.update(item)
        precision += precision

no_of_results = len(occurrenceSentence)


if no_of_results != 0:

    print(f"Found {no_of_results} relevant results in {(time.time() - init_time)} ms")
    sor_dict = dict(sorted(occurrenceSentence.items(), key=lambda x: x[0], reverse=True)) # key is at 0 element of each item
    for k, v in sor_dict.items():
        print(k, v)
else:
    print("No results were found")
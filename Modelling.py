#using LDA technique for topic modelling

with open('D3.txt', 'r') as myfile:
  d1 = myfile.read()

with open('D5.txt', 'r') as myfile:
  d2 = myfile.read()

with open('D10.txt', 'r') as myfile:
  d3 = myfile.read()

with open('D19.txt', 'r') as myfile:
  d4 = myfile.read()

with open('D22.txt', 'r') as myfile:
  d5 = myfile.read()

with open('D24.txt', 'r') as myfile:
  d6 = myfile.read()

with open('D39.txt', 'r') as myfile:
  d7 = myfile.read()

with open('D42.txt', 'r') as myfile:
  d8 = myfile.read()

with open('D43.txt', 'r') as myfile:
  d9 = myfile.read()

with open('D45.txt', 'r') as myfile:
  d10 = myfile.read()

with open('D46.txt', 'r') as myfile:
  d11 = myfile.read()

with open('D47.txt', 'r') as myfile:
  d12 = myfile.read()

with open('D48.txt', 'r') as myfile:
  d13 = myfile.read()

with open('D49.txt', 'r') as myfile:
  d14 = myfile.read()

with open('D50.txt', 'r') as myfile:
  d15 = myfile.read()


doc_complete = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15]

#applying the standard Latent Dirichlet Allocation (LDA) using nltk library and also including the clean data beforehand
"""doc_complete = [
	"Human machine interface for Lab ABC computer applications",
	"A survey of user opinion of computer system response time",
	"The EPS user interface management system",
	"System and human system engineering testing of EPS",
	"Relation of user-perceived response time to error measurement",
	"The generation of random, binary, unordered trees",
	"The intersection graph of paths in trees",
	"Graph minors IV: Widths of trees and quasi-ordering",
	"Graph minors: A survey"
	]"""

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]  
dictionary = corpora.Dictionary(doc_clean)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(doc_term_matrix, num_topics=15, id2word = dictionary, passes=100)
print(ldamodel.print_topics(num_topics=15, num_words=4))

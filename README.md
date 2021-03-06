TOPIC MINING FROM YOUTUBE TEXT TRANSCRIPTS


Downloading MP3/WAV audio file for the list of video links provided:

Package Used – youtube_dl

Methodology-Created and ran a shell script to take input from the list of links provided and redirected all the WAV files to a folder names as Vx.WAV where x is the number of the video. From now onwards a video is uniquely identified by x.

Comments – Used the WAV format instead of MP3 because speech to text APIs support such a file. If MP3 is required, it can be easily obtained by changing the parameters passed to the function. We can use Audacity software to convert from one form to another.

Extracting Text Transcripts from WAV Files:

Package Used – SpeechRecognition, CMUSphinx

Methodology – Exceute a shell script to take all audio files and use the pocketsphinx API to transalation and redirect all the outputs to respective documents.

Comments – Google Speech Cloud API gives slightly better results but it requires interent connectivity. Pocketsphinx is thus more convenient and slight inaccuracies do not affect the task in hand in particular.

Topic Mining from List of Text Documents: (Latent Dirichlet Allocation)

Package Used – nltk, gensim

Methodology-

1. Cleaning up the data to remove redundant words like prepositions, articles and punctuation marks which appear with high probabilities in any transcript but never contribute to topic modelling.
2. Create the LDA matrix of documents as rows and words as colums.
3. Factorise the above matrix into one of documents vs topics and other of topics versus words. Each elements in both the matrices will correspond to frequency count of the topic/word respectively.
4. Find the product of conditional probabilities for all the words and display top few words as output and construct a meaningful topic from these set of outputs.
5. The hyperparamters here are the number of iterations, number of topics in each document and number of words per topic (refered as alpha and beta parameters).


 ###  LOADING THE DATA
    ## 1 TOKENIZ
    sentence = """At eight o'clock on Thursday morning
    ... Arthur didn't feel very good."""
    tokens = nltk.word_tokenize(sentence)
    tokens

    ['At', 'eight', "o'clock", 'on', 'Thursday', 'morning',
     'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']
    tagged = nltk.pos_tag(tokens)
    tagged[0:6]
    [('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'),
     ('Thursday', 'NNP'), ('morning', 'NN')]

    # 2 display enetitites

    entities = nltk.chunk.ne_chunk(tagged)
    entities
    ## count pos tags
    text = "Guru99 is one of the best sites to learn WEB, SAP, Ethical Hacking and much more online."
    lower_case = text.lower()
    tokens = nltk.word_tokenize(lower_case)
    tags = nltk.pos_tag(tokens)
    counts = Counter(tag for word, tag in tags)
    print(counts)

    ### COUNTING POS TAGS

    text = "Guru99 is one of the best sites to learn WEB, SAP, Ethical Hacking and much more online."
    lower_case = text.lower()
    tokens = nltk.word_tokenize(lower_case)
    tags = nltk.pos_tag(tokens)
    counts = Counter(tag for word, tag in tags)
    print(counts)

    #  from nltk.corpus import treebank
    t = treebank.parsed_sents('wsj_0001.mrg')[0]
    t.draw()

    ## produces graphicsal of dispalyed words s
    a = "Gase     visit the site guru99.com and much more."
    words = nltk.tokenize.word_tokenize(a)
    fd = nltk.FreqDist(words)
    fd.plot()

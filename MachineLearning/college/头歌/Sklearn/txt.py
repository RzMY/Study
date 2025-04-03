from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


categories = [
    'alt.atheism',
    'talk.religion.misc',
]

# 加载对应目录的新闻数据，包含857 个文档
data = fetch_20newsgroups("./step5/",subset='train', categories=categories)
X = data.data

def transfer2CountVector():
    '''
    使用CountVectorizer方法提取特征向量，返回词汇表大小和前五条特征向量

    返回值:
    vocab_len - 标量，词汇表大小
    tokenizer_list - 数组，对测试字符串test_str进行分词后的结果
    '''

    vocab_len = 0

    test_str = "what's your favorite programming language?"
    tokenizer_list = []

    #   请在此添加实现代码   #
    # ********** Begin *********#

    count_vectorizer = CountVectorizer()
    count_vectorizer.fit(X)
    vocab_len = len(count_vectorizer.vocabulary_)
    tokenizer_list = count_vectorizer.build_analyzer()(test_str)

    # ********** End **********#

    return vocab_len,tokenizer_list

def transfer2TfidfVector():
    '''
        使用TfidfVectorizer方法提取特征向量，并将向量化转换器应用到新的测试数据

        TfidfVectorizer()方法的参数设置：
        min_df = 2,stop_words="english"

        test_data - 需要转换的原数据

        返回值:
        transfer_test_data - 二维数组ndarray
        '''

    test_data = ['Once again, to not believe in God is different than saying\n>I BELIEVE that God does not exist. I still maintain the position, even\n>after reading the FAQs, that strong atheism requires faith.\n>\n \nNo it in the way it is usually used. In my view, you are saying here that\ndriving a car requires faith that the car drives.\n \nFor me it is a conclusion, and I have no more faith in it than I have in the\npremises and the argument used.\n \n \n>But first let me say the following.\n>We might have a language problem here - in regards to "faith" and\n>"existence". I, as a Christian, maintain that God does not exist.\n>To exist means to have being in space and time. God does not HAVE\n>being - God IS Being. Kierkegaard once said that God does not\n>exist, He is eternal. With this said, I feel it\'s rather pointless\n>to debate the so called "existence" of God - and that is not what\n>I\'m doing here. I believe that God is the source and ground of\n>being. When you say that "god does not exist", I also accept this\n>statement - but we obviously mean two different things by it. However,\n>in what follows I will use the phrase "the existence of God" in it\'s\n>\'usual sense\' - and this is the sense that I think you are using it.\n>I would like a clarification upon what you mean by "the existence of\n>God".\n>\n \nNo, that\'s a word game. The term god is used in a different way usually.\nWhen you use a different definition it is your thing, but until it is\ncommonly accepted you would have to say the way I define god is ... and\nthat does not exist, it is existence itself, so I say it does not exist.\n \nInterestingly, there are those who say that "existence exists" is one of\nthe indubitable statements possible.\n \nFurther, saying god is existence is either a waste of time, existence is\nalready used and there is no need to replace it by god, or you are implying\nmore with it, in which case your definition and your argument so far\nare incomplete, making it a fallacy.\n \n \n(Deletion)\n>One can never prove that God does or does not exist. When you say\n>that you believe God does not exist, and that this is an opinion\n>"based upon observation", I will have to ask "what observtions are\n>you refering to?" There are NO observations - pro or con - that\n>are valid here in establishing a POSITIVE belief.\n(Deletion)\n \nWhere does that follow? Aren\'t observations based on the assumption\nthat something exists?\n \nAnd wouldn\'t you say there is a level of definition that the assumption\n"god is" is meaningful. If not, I would reject that concept anyway.\n \nSo, where is your evidence for that "god is" is meaningful at some level?\n   Benedikt\n']
    transfer_test_data = None

    #   请在此添加实现代码   #
    # ********** Begin *********#

    tfidf_vectorizer = TfidfVectorizer(min_df=2, stop_words="english")
    tfidf_vectorizer.fit(X)
    transfer_test_data = tfidf_vectorizer.transform(test_data).toarray()

    # ********** End **********#

    return transfer_test_data


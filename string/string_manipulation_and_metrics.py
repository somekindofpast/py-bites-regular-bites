import re
import string
from collections import Counter
from dataclasses import dataclass, field
from typing import List, Set, Tuple


STOPWORDS: set = {
    "she's", "wasn", "through", "won", "that'll", "his", "once", "this",
    "you", "ll", "has", "because", "m", "ours", "doing", "any", "aren't",
    "they", "shouldn't", "being", "out", "is", "our", "it", "don", "had",
    "nor", "your", "she", "you've", "themselves", "or", "y", "needn", "on",
    "to", "at", "it's", "ve", "s", "too", "up", "didn't", "during", "haven",
    "can", "haven't", "each", "couldn", "isn't", "not", "against", "where",
    "was", "aren", "all", "by", "why", "hers", "theirs", "have", "as",
    "yourself", "their", "very", "who", "yourselves", "over", "and",
    "again", "do", "weren't", "which", "ma", "in", "such", "herself",
    "yours", "doesn", "if", "my", "after", "into", "just", "now", "isn",
    "itself", "between", "will", "other", "its", "these", "should", "re",
    "below", "having", "am", "both", "d", "you'll", "but", "should've",
    "won't", "himself", "shan't", "the", "me", "weren", "further", "until",
    "here", "myself", "whom", "were", "hasn", "don't", "wouldn't", "been",
    "before", "above", "he", "than", "most", "shan", "them", "mustn't",
    "couldn't", "you'd", "for", "of", "her", "those", "needn't", "you're",
    "t", "hadn't", "down", "o", "did", "about", "from", "does", "wouldn",
    "off", "then", "ain", "few", "hasn't", "some", "i", "ourselves", "an",
    "when", "are", "under", "more", "with", "hadn", "what", "while", "didn",
    "doesn't", "only", "him", "mightn", "be", "mightn't", "a", "how", "no",
    "there", "that", "so", "we", "same", "mustn", "wasn't", "shouldn", "own",
}
GETTYSBURG: str = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battlefield of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we cannot dedicate—we cannot consecrate—we cannot hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom— and that government of the people, by the people, for the people, shall not perish from the earth."""  # noqa E501


@dataclass
class Corpora:
    """Add the initial variables along with creating any methods that
    will get this working as described in the bite's description.

    * txt
    * count
    * tag
    * extra
    * stopwords
    """
    txt: str
    count: int = field(init=False, repr=False)
    tag: str = field(init=False, repr=False)
    extra: [str] = field(init=False, repr=False)
    stopwords: [str] = field(init=False, repr=False)

    def __post_init__(self):
        self.count = 5
        self.tag = "#"
        self.extra = []
        self.stopwords = STOPWORDS

    @property
    def cleaned(self) -> str:
        """Takes a corpus and cleans it up.

        * All text is made lowercase
        * All punctuation is removed
        * If a list of extra characters were given, remove those too

        :param txt: Corpus of text
        :return: cleaned up corpus
        """
        to_be_removed = list(string.punctuation)
        text_no_extra = self.txt.lower()
        for item in self.extra:
            text_no_extra = re.sub(item, '', text_no_extra)
        cleaned = ""
        for i in range(len(text_no_extra)):
            char = text_no_extra[i]
            if char == '\n':
                cleaned += ' '
            elif char == '—':
                if 0 <= i - 1 and text_no_extra[i - 1] != ' ' and i + 1 < len(text_no_extra) and text_no_extra[i + 1] != ' ':
                    cleaned += ' '
            elif char not in to_be_removed:
                cleaned += char

        return cleaned

    @property
    def metrics(self) -> List[Tuple[str, int]]:
        """Generates word count metrics.

        * Using the cleaned up corpus, count up how many times each word is used
        * Exclude stop words using STOPWORDS
        * Use count to return the requested amount of the top words, defaults to 5

        :return: List of tuples, i.e. ("word", count)
        """
        counter = Counter()
        for word in self.cleaned.split():
            if word not in self.stopwords:
                counter[word] += 1
        return counter.most_common(self.count)

    @property
    def graph(self) -> None:
        """Generates a textual graph of the words

        * Prints out the words along with a "tag" bar graph, defaults to using
          the # character
        * The word is right-aligned and takes up 10 character spaces
        * The tag is repeated the number of counts of the word

        For example, the top 10 words in the Gettysburg address would be
        displayed in this manner:

            nation #####
         dedicated ####
             great ###
            cannot ###
              dead ###
                us ###
             shall ###
            people ###
               new ##
         conceived ##

        :param metrics: List of tuples with word counts
        :return: None
        """
        for item in self.metrics:
            print(f"{item[0] : >10} " + (self.tag * item[1]))


if __name__ == '__main__':
    TAX_SYSTEM_IN_US = """Suppose that every day, ten men go out for beer, and the bill for all ten comes to $100.  If they paid their bill the way we pay our taxes (by taxpayer decile), it would go something like this:

    The first four men (the poorest) would pay nothing.
    The fifth would pay $1.
    The sixth would pay $3.
    The seventh would pay $7.
    The eighth would pay $12.
    The ninth would pay $18.
    The tenth man (the richest) would pay $59.

    So, that’s what they decided to do.

    The ten men drank in the bar every day and seemed quite happy with the arrangement, until one day, the owner threw them a curve ball.  “Since you’re all such good customers,” he said, “I’m going to reduce the cost of your daily beer by $20.”  Drinks for the ten men would now cost just $80.

    The group still wanted to pay their bill the way we pay our taxes.  So the first four men were unaffected. They would still drink for free.  But what about the other six?  How could they divide up the $20 windfall so that everyone would get his fair share?

    The bar owner suggested that it would be fair to reduce each man’s bill by a higher percentage the poorer he was, to follow the principle of the tax system they had been using, and he proceeded to suggest the new lower amounts each should now pay.

    And so the fifth man, like the first four, now paid nothing (a 100% saving).
    The sixth now paid $2 instead of $3 (a 33% saving).
    The seventh now paid $5 instead of $7 (a 29% saving).
    The eighth now paid $9 instead of $12 (a 25% saving).
    The ninth now paid $14 instead of $18 (a 22% saving).
    The tenth now paid $50 instead of $59 (a 15% saving).

    The first four continued to drink for free, and the latter six were all better off than before.  But, once outside the bar, the men began to compare their savings.

    “I only got a dollar out of the $20 saving,” declared the fifth man.  He pointed to the tenth man, “But he got $9!”

    “Yeah, that’s right,” exclaimed the sixth man.  “I only saved a dollar, too. It’s unfair that he saved nine times more than me!”

    “That’s true!” shouted the seventh man.  “Why should he get $9 back, when I got only $2?  The wealthy get all the breaks!”

    “Wait a minute,” yelled the first four men in unison, “we didn’t get anything at all.  This new tax system exploits the poor!”

    The nine men surrounded the tenth and beat him up.

    The next day, the tenth man didn’t show up, so the other nine sat down and had their beers without him.  But when it came time to pay the bill, they discovered something important: They didn’t have enough money between all of them for even half of the bill!

    And that is how our tax system works.  The people who already pay the highest taxes will naturally get the most benefit from a tax reduction.  Tax them too much, attack them for being wealthy, and they just may not show up anymore.  In fact, they might start drinking overseas, where the atmosphere is friendlier."""
    EXTRA_CHAR = "’ “ ”".split()

    corpora = Corpora(GETTYSBURG)
    _cleaned = corpora.cleaned
    print(_cleaned)
    print(len(_cleaned))
    print(corpora.metrics)
    corpora.graph

    corpora = Corpora(TAX_SYSTEM_IN_US)
    _cleaned = corpora.cleaned
    print(_cleaned)
    print(len(_cleaned))
    corpora.extra = ["men", "man"]
    corpora.count = 10
    corpora.tag = '*'
    print(corpora.metrics)
    corpora.graph
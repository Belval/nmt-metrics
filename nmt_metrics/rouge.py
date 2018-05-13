class RougeN(object):
    """
        Rouge-N evaluation metric, as defined in http://www.aclweb.org/anthology/W/W04/W04-1013.pdf
    """

    @staticmethod
    def evaluate(s1, s2, ngrams=1):
        """
            Evaluates the closeness of s1 to s2
        """
    
        score = 0.0

        s1_grams = [s1[i:i+ngrams] for i in range(len(s1)-ngrams+1)]
        s2_grams = [s2[i:i+ngrams] for i in range(len(s2)-ngrams+1)]

        for gram in s2_grams:
            if gram in s1_grams:
                score += 1.0
                s1_grams.remove(gram)

        return score / len(s2)

        
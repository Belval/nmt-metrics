# nmt_metrics [![TravisCI](https://travis-ci.org/Belval/nmt-metrics.svg?branch=master)](https://travis-ci.org/Belval/nmt-metrics)

A Python 3 package with some of the most used machine translation metrics

How to install:

pip package coming soon (still testing metrics)

How to use:

    from nmt_metrics import Bleu, Rouge, Meteor

    s1 = 'the cat sat on the mat'.split(' ')
    s2 = 'on the mat sat the cat'.split(' ')

    Bleu.evaluate(s1, s2) # 1.0
    Rouge.evaluate(s1, s2) # 1.0
    Meteor.evaluate(s1, s2) # 0.5

nmt_metrics does not manage tokenization for you. It expects a sequence of token.

## Supported metrics

- BLEU
- ROUGE
- METEOR

## [METRIC] is not included

1. Clone project
2. Create a name_of_your_metric.py file in the nmt_metrics folder
3. Reproduce the template used for the other metrics (implement evaluate() function)
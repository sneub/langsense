# -*- coding: utf-8 -*-

from . import ruleset

import re
import operator

class LangSense(object):
  def detect(self, string, country_hint=None):
    if type(string) == str:
      text = string.decode('utf-8').lower()
    else:
      text = string.lower()

    shortlist_char = self._char_shortlist(text)
    shortlist_rules = self._rule_shortlist(text)
    shortlist_words = self._word_shortlist(text)
    shortlist_segments = self._segment_shortlist(text)

    result = {l: 0 for l in ruleset.RuleSet.language_list}

    for l in ruleset.RuleSet.language_list:
      try:
        result[l] += (shortlist_char[l] * ruleset.RuleSet.score_weights['char'])
      except Exception, _:
        pass

      try:
        result[l] += (shortlist_rules[l] * ruleset.RuleSet.score_weights['rule'])
      except Exception, _:
        pass

      try:
        result[l] += (shortlist_words[l] * ruleset.RuleSet.score_weights['word'])
      except Exception, _:
        pass

      try:
        result[l] += (shortlist_segments[l] * ruleset.RuleSet.score_weights['segment'])
      except Exception, _:
        pass

    sum_scores = sum([v for _, v in result.iteritems()])
    result = {k: float(v)/sum_scores for k, v in result.iteritems() if v > 0}

    if country_hint:
      country_hint = country_hint.decode('utf-8').upper()
      lang = ruleset.RuleSet.country_langs[country_hint]
      if lang in result:
        result[lang] *= ruleset.RuleSet.score_weights['hint']

    result = list(reversed(sorted(result.items(), key=operator.itemgetter(1))))

    return result

  def _char_shortlist(self, string):
    lang_shortlist = []

    for c in string:
      lang_shortlist = lang_shortlist + [(c, l) for (l, a) in ruleset.RuleSet.alphabets.iteritems() if c in a]

    langs = set([i[1] for i in lang_shortlist])

    master_langs = []
    bad_langs = []
    scores = {l: len(string) for l in langs}

    for l in langs:
      for c, _ in lang_shortlist:
        if c not in ruleset.RuleSet.alphabets[l]:
          bad_langs.append(l)
          scores[l] -= 1

      master_langs.append(l)

    scores = {k: s/len(string) for k, s in scores.iteritems()}
    return {k: v for k, v in scores.iteritems() if v > 0}


  def _rule_shortlist(self, string):
    lang_shortlist = []
    scores = {}

    for lang, rules in ruleset.RuleSet.word_rules.iteritems():
      for rule in rules:
        if re.search(rule, string):
          lang_shortlist.append(lang)

          if lang in scores:
            scores[lang] += 1
          else:
            scores[lang] = 1

    return {k: scores[k] for k in list(set(lang_shortlist))}


  def _segment_shortlist(self, string):
    lang_shortlist = []
    scores = {}

    for lang, segments in ruleset.RuleSet.word_segments.iteritems():
      for segment in segments:
        if re.search(r'\w'+ segment + r'\b', string) or re.search(r'\b'+ segment + r'\w', string) or re.search(r'\w'+ segment + r'\w', string):
          lang_shortlist.append(lang)

          if lang in scores:
            scores[lang] += 1
          else:
            scores[lang] = 1

    return {k: scores[k] for k in list(set(lang_shortlist))}

  
  def _word_shortlist(self, string):
    lang_shortlist = []
    scores = {}

    for lang, words in ruleset.RuleSet.words.iteritems():
      for word in words:
        if re.search(r'\b'+ word + r'\b', string):
          lang_shortlist.append(lang)

          if lang in scores:
            scores[lang] += 1
          else:
            scores[lang] = 1

    return {k: scores[k] for k in list(set(lang_shortlist))}

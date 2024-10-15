from cltk import NLP

vitruvius = "Architecti est scientia pluribus disciplinis et variis eruditionibus ornata, quae ab ceteris artibus perficiuntur. Opera ea nascitur et fabrica et ratiocinatione."

cltk_nlp = NLP(language="lat")

cltk_doc = cltk_nlp.analyze(text=vitruvius)

cltk_doc.tokens[:5]
cltk_doc.lemmata[:5]
cltk_doc.morphosyntactic_features[2]  # 'scientia'
cltk_doc.pos[:5]
cltk_doc.sentences_tokens

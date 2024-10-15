from cltk import NLP

# Initialize the NLP model for Latin language
cltk_nlp = NLP(language="lat")

# Input text in Latin
text = (
    "In nova fert animus mūtātās dīcere fōrmās corpora; dī, coeptīs (nam vōs mūtāstis et illās) "
    "adspīrāte meīs prīmāque ab orīgine mundī ad mea perpetuum dēdūcite tempora carmen! "
    "Ante mare et terrās et quod tegit omnia caelum ūnus erat tōtō nātūrae vultus in orbe, "
    "quem dīxēre chaos rudis indīgestaque mōlēs nec quicquam nisi pondus iners congestaque eōdem "
    "nōn bene iūnctārum discordia sēmina rērum."
)

# Analyze the text
cltk_doc = cltk_nlp.analyze(text=text)

# Print the first 12 tokens of the analyzed document
print(cltk_doc.tokens[:12])
cltk_nlp.analyze(text=text)
print (cltk_doc.tokens[:12])
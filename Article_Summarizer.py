#!/usr/bin/env python
# coding: utf-8

# In[26]:


get_ipython().run_cell_magic('capture', '', '\npip install newspaper3k')


# In[27]:


get_ipython().run_cell_magic('capture', '', "\nimport nltk\nfrom newspaper import Article\nnltk.download('punkt')\nfrom IPython.display import clear_output\n\n# make pretty optional\nimport pprint\npp = pprint.PrettyPrinter(indent=4)\n# pp.pprint(article.summary.replace('\\n', ''))")


# In[28]:


import ipywidgets as widgets
from IPython.display import display

class url_input():
    def __init__(self, url = ""
                ):
        self.url = widgets.Text(url)
        self.url.on_submit(self.handle_submit)
        display(self.url)

    def handle_submit(self, text):
        self.v = str(text.value)
        return self.v

print("Please enter an article URL")
f = url_input()


# In[55]:


button = widgets.Button(description='TL;DR')
output = widgets.Output()

display(button, output)

def click(b):
    # parse and summarize article
    article = Article(f.url.value)
    article.download()
    article.parse()
    article.nlp()

    #display
    with output:
        clear_output()
        display('AUTHOR: {}'.format(', '.join([str(elem) for elem in article.authors])), 
                '======================================================================',
                'DATE PUBLISHED: {}'.format(article.publish_date), 
                '======================================================================',
                'SUMMARY: {}'.format(article.summary.replace('\n', '')),
                '======================================================================',
                'FULL TEXT: {}'.format(article.text.replace('\n', ''))
               )

button.on_click(click)


# In[ ]:





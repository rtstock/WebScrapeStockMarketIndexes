# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:19:15 2015

@author: justin.malinchak
"""

from bs4 import BeautifulSoup
html_doc= """
<article>
<topic>oil, gas</topic>
<body>body text</body>
</article>

<article>
<topic>food</topic>
<body>body text</body>
</article>

<article>
<topic>cars</topic>
<body>body text</body>
</article>
"""
soup = BeautifulSoup(html_doc)

bodies = [a.get_text() for a in soup.find_all('body')]
topics = [a.get_text() for a in soup.find_all('topic')]
print bodies
print topics

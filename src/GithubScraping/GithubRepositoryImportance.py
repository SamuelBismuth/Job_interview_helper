# We only take the project where the user have contribuate x% of all the project.
# QUESTION: Is it really relevant to calculate this in % and not in time to work...
# We must give a grade to all the project.
# How to attribute a grade for a project?

#/SamuelBismuth/GIS

from bs4 import BeautifulSoup

html_doc = open('/home/sam/Desktop/Final_Project/GithubScraping/repositories.html')

soup = BeautifulSoup(html_doc, 'html.parser')

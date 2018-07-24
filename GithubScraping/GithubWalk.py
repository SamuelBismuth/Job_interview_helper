# Here for a given github url we need to clone all the interesting project and classify
# them such that the use of PMD will be easy.
# Adding to the PMD work, we need to check all the files that are no code.

from bs4 import BeautifulSoup

html_doc = open('/home/sam/Desktop/Final_Project/GithubScraping/repositories.html')

soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())

# We need to separate project coded in different languages.
# Delete all the forked project.
# Need to check the contribution of the user.
# check number of contributors.
# ATTENTION: PMD only check the code, we must find another way to check the readme and the
# github repository.

for link in soup.find_all(itemprop="name codeRepository"):
    print(link.get('href'))





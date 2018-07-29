# Here for a given github url we need to clone all the interesting project and classify
# them such that the use of PMD will be easy.
# Adding to the PMD work, we need to check all the files that are no code.
from os import mkdir
import os
from bs4 import BeautifulSoup
from GithubScraping.GithubWget import w_get, git_clone
import shutil

future_worker = "yoshago"  # Here we need the github username.

# Here we're assuming the url is https://github.com/SamuelBismuth?tab=repositories
# but the real app must make an input (secure).
url = "https://github.com/" + future_worker + "?tab=repositories"
w_get(url, "repositories.html")

html_doc = open('/home/sam/Desktop/Final_Project/GithubScraping/repositories.html')

soup = BeautifulSoup(html_doc, 'html.parser')

# We need to separate project coded in different languages.
# Delete all the forked project.
# Need to check the contribution of the user.
# check number of contributors.
# ATTENTION: PMD only check the code, we must find another way to check the readme and the
# github repository.

# Giving to the user to find
# For example give to the user to choose if he want to focus on the java code or c++, or either ion the small
# code, or the big project, only 5 or everything. Maybe we can tell the running time for a chosen order.

if __name__ == "__main__":

    if not os.path.exists('/home/sam/Desktop/Final_Project/GithubScraping/' + future_worker):
        mkdir(future_worker)

    for link in soup.find_all(itemprop="name codeRepository"):
        git_clone('/home/sam/Desktop/Final_Project/GithubScraping/' + future_worker + '/',
                  "https://github.com" + link.get('href'))
        # Check the contribution of the user and the level of the project.


    shutil.rmtree('/home/sam/Desktop/Final_Project/GithubScraping/' + future_worker)
    os.remove('/home/sam/Desktop/Final_Project/GithubScraping/repositories.html')



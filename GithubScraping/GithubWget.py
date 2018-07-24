# Here we're assuming the url is https://github.com/SamuelBismuth?tab=repositories
# but the real app must make an input (secure).

from subprocess import call

url = "https://github.com/SamuelBismuth?tab=repositories"

call(["wget", "-Orepositories.html", "-P /home/sam/Desktop/Final_Project/GithubScraping", url])

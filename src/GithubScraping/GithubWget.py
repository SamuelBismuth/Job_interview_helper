from subprocess import call
import os


def w_get(url, output_name):
    call(["wget", "-O", output_name, "-P /home/sam/Desktop/Final_Project/GithubScraping", url])


def git_clone(path, url):
    os.chdir(path)
    call(["git", "clone", url])

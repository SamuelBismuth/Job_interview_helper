import subprocess
from subprocess import call
import os


def w_get(url, output_name):
    call(["wget", "-O", output_name, "-P /home/sam/Desktop/Final_Project/GithubScraping", url])


def git_clone(path, url):
    os.chdir(path)
    call(["git", "clone", url])


def pmd(pmd_path, src, ruleset, result):
    subprocess.Popen(["interminal", "--script", "alias pmd=\" " + pmd_path + " pmd\" \n "
                                            "pmd -d " + src + " -R "
                                            + ruleset + " -f csv -r "
                                            + result])


pmd("$HOME/Desktop/Final_Project/PMD/pmd-bin-6.7.0/bin/run.sh",
    "/home/sam/Desktop/Final_Project/PMD/TestMyTokenizer.java",
    "/home/sam/Desktop/Final_Project/PMD/ruleset.xml",
    "/home/sam/Desktop/Final_Project/PMD/result.csv")

#Joni's and Ishay's oop project:
pmd("$HOME/Desktop/Final_Project/PMD/pmd-bin-6.7.0/bin/run.sh",
    "/home/sam/Desktop/Final_Project/PMD/GIS/GIS/src",
    "/home/sam/Desktop/Final_Project/PMD/ruleset.xml",
    "/home/sam/Desktop/Final_Project/PMD/resultOPPProject.csv")
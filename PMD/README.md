please run:
alias pmd="$HOME/pmd-bin-6.5.0/bin/run.sh pmd"
pmd -d /home/sam/Desktop/Final_Project/PMD/TestMyTokenizer.java -R /home/sam/Desktop/Final_Project/PMD/ruleset.xml -f csv -r /home/sam/Desktop/Final_Project/PMD/result.csv


Joni's and Ishay's oop project:
pmd -d /home/sam/Desktop/Final_Project/PMD/GIS/GIS/src -R /home/sam/Desktop/Final_Project/PMD/ruleset.xml -f csv -r /home/sam/Desktop/Final_Project/PMD/resultOPPProject.csv


from the temrinal.

seems we need a "ruleset" for all the languages.
Read about the syntax of the ruleset.
Need to export the result into a csv table (seems to be the easiest way (or XML).
Include code/comments... Very strong tool.
Need to tranlate all the warning into a "grade" discuus about this.
Cna check (java):
    Best Practices
    Code Style
    Design
    Documentation
    Error Prone
    Multithreading
    Performance
    Security
    Additional rulesets

More doc about the terminal command here : https://pmd.github.io/pmd-6.5.0/pmd_userdocs_cli_reference.html#available-report-formats

ISSUES:
Not seem to know to check english level.
Must be in english, but this must be natural to the programmer -> can't check the french level for example. (check language <lang>
-l <lang>)  https://pmd.github.io/pmd-6.5.0/pmd_userdocs_cli_reference.html#available-report-formats

ATTENTION:
Can use PMD: copy paste code analyzer !!!

Supported Language:
https://pmd.github.io/pmd-6.5.0/pmd_userdocs_cpd#supported-languages

To export the result : -reportfile <path>
-r <path>

ATTENTION: PMD know how to travel in the folders, no need to send him to the src folder.




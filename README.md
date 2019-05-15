# LazyExtractor

![lazy](https://user-images.githubusercontent.com/16065604/57729907-44d38c80-7665-11e9-8c07-f4d1cc3cec9c.gif)

Allows the Easy extraction of Nintendo Switch NSP and XCI files.

Features:
* Supports only base NSP files for now
* Automatically Extracts NSP files and finds the biggest NCA and Titlekey for you.

Soon:
* Add Support to extract XCI files
* Add Support for Updated NSPs
*:white_check_mark: Add Support for Newer NCAs
* Better Error Handling
* Better Overall Readable Code


Concerns:
* Hangs with Extracting big NCA files with no progress bar.

Solution:
* Wait it out it is working, i have no figured out a way to pipe the progress information in yet. ( new to python )

Needed Files:
* Squirrel.exe :: https://github.com/julesontheroad/NSC_BUILDER :: grab it from that release
* Hactool.exe :: https://github.com/SciresM/hactool :: grab it from that release
* Python 2.7

HowTo:

* Extract Squirrel and Hactool to the same directory where app.py is.
* Run app.py

Why:
* This is my own personal tool i created so i did not have to constantly run commands,
i decided to release it to the public maybe others might find useful.

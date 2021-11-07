import webbrowser
from random import choice
random_page_generator = ['http://www.python.org','https://www.skype.com/en/',
                         'https://maharatech.gov.eg/login/index.php']
webbrowser.open(choice(random_page_generator),new=2)
#webbrowser.open('http://www.python.org')
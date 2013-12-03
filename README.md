For pelican blogs there is only the requirement of a webserver on the hosting site, as it is all static pages.
On the client side (to write blog articles) it is recommended to use python2.7 with virtualenv installed.
For debian/ubuntu it is:

    apt-get install python2.7 python2.7-dev python-virtualenv 

To create a virtual environment and change into it:

    $ virtualenv ~/virtualenvs/pelican
    $ cd ~/virtualenvs/pelican
    $ . bin/activate

you need to change into that virtualenv whenever working and generating your blog.

Install via pip in the virtual environment:

    $ pip install pelican

We do use Markdown and Typogrify for blog.torservers.net:

    $ pip install Markdown typogrify

To start a new pelicanblog use and answer the questions accordingly:
    
    $ pelican-quickstart

For the existing blog:

    $ git clone https://github.com/torservers/blog.torservers.net
    
Make your changes, most likely changing blog articles in ./content/ . You can quick regenerate the output by running `make html`. We prefer fabric:

    $ pip install Fabric

To create the blog from markdown:

    $ fab build

To quickly test locally (it will be accessible on http://localhost:8000 ):

    $ fab serve
 
To upload the blog to your webserver use, your public key needs to be on blog.torservers.net for the blog user.

    $ fab publish

To use Markdown your files need to end in .md, .markdown, .mkd or mdown in content/

To change the theme (and other settings) for your blog edit yor pelicanconf.py.
To get all kinds of themes:

    $ git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes

And edit your pelicanconf.py to include:

    THEME = "/home/user/pelican-themes/theme-name"

In our case we do have the theme copied within the repo under theme
THEME = "theme/


For a comprehensive guide to getting started:
http://docs.getpelican.com/en/latest/getting_started.html
For themes:
https://github.com/getpelican/pelican-themes

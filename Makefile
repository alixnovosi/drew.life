##-----------------------------------------------------------------------------------------------##
## AUTHOR:  Andrew Michaud                                                                       ##
## FILE:    Makefile                                                                             ##
## PURPOSE: compiling sass -> css for drew.life                                                  ##
## UPDATED: 2018-12-21                                                                           ##
## LICENSE: ISC                                                                                  ##
##-----------------------------------------------------------------------------------------------##
BASEDIR=$(CURDIR)

SASSINPUTDIR=$(BASEDIR)/sass
CSSOUTPUTDIR=$(BASEDIR)/css

BLOGCSSDIR=$(BASEDIR)/theme/static/css
BLOGSASSDIR=$(BASEDIR)/theme/static/sass
WEBCSSDIR=$(BASEDIR)/nginx_content/css
WEBSASSDIR=$(BASEDIR)/nginx_content/sass

.PHONY: all sasscompile csscopy clean

all: clean sasscompile csscopy

sasscompile:
	pyscss $(SASSINPUTDIR)/main.scss --output $(CSSOUTPUTDIR)/main.css --no-compress

csscopy:
	cp $(CSSOUTPUTDIR)/main.css $(BLOGCSSDIR)
	cp $(CSSOUTPUTDIR)/main.css $(WEBCSSDIR)
	cp $(SASSINPUTDIR)/main.scss $(BLOGSASSDIR)
	cp $(SASSINPUTDIR)/main.scss $(WEBSASSDIR)

clean:
	rm $(CSSOUTPUTDIR)/main.css $(WEBCSSDIR)/main.css $(WEBSASSDIR)/main.scss \
	$(BLOGCSSDIR)/main.css $(BLOGSASSDIR)/main.scss

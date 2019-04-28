##-----------------------------------------------------------------------------------------------##
## AUTHOR:  Andrew Michaud                                                                       ##
## FILE:    Makefile                                                                             ##
## PURPOSE: pelican generated makefile,                                                          ##
##          plus compiling sass -> css for drew.life, and moving other js around                 ##
## UPDATED: 2019-04-27                                                                           ##
## LICENSE: ISC                                                                                  ##
##-----------------------------------------------------------------------------------------------##
PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

SSH_HOST=laphicet.drew.life
SSH_PORT=22
SSH_USER=amichaud
SSH_TARGET_DIR=/usr/local/www/nginx/output

# custom items for SCSS compile and nonogram JS setup
CSSDIR=$(BASEDIR)/theme/static/css
SASSDIR=$(BASEDIR)/theme/static/sass
NONOGRAMDIR=$(BASEDIR)/nonogram_web

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

# custom for SCSS compile
sasscompile:
	pysassc $(SASSDIR)/main.scss $(CSSDIR)/main.css --style expanded

# custom for ReactJS toy,
# in git submodule
jscopy:
	cp $(NONOGRAMDIR)/dist/*.js $(INPUTDIR)/dist/
	cp $(NONOGRAMDIR)/dist/*.js.map $(INPUTDIR)/dist/

html: sasscompile jscopy
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
	rm -f $(CSSDIR)/main.css $(CSSDIR)/main.css.map
	rm -f $(INPUTDIR)/dist/*.js $(INPUTDIR)/dist/*.js.map

regenerate: sasscompile jscopy
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

serve-global:
ifdef SERVER
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b $(SERVER)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b 0.0.0.0
endif

devserver:
ifdef PORT
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

publish: sasscompile jscopy
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvz --delete $(OUTPUTDIR)/ \
$(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

.PHONY: html help clean regenerate serve serve-global devserver stopserver publish sasscompile \
jscopy rsync_upload

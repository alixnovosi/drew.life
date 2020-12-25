##----------------------------------------------------------------------------##
## author:  Andrew Michaud                                                    ##
## file:    Makefile                                                          ##
## purpose: pelican generated makefile,                                       ##
##          plus compiling sass -> css for drew.life,                         ##
##          and moving other js around                                        ##
## updated: 2020-12-24                                                        ##
## license: ISC                                                               ##
##----------------------------------------------------------------------------##
PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
AUTHOR_IMAGES=$(BASEDIR)/theme/static/images/author_images

CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

SSH_HOST=laphicet.drew.life
SSH_PORT=22
SSH_USER=amichaud
SSH_TARGET_DIR=/usr/local/www/nginx/output

# custom items for SCSS compile, and JS toy setup.
CSSDIR=$(BASEDIR)/theme/static/css
SASSDIR=$(BASEDIR)/theme/static/sass

# TODO can you do this more succinctly in make?
NONOGRAMDIR=$(BASEDIR)/dist/nonogram_web
SUDOKUDIR=$(BASEDIR)/dist/sudoku_web
BOUNCEDIR=$(BASEDIR)/dist/bounce
LORENZDIR=$(BASEDIR)/dist/lorenz
TREEDIR=$(BASEDIR)/dist/tree_web
SORTVIZDIR=$(BASEDIR)/dist/sortviz
MARKOVBOXDIR=$(BASEDIR)/dist/markovbox

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

# custom for js toys,
# in git submodule
jscopy:
	cp $(NONOGRAMDIR)/dist/* $(INPUTDIR)/dist/nonogram/
	cp $(SUDOKUDIR)/dist/* $(INPUTDIR)/dist/sudoku/
	cp $(BOUNCEDIR)/dist/* $(INPUTDIR)/dist/bounce/
	cp $(LORENZDIR)/dist/* $(INPUTDIR)/dist/lorenz/
	cp $(TREEDIR)/dist/* $(INPUTDIR)/dist/tree/
	cp $(SORTVIZDIR)/dist/* $(INPUTDIR)/dist/sortviz/
	cp $(MARKOVBOXDIR)/dist/* $(INPUTDIR)/dist/markovbox/

html: sasscompile jscopy
	cp -R $(INPUTDIR)/gallery/commart $(OUTPUTDIR)/gallery/
	$(BASEDIR)/hash_author_images $(INPUTDIR)/gallery/author_images $(AUTHOR_IMAGES)
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
	rm -f $(CSSDIR)/main.css $(CSSDIR)/main.css.map
	rm -f $(INPUTDIR)/dist/nonogram/*
	rm -f $(INPUTDIR)/dist/sudoku/*
	rm -f $(INPUTDIR)/dist/bounce/*
	rm -f $(INPUTDIR)/dist/lorenz/*
	rm -f $(INPUTDIR)/dist/tree/*
	rm -f $(INPUTDIR)/dist/sortviz/*
	rm -f $(INPUTDIR)/dist/markovbox/*

regenerate: sasscompile jscopy
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) \
		-p $(PORT)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

serve-global:
ifdef SERVER
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) \
		-p $(PORT) -b $(SERVER)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) \
		-p $(PORT) -b 0.0.0.0
endif

devserver:
ifdef PORT
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) \
		-p $(PORT)
else
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

publish: sasscompile jscopy
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	chmod -R o+r $(OUTPUTDIR)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvz --delete $(OUTPUTDIR)/ \
$(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

.PHONY: html help clean regenerate serve serve-global devserver stopserver \
	publish sasscompile jscopy rsync_upload

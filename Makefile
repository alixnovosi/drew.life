##-----------------------------------------------------------------------------------------------##
## AUTHOR:  Andrew Michaud                                                                       ##
## FILE:    Makefile                                                                             ##
## PURPOSE: compiling sass -> css for drew.life, and moving other stuff around                   ##
## UPDATED: 2019-02-26                                                                           ##
## LICENSE: ISC                                                                                  ##
##-----------------------------------------------------------------------------------------------##
BASEDIR=.

SASS_INPUT_DIR=$(BASEDIR)/theme/static/sass
CSS_OUTPUT_DIR=$(BASEDIR)/theme/static/css

NGINX_CONTENT=$(BASEDIR)/nginx_content

NONOGRAM_DIR=$(BASEDIR)/nonogram_web

.PHONY: all sasscompile csscopy jscopy pelican clean

all: clean sasscompile csscopy jscopy

pelican:
	pelican content --verbose

sasscompile:
	pyscss $(SASS_INPUT_DIR)/main.scss \
		--output $(CSS_OUTPUT_DIR)/main.css \
		--no-compress \
		--style expanded

jscopy:
	cp -R $(NONOGRAM_DIR)/dist $(NGINX_CONTENT)/
	cp $(NONOGRAM_DIR)/dist/nonogram.html $(NGINX_CONTENT)/

clean:
	rm -f $(CSS_DIR)/main.css \ $(CSS_DIR)/main.css.map

	rm -rf $(NGINX_CONTENT)/dist
	rm -f $(NGINX_CONTENT)/nonogram.html

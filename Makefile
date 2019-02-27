##-----------------------------------------------------------------------------------------------##
## AUTHOR:  Andrew Michaud                                                                       ##
## FILE:    Makefile                                                                             ##
## PURPOSE: compiling sass -> css for drew.life, and moving other stuff around                   ##
## UPDATED: 2019-02-26                                                                           ##
## LICENSE: ISC                                                                                  ##
##-----------------------------------------------------------------------------------------------##
BASEDIR=.

SASS_INPUT_DIR=$(BASEDIR)/sass
CSS_OUTPUT_DIR=$(BASEDIR)/css

BLOG_CSS_DIR=$(BASEDIR)/theme/static/css
BLOG_SASS_DIR=$(BASEDIR)/theme/static/sass
NGINX_CONTENT=$(BASEDIR)/nginx_content
WEB_CSS_DIR=$(NGINX_CONTENT)/css
WEB_SASS_DIR=$(NGINX_CONTENT)/sass

NONOGRAM_DIR=$(BASEDIR)/nonogram_web

.PHONY: all sasscompile csscopy jscopy clean

all: clean sasscompile csscopy jscopy

sasscompile:
	pyscss $(SASS_INPUT_DIR)/main.scss \
		--output $(CSS_OUTPUT_DIR)/main.css \
		--no-compress \
		--style expanded

csscopy:
	cp $(CSS_OUTPUT_DIR)/main.css $(BLOG_CSS_DIR)
	cp $(CSS_OUTPUT_DIR)/main.css.map $(BLOG_CSS_DIR)
	cp $(CSS_OUTPUT_DIR)/main.css $(WEB_CSS_DIR)
	cp $(CSS_OUTPUT_DIR)/main.css.map $(WEB_CSS_DIR)
	cp $(SASS_INPUT_DIR)/main.scss $(BLOG_SASS_DIR)
	cp $(SASS_INPUT_DIR)/main.scss $(WEB_SASS_DIR)

jscopy:
	cp -R $(NONOGRAM_DIR)/nonogram_web/dist $(NGINX_CONTENT)/
	cp $(NONOGRAM_DIR)/nonogram_web/nonogram.html $(NGINX_CONTENT)/

clean:
	rm -f $(CSS_OUTPUT_DIR)/main.css \
		$(WEB_CSS_DIR)/main.css $(WEB_SASS_DIR)/main.scss \
		$(BLOG_CSS_DIR)/main.css $(BLOG_SASS_DIR)/main.scss \
		$(WEB_CSS_DIR)/main.css.map $(BLOG_CSS_DIR)/main.css.map

	rm -rf $(NGINX_CONTENT)/dist
	rm -f $(NGINX_CONTENT)/nonogram.html

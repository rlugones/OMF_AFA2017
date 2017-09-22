name=poster
clean_ext = aux log nav out snm toc

all: compile #clean

test:
	pdflatex $(name).tex;

compile:
	pdflatex $(name).tex; pdflatex $(name).tex;

clean:
	rm -rf $(name).aux $(name).log $(name).nav $(name).out $(name).snm $(name).toc $(name)*~

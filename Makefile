PYTHON = 'python3'
all: 
	$(PYTHON) run.py

.PHONY: clean
clean:
	rm *.pyc *.txt

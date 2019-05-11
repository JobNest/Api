PYTHON = 'python3'
all: 
	$(PYTHON) run.py

online: 
	nohup $(PYTHON) run.py &

.PHONY: clean
clean:
	rm *.pyc *.txt

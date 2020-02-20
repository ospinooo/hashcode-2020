

zip:
	zip ./results/src.zip main.py input.py output.py solver.py
		
all:
	python main.py a_in.txt
	python main.py b_in.txt
	python main.py c_in.txt
	python main.py d_in.txt
	python main.py e_in.txt
	python main.py f_in.txt
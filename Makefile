PYTHON3=/usr/local/bin/python3 
PIP=/usr/local/bin/pip3

run: env tag36h11_big output
	. env/bin/activate; ${PYTHON3} apriltag-gen.py 

env: requirements.txt
	test -d env || virtualenv env
	. env/bin/activate; ${PIP} install -Ur requirements.txt
	touch env/bin/activate

tag36h11_big:
	mkdir tag36h11_big

output:
	mkdir output

clean:
	rm -rf env
	find -iname "*.pyc" -delete

FORCE:

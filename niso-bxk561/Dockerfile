FROM pklehre/niso2019-lab3
RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y pypy3
ADD src /bin
CMD ["-username", "bxk561", "-submission", "pypy3 /bin/lab/main.py"]
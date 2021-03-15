all:	unexpire newtime.so

unexpire : testexpire.c
	gcc -o unexpire testexpire.c 

newtime.so:	newtime.c
	gcc -shared -fPIC newtime.c -o newtime.so -ldl

clean:
	rm -f newtime.so *.o

test:	all
	@ echo "running random without our replacement of time()"
	@ unset LD_PRELOAD
	./unexpire
	@ echo "running random with our replacement of time()"
	export LD_PRELOAD=$$PWD/newtime.so; ./unexpire
	@ unset LD_PRELOAD


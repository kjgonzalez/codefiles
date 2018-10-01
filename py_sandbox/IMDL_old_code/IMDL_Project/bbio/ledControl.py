# objective: turn on any given LED light on BBB

base='/sys/class/leds/beaglebone:green:usr'
led ='/brightness'
trig='/trigger'
defaults=['heartbeat','none','cpu0','mmc1']

def init(n):
	# initialize an led: turn off trigger
	st=base+str(n)+trig
	value = open(st,'w')
	value.write(str('none'))
	value.close()

def cleanup(n):
	# cleanup led: restore trigger
	st=base+str(n)+trig
	value = open(st,'w')
	value.write(defaults[n])
	value.close()

def on(n):
	# turn on led
	st=base+str(n)+led
	value = open(st,'w')
	value.write(str(1))
	value.close()

def off(n):
	# turn off led
	st=base+str(n)+led
	value = open(st,'w')
	value.write(str(0))
	value.close()

# eof

'''
objective: quick kjg example of how to use dict

'''

# sample list here
a='''193990_dsnu-20-20-p-s6---_20p--.asm.1
193990_dsnu-20-20-p-s6---_20p--.asm.2
193990_dsnu-20-20-p-s6---_20p--.asm.3
193990_dsnu-20-20-p-s6---_20p--.asm.4
brakebalancerod.prt.1
brakebalancerod.prt.2
brakebalancerod.prt.3
brakebalancerod.prt.4
brakebalancerod.prt.5
brakemountingplate.prt.1
brakemountingplate.prt.2
brakemountingplate.prt.3
brakemountingplate.prt.4
brakemountingplate.prt.5
brake_assm_dv.asm.13
brake_cable_bracket.prt.9
creo_parametric_customization.ui
ebrake_193990_dsnu-20-20-p-s6.asm.1
ebrake_193990_dsnu-20-20-p-s6.asm.2
ebrake_193990_dsnu-20-20-p-s6.asm.3
ebrake_holder1.prt.1
ebrake_holder1.prt.2
ebrake_holder1.prt.3
ebrake_holder1.prt.4
ebrake_holder1.prt.5
ebrake_holder2.prt.1
ebrake_holder2.prt.2
ebrake_holder2.prt.3
emergency_brake_cable_bracket.prt.1
emergency_brake_cable_bracket.prt.2
fast_m6_40.prt.1
fast_m6_40.prt.2
fast_m6_8.prt.1
fast_m6_8.prt.2
fast_m6_8.prt.3
id_copies.py
linearactuator_50mm.prt.1
linearactuator_50mm.prt.2
linearactuator_50mm.prt.3
linearactuator_50mm.prt.4
linearactuator_50mm.prt.5
linearactuator_50mm.prt.6
linearactuator_50mm.prt.7
linearactuator_50mm.prt.8
linearmotordualbracket.prt.1
linearmotordualbracket.prt.2
linearmotordualbracket.prt.3
linearmotordualbracket.prt.4
linearmotordualbracket.prt.5
PRO_trl.txt.1
std.out
temp.prt.1
temp.prt.2
temp.prt.3
temp2.prt.1
temp2.prt.2
temp2.prt.3
trail.txt.1
_193990_dsnu-20-20-p---_-----0-.prt.1
_193990_dsnu-20-20-p---_----00-.prt.1
_din-439-b_-_m22x1_5_f_.prt.1'''

itemList = a.split('\n') # now have list of each line in above string


# next, want to count how many items are unique
d=dict()

for i in itemList:
	iname = i[:i.find('.')]
	if(d.has_key(iname)):
		# name is already in database / dictionary, add to count
		d[iname]=d[iname]+1
	else:
		# name not in dict, create new entry
		d[iname] = 1

for k in d:
	print d[k],k







import hashlib
username_trial = "MORTON"
bUsername_trial = b"MORTON"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

#I used bUsername_trial because enter_liscence used it as well but after testing afterwards, they output the same answer
mykey = ''


mykey = mykey + (hashlib.sha256(bUsername_trial).hexdigest()[4]) 
mykey = mykey + (hashlib.sha256(bUsername_trial).hexdigest()[5])
mykey = mykey + (hashlib.sha256(bUsername_trial).hexdigest()[3])
mykey = mykey + (hashlib.sha256(bUsername_trial).hexdigest()[6])
mykey = mykey + (hashlib.sha256(bUsername_trial).hexdigest()[2])
mykey = mykey + (hashlib.sha256(bUsername_trial).hexdigest()[7])
mykey = mykey + (hashlib.sha256(bUsername_trial).hexdigest()[1])
mykey = mykey + (hashlib.sha256(bUsername_trial).hexdigest()[8])
print(mykey)

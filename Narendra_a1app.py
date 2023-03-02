old=input("Enter original currency:").upper()
new=input("Enter desired currency:").upper()
amt=input("Enter original currency:")
import Narendra_a1

if(not(Narendra_a1.is_currency(old))):
	print(old," is not a valid currency")
	quit()
if(not(Narendra_a1.is_currency(new))):
	print(new," is not a valid currency")
	quit()
print(f'you can exhange{amt} {old} for {Narendra_a1.exchange(old,new,amt)} {new}')
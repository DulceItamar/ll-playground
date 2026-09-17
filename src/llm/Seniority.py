
def define_Seniority(years: int) -> str:
   if years <=1: 
    return "Entry-level candidate"
   elif years > 1 & years <=3:
    return "Junior candidate"
   else: 
    return "Senior candidate"
     

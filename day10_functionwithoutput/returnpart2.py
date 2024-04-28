# def format_name(f_name,l_name):
#   if f_name == "" or l_name == "":
#     return "it is not valid"
  
#   formatted_fname = f_name.title()
#   formatted_lname = l_name.title()

#   return f"{formatted_fname} {formatted_lname}"
#     #return itu end def , kalo dikasih print() ga bakal jalan

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(year,month):
  """Telling how many days in a month."""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month-1]
  


year = int(input())
month = int(input())
days = days_in_month(year, month)

# days_in_month()
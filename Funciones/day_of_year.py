def is_year_leap(year):
    if year%4!=0:
          return False
    elif year%100!=0:
          return True
    elif year%400!=0:
          return False
    else:
          return True      

def days_in_month(year, month):
    dias_mes=[31,[28,29],31,30,31,30,31,31,30,31,30,31]
    index=month-1
    if index!=1:
          return dias_mes[index]
    else:
          if is_year_leap(year):
               return dias_mes[1][1]
          else:
               return dias_mes[1][0]

def day_of_year(year, month, day):
    b_year=year>0 and type(year)==int
    b_month=((type(month)==int) and month>0 and month<13)
    b_day=(type(day)==int and day>0 and day<=days_in_month(year,month))
    if (b_year and b_month and b_day)==False:
         return 'Error en los argumentos'
    else:
        dia_del_mes=days_in_month(year,month)
        total_dias=day
        for i in range(1,month):
             total_dias+=days_in_month(year,i)
        return total_dias
             

print(day_of_year(2000, 12, 31))
print(day_of_year(2000, 2, 29))
step_file=open("step.txt","r")
days= {"january":31, "february":28, "march":31, "april":30, "may":31, "june":30, "july":31, "august":31, "september":30, "october":31, "november":30, "december":31}
dates = list(days.keys())
monthly_averages={}
for month in dates:
    total=0
    month_days=days[month]
    for steps in range (month_days):
        total+=int(step_file.readline())
    monthly_averages[month]=total/month_days

#TRENDS
trends=["N/A"]
last_avg=-1
for month in dates:
    avg_steps=monthly_averages[month]
    if last_avg!=-1:
        if avg_steps>last_avg:
            trends.append("increased")
        elif avg_steps<last_avg:
            trends.append("decreased")
        else:
            trends.append("stayed same")
    last_avg=avg_steps
#PRINTING
i=0
for month in dates:
    avg_steps = monthly_averages[month]
    print(f"{month.capitalize()} has {avg_steps:.2f} average steps and from previous month they",trends[i])
    i+=1
step_file.close()
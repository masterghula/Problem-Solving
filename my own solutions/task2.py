eye_file = open("optometry.txt", "r")
total_brown=0
total_green=0
total_blue=0
total_hazel=0

brown_tally=0
green_tally=0
hazel_tally=0
blue_tally=0
line_tally=0

for line in eye_file:
    temp_color = ''
    temp_age = ''
    age_collecting = "False"
    for char in line:
        if char==',' or char=='\n':
            age_collecting="True"
            continue
        elif char!=','and age_collecting=="False":
            temp_color+=char.upper()
        elif char!='\n':
            temp_age+=char
    if temp_color=="BROWN":
        total_brown+=int(temp_age)
        brown_tally+=1
    elif temp_color=="BLUE":
        total_blue+=int(temp_age)
        blue_tally+=1
    elif temp_color=="GREEN":
        total_green+=int(temp_age)
        green_tally+=1
    elif temp_color=="HAZEL":
        total_hazel+=int(temp_age)
        hazel_tally+=1
    line_tally+=1

print("Brown is ", brown_tally/line_tally*100, " of total", "and average age is ", total_brown/brown_tally)
print("Green is ", green_tally/line_tally*100, " of total", "and average age is ", total_green/green_tally)
print("Hazel is ", hazel_tally/line_tally*100, " of total", "and average age is ", total_hazel/hazel_tally)
print("Blue is ", blue_tally/line_tally*100, " of total", "and average age is ", total_blue/blue_tally)
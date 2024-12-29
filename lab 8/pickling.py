import pickle
students_dict = {'Chris':21, 'Paula':22, 'Lucy':21, 'Sarah':19, 'Michael':20, 'Bruce':21}
out_file = open('student_store.dat', 'wb')
pickle.dump(students_dict, out_file)
out_file.close()
input_file = open('student_store.dat', 'rb')
new_stud_dict = pickle.load(input_file)
for stud in new_stud_dict:
    print(stud, new_stud_dict[stud])
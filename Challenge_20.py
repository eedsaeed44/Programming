taskes_list = input("Enter your taskes for today seperated by comma: ").split(", ")
done_taskes = []
ongoing_taskes = []
for task in taskes_list:
    print(f"\n{task}\n")
    confirm = input(f"Did you finish {task} already?\n").lower()
    if confirm =='yes':
        print("Nice jobe!")
        done_taskes.append(task)
    else:
        print("Try not to put it off")
        ongoing_taskes.append(task)
    print("----------------------------------------")    
progress = input("Do you want to see your today's progress? (yes\no)\n").lower()
if progress == 'yes':
    print("\n***************** Done Taskes *****************\n")
    print(done_taskes)
    print("\n************* Ongoing Taskes ********************\n")
    print(ongoing_taskes)

print("\nFinished!\n\n==================================================")
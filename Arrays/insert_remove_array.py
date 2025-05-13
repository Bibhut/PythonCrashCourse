guest_lists = ["Rupendra", "Anuj" , "Binod" , "Samir"]
print(f"{guest_lists[0]}, your are invited for the dinner at 9:00pm.")
print(f"{guest_lists[1]}, your are invited for the dinner at 9:00pm.")
print(f"{guest_lists[2]}, your are invited for the dinner at 9:00pm.")
print(f"{guest_lists[3]}, your are invited for the dinner at 9:00pm.")


cancelled_guest = "Anuj"
print(f"\n{cancelled_guest} cannot make it to the dinner. So mahesh is invited. \n")
guest_lists.remove(cancelled_guest)
guest_lists.append("Mahesh")
print(f"{guest_lists[0]}, your are invited for the dinner at 9:00pm.")
print(f"{guest_lists[1]}, your are invited for the dinner at 9:00pm.")
print(f"{guest_lists[2]}, your are invited for the dinner at 9:00pm.")
print(f"{guest_lists[3]}, your are invited for the dinner at 9:00pm.")

print("\n i found a bigger dinner table so inviting new 3 guests. \n")
guest_lists.append("Biswash")
guest_lists.insert(0,"Umesh")
guest_lists.insert(2, "Ankit")

print(f"{guest_lists[0]}, your are invited for the dinner at 9:00pm.")
print(f"{guest_lists[1]}, your are invited for the dinner at 9:00pm.")
print(f"{guest_lists[2]}, your are invited for the dinner at 9:00pm.")
print(f"{guest_lists[3]}, your are invited for the dinner at 9:00pm.")
print(f"{guest_lists[4]}, your are invited for the dinner at 9:00pm.")
print(f"{guest_lists[5]}, your are invited for the dinner at 9:00pm.")
print(f"{guest_lists[6]}, your are invited for the dinner at 9:00pm.")

print("\n Dinner table wont arrive on time for dinner so need to remove two guests. \n")

guest_lists.pop()
guest_lists.pop()
guest_lists.pop()
guest_lists.pop()
guest_lists.pop()

print(f"{guest_lists[0]}, you are still invited.")
print(f"{guest_lists[1]}, you are still invited.")

del guest_lists[0]
del guest_lists[0] # Once del above , the new index for the new guest will be 0

print(guest_lists)
fav_destination_list = ["norway", "spain", "switzerland", "denmark"]
print("\n *****Original destination list is******* \n")
print(fav_destination_list)
print("\n *****sort list temporarily using sorted****** \n")
print(f"sorted list is {sorted(fav_destination_list)}")
print(fav_destination_list)
print("\n ***reverse list temporarily using sorted, reverse = true ***** \n")
print(f"{sorted(fav_destination_list,reverse=True)}")
print("\n *****Original destination list is still****** \n")
print(fav_destination_list)

print("\n ****After original list reverse**** \n")
fav_destination_list.reverse()
print(fav_destination_list)

print("\n ****After original list sorted***** \n")
fav_destination_list.sort()
print(fav_destination_list)

print("\n ****After original list sorted and reverse = true *****\n")
fav_destination_list.sort(reverse=True)
print(fav_destination_list)
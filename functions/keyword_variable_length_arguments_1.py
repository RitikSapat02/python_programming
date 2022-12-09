def details(id,**d):
    print(f"Details of id {id}:")
    for d,v in d.items():
        print(f"{d} is {v}")

details(222,name="Ritik",salary=874837878384374)
print()
details(14,name="Pratik",salary=95045475878384374)


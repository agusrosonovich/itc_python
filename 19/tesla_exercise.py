bought_tesla = True
year_of_tesla_purchase = 2000
is_US_citizen = True
current_year = 2018


if bought_tesla and is_US_citizen:
    if current_year-year_of_tesla_purchase <4:
        print("Would you like an upgrade?: ")
    else:
        print("Are you satisfied with your car?")
elif bought_tesla:
    print("Would you like to move to the US?: ")
else:
    print("Would you like to buy a brand new Tesla?")




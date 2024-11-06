AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
Auto = "******************************** \nAutoCountry Vehicle Finder v0.1 \n********************************\nPlease Enter the following number below from the following menu: \n1. PRINT all Authorized Vehicles\n2. Exit\n********************************"
print(Auto)


if int(input()) == 1:
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for allowed in AllowedVehiclesList:
        print(allowed)
    print(Auto)


elif int(input()) == 2:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
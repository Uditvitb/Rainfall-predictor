import model
def classifier(l):
    if l[0]==1:
        return "will Rain"
    elif l[0]==0:
        return "will not rain"
    else:
        return "error"

pressure=float(input("Enter the Pressure of the Region: "))
maxtemp=float(input("Enter the Maximum Temperture of the Region: "))
mintemp=float(input("Enter the Minimum Temperture of the Region: "))
temp=float(input("Enter the Actual Temperture of the Region: "))
humidity=float(input("Enter the humidity of the Region: "))
cloud=float(input("Enter the cloud data of the Region: "))
sunshine=float(input("Enter the Sunshine data of the Region: "))
wind_direction=float(input("Enter the wind_direction data of the Region: "))
windspeed=float(input("Enter the Wind Speed data of the Region: "))

l=model.prediction(model.ml,[[pressure,maxtemp,temp,mintemp,humidity,cloud,sunshine,wind_direction,windspeed]])
print(f"Model predicted: {classifier(l)}")
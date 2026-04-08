# Write your code here!
def temp_and_color(data):
    temp = None
    color = None 
    if "temp" in data:
        temp = data["temp"]      
    if "color" in data:
        color = data["color"]
    return (temp, color)
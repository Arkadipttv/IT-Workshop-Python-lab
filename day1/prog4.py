def calculate(total_cookies: int):
    cookies_per_box = 24
    boxes_per_container = 75
    full_boxes = total_cookies//cookies_per_box
    leftover_cookies = total_cookies%cookies_per_box
    full_containers = full_boxes//boxes_per_container
    leftover_boxes = full_boxes%boxes_per_container
    print("Total Number of boxes: ", full_boxes)
    print("Total Number of containers: ", full_containers)
    if(leftover_cookies>0):
        print("Leftover cookies: ", leftover_cookies)
    if(leftover_boxes>0):
        print("Leftover boxes: ", leftover_boxes)
def main():
    total_cookies = int(input("Enter the number of Cookies: "))
    calculate(total_cookies)
if __name__ == "__main__":
    main()
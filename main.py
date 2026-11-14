from datetime import date, timedelta, datetime

# Configuration
contentNo = int(input("Enter number of content/graphic: "))
duration = int(input("Enter duration of campaign(in days): "))

# Starting date
while True:
    try:
        date_str = input("Enter start date (MM/DD/YYYY): ")
        startDate = datetime.strptime(date_str, "%m/%d/%Y").date()
        #startDate = date.today()
        break

    except ValueError:
        print("Invalid date. Please use MM/DD/YYYY.")

if contentNo < 1:
    print("Error: At least 1 graphic is required.")

elif duration < 1:
    print("Error: Campaign duration must be positive.")

elif contentNo == 1:
    print("Only one graphic. Schedule on:", startDate)

else:
    # Calculate interval
    interval = duration / (contentNo - 1)

    print("Posting interval:", interval, "days")
    print("\nPosting Schedule:")

    for i in range(contentNo):
        postDate = startDate + timedelta(days=interval * i)
        print(f"Graphic {i + 1}: {postDate}")
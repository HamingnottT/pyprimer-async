def main():
    user_input = ""
    started = False

    while True:
        user_input = input(">").lower()

        if user_input == "start":
            if not started:
                print("Starting car...")
                started = True
            else:
                print("Car already started.")
        elif user_input == "stop":
            if started:
                print("Stopping car")
                started = False
            else:
                print("Car already stopped.")
        elif user_input == "help":
            print("""
            start - to start the car
            stop - to stop the car
            quit - to exit
            """)
            # print("start - to start the car\n" +
            # "stop - to stop the car\n" +
            # "quit - to exit\n")
        elif user_input == "quit":
            print("Exiting program. . .")
            break
        else:
            print("I don't understand that...")

if __name__ == '__main__':
    main()
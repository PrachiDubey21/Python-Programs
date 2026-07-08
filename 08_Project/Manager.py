import json

FILE_NAME = "youtube.txt"


# -------------------- File Handling --------------------

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(videos):
    with open(FILE_NAME, "w") as file:
        json.dump(videos, file, indent=4)


# -------------------- Display Videos --------------------

def list_videos(videos):

    print("\n" + "-" * 50)

    if not videos:
        print("No videos found.")
    else:
        for i, video in enumerate(videos, start=1):
            print(f"{i}. {video['name']}  |  Duration: {video['time']}")

    print("-" * 50)


# -------------------- Add Video --------------------

def add_video(videos):

    name = input("Enter video name: ")
    duration = input("Enter video duration: ")

    new_video = {
        "name": name,
        "time": duration
    }

    videos.append(new_video)
    save_data(videos)

    print("Video added successfully!")


# -------------------- Update Video --------------------

def update_video(videos):

    list_videos(videos)

    try:
        index = int(input("Enter video number to update: ")) - 1

        if 0 <= index < len(videos):

            videos[index]["name"] = input("Enter new name: ")
            videos[index]["time"] = input("Enter new duration: ")

            save_data(videos)
            print("Video updated successfully!")

        else:
            print("Invalid video number.")

    except ValueError:
        print("Please enter a valid number.")


# -------------------- Delete Video --------------------

def delete_video(videos):

    list_videos(videos)

    try:
        index = int(input("Enter video number to delete: ")) - 1

        if 0 <= index < len(videos):

            deleted_video = videos.pop(index)
            save_data(videos)

            print(f"{deleted_video['name']} deleted successfully!")

        else:
            print("Invalid video number.")

    except ValueError:
        print("Please enter a valid number.")


# -------------------- Main Menu --------------------

def main():

    videos = load_data()

    while True:

        print("\n===== YouTube Video Manager =====")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # if choice == "1":
        #     list_videos(videos)

        # elif choice == "2":
        #     add_video(videos)

        # elif choice == "3":
        #     update_video(videos)

        # elif choice == "4":
        #     delete_video(videos)

        # elif choice == "5":
        #     print("Goodbye!")
        #     break

        # else:
        #     print("Invalid choice. Please try again.")

        
        match choice:
            case '1':
                list_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")


# -------------------- Program Entry --------------------

if __name__ == "__main__":
    main()
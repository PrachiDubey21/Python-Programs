import sqlite3

# ---------------- Database Setup ------------------------------

DB_NAME = "youtube_videos.db"

# connection to the database
connection = sqlite3.connect(DB_NAME)

# cursor object
cursor = connection.cursor()

# creating table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
""")

connection.commit()


# --------------------------------------------------------------------

def list_videos():

    cursor.execute("SELECT * FROM videos")
      
    # for row in cursor.fetchall():
    #     print(row)

    videos = cursor.fetchall()

    print("\n" + "*" * 50)

    if not videos:
        print("No videos found.")

    else:
        print("ID\tName\t\tDuration")
        print("-" * 50)

        for video in videos:
            print(f"{video[0]}\t{video[1]}\t\t{video[2]}")

    print("*" * 50)


def add_video():

    name = input("Enter video name: ")
    duration = input("Enter video duration: ")

    cursor.execute(
        "INSERT INTO videos (name, time) VALUES (?, ?)",
        (name, duration)
    )

    # saves changes
    connection.commit()

    print("Video added successfully")


def update_video():

    list_videos()

    try:
        video_id = int(input("Enter video ID to update: "))

        new_name = input("Enter new video name: ")
        new_duration = input("Enter new video duration: ")

        cursor.execute(
            """
            UPDATE videos
            SET name = ?, time = ?
            WHERE id = ?
            """,
            (new_name, new_duration, video_id)
        )

        if cursor.rowcount == 0:
            print("No video found with that ID.")

        else:
            connection.commit()
            print("Video updated successfully!")

    except ValueError:
        print("Please enter a valid ID.")


def delete_video():

    list_videos()

    try:
        video_id = int(input("Enter video ID to delete: "))

        cursor.execute(
            "DELETE FROM videos WHERE id = ?",
            (video_id,)
        )

        if cursor.rowcount == 0:
            print("No video found with that ID.")

        else:
            connection.commit()
            print("Video deleted successfully!")

    except ValueError:
        print("Please enter a valid ID.")


# ----------------------------------------------------------------------

def main():

    while True:

        print("\n----------- YouTube Manager ---------------")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            add_video()

        elif choice == "3":
            update_video()

        elif choice == "4":
            delete_video()

        elif choice == "5":
            print("Exit")
            break

        else:
            print("Invalid choice. Please try again.")

    # closing database connection 
    connection.close()


# -----------------------------------

if __name__ == "__main__":
    main()
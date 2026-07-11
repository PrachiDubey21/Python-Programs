# pymongo is a Python library used to connect Python with MongoDB.

# MongoDB automatically creates IDs like
# 684fa42091d8c487f3e89342
# These are ObjectIds, not strings.
# Whenever you search using _id, MongoDB expects an ObjectId.

# MongoDB creates ID automatically.
# MongoDB operators begin with $

#--------------------------------------------------------------------------------

#We need to create an account on Atlas(MongoDB)

from pymongo import MongoClient
from bson import ObjectId

# -------------------- MongoDB Connection --------------------

# MONGO_URI = "mongodb+srv://<username>:<password>@<cluster-url>/"

# client = MongoClient(
#     MONGO_URI,
#     tlsAllowInvalidCertificates=True
# )

# for using localhost mongoDB
client = MongoClient("mongodb://localhost:27017/")

# database
database = client["ytmanager"]

# collection
video_collection = database["videos"]


# ---------------------------------------

def list_videos():

    videos = video_collection.find()

    print("\n" + "-" * 50)

    found = False

    for video in videos:
        found = True

        print(f"ID       : {video['_id']}")
        print(f"Name     : {video['name']}")
        print(f"Duration : {video['time']}")
        print("-" * 50)

    if not found:
        print("No videos found.")

    print("-" * 55)


def add_video():

    name = input("Enter video name: ")
    duration = input("Enter video duration: ")

    video_collection.insert_one({
        "name": name,
        "time": duration
    })

    print("Video added successfully")


def update_video():

    list_videos()

    try:
        video_id = input("Enter video ID to update: ")

        new_name = input("Enter new video name: ")
        new_duration = input("Enter new video duration: ")

        result = video_collection.update_one(
            {"_id": ObjectId(video_id)},
            {
                "$set": {
                    "name": new_name,
                    "time": new_duration
                }
            }
        )

        if result.modified_count > 0:
            print("Video updated successfully")
        else:
            print("No video found with that ID")

    except Exception:
        print("Invalid Object ID")


def delete_video():

    list_videos()

    try:
        video_id = input("Enter video ID to delete: ")

        result = video_collection.delete_one(
            {
                "_id": ObjectId(video_id)
            }
        )

        if result.deleted_count > 0:
            print("Video deleted successfully")
        else:
            print("No video found with that ID")

    except Exception:
        print("Invalid Object ID")


# ----------------------------------------

def main():

    while True:

        print("\n------------- YouTube Manager ------------------")
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
            print("Thank you for using YouTube Manager")
            break

        else:
            print("Invalid choice, Please try again")

    client.close()


# ---------------------------------------

if __name__ == "__main__":
    main()
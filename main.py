# from typing import List, Tuple

# # A Song has
# # - a title
# # - a primary artist name
# # - a list of other associated artists' names
# # - an album title
# # - a duration (in seconds)
# # - a boolean indicating whether or not it is a favorite song
# Song = Tuple[str, str, List[str], str, int, bool]


# def find_all_favorites(songs: List[Song]) -> List[Song]:
#     favorites = []
#     for song in songs:
#         if song[5] == True:
#             favorites.append(song)
#     return favorites


# def find_all_by_artist(songs: List[Song], name: str) -> List[Song]:
#     fromArtist = []
#     for song in songs:
#         if name in song[1] or name in song[2]:
#             fromArtist.append(song)
#     return fromArtist


# def find_all_shorter_than(songs: List[Song], duration: int) -> List[Song]:
#     shorterSongs = []
#     for song in songs:
#         if song[4] < duration:
#             shorterSongs.append(song)
#     return shorterSongs

# def myFunction():
#     print("Yolo, fam!")


from typing import List


def collect_blessings() -> List[str]:
    blessings = []
    while True:
        user_input = input(
            "Enter the things you are thankful for or enter 'q' to quit.\n> ")
        if user_input.lower() == 'q':
            break
        blessings.append(user_input)
    return blessings


def display_blessings(blessings: List[str]):
    count = len(blessings)
    print(f"Wow! You're thankful for {count} things!")
    print("Here they are again:")
    for item in blessings:
        print(item)


def main():
    print("Welcome to Count Your Blessings")
    blessings = collect_blessings()
    display_blessings(blessings)


if __name__ == '__main__':
    main()

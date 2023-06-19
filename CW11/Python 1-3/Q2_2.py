import argparse
import os
import time

def list_files(path, show_size=False, show_modified_time=False):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(item_path + os.sep)
            list_files(item_path, show_size, show_modified_time)
        else:
            if show_size:
                size = os.path.getsize(item_path) // 1024  # Convert bytes to KB
                size_str = f" (Size: {size} KB)"
            else:
                size_str = ""
            if show_modified_time:
                modified_time = time.localtime(os.path.getmtime(item_path))
                modified_time_str = f" (Modified: {time.strftime('%Y-%m-%d %H:%M:%S', modified_time)})"
            else:
                modified_time_str = ""
            print(item_path + size_str + modified_time_str)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="List all files and subdirectories within a directory.")
    parser.add_argument('path', help="Directory path")
    parser.add_argument('--size', action='store_true', help="Show the size of files in KB")
    parser.add_argument('--modified-time', action='store_true', help="Show the last modified time of files")
    args = parser.parse_args()

    list_files(args.path, args.size, args.modified_time)
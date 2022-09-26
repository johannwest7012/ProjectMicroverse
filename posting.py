import fnmatch
import os

import random
import shutil

import instaloader
from instabot import Bot
from instaloader import Instaloader, Profile
from datetime import datetime
from itertools import dropwhile, takewhile, islice
from math import ceil
import instaloader
from os.path import exists


def get_jpgs_from_direct(directory, jpg_path_list):
    for dirpath, dirs, files in os.walk("C:\\Users\\Johan\\Documents\\Python Projects\\ProjectMicroverse\\" + str(directory)):
        for filename in fnmatch.filter(files, '*.jpg'):
            print(os.path.join(dirpath, filename))
            jpg_path_list.append(os.path.join(dirpath, filename))

    return jpg_path_list


def main():
    print()

    # config file causes error, remove it before logging in
    if exists("C:\\Users\\Johan\\Documents\\Python Projects\\ProjectMicroverse\\config"):
        shutil.rmtree("C:\\Users\\Johan\\Documents\\Python Projects\\ProjectMicroverse\\config")

    #folders to pull from
    FOLDERS = ['epic.png', 'inhalemybees']

    jpg_path_list = []
    for folder in FOLDERS:
        jpg_path_list = get_jpgs_from_direct(folder, jpg_path_list)

    print("path list", jpg_path_list)

    # shuffles list so you are not posting back to back pics from the same source
    random.shuffle(jpg_path_list)

    bot = Bot()
    bot.login(username="usernamehere", password="passwordhere")

    # for loop this later
    for i in range(len(jpg_path_list) - 1):
        path = jpg_path_list.pop(0)

        # input caption later
        bot.upload_photo(path)

        # delete after posting
        shutil.rmtree(path)


if __name__ == '__main__':
    main()

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






#date range of posts to pull
SINCE = datetime(2022, 4, 10)
UNTIL = datetime(2022, 4 ,26)

def getPosts(MASTER_LIST):
    # instaloader
    L = instaloader.Instaloader()  # instaloader access
    # #login to your recon_account to scrap private accounts you follow
    L.login("reconbot7012", "JW22kicker")

    # get the list of people your Recon Account follows
    recon_profile = Profile.from_username(L.context, "reconbot7012")

    # List of usernames

    # for i in recon_profile.get_followees():
    #     MASTER_LIST.append(i.username)

    print(MASTER_LIST)
    for username in MASTER_LIST:
        profile = Profile.from_username(L.context, username)
        post_count = profile.get_posts().count
        #fethcing total likes
        likes = 0
        view_count = 0
        comments = 0

        video_count = 0
        pic_count = 0
        for post in profile.get_posts():
            comments += post.comments
            if post.is_video:
                video_count += 1
                view_count += post.video_view_count

            else:
                pic_count += 1
                likes += post.likes

        print("Likes:",likes)
        print("Video Views:", view_count)

        average_likes = likes / pic_count
        average_views = view_count / video_count

        k= 0
        count = 0
        for post in profile.get_posts():
            print(count)
            count += 1
            postdate = post.date
            if postdate > UNTIL:
                continue
            elif postdate <= SINCE:
                k += 1
                if k == 100:
                    break
                else:
                    continue
            else:
                print("Within time frame")
                #download if above average
                if post.is_video:
                    print("Video view", post.video_view_count)
                    print("Average views", average_views)
                    if post.video_view_count > average_views:
                        L.download_post(post, username)

                else:
                    print("Postlikes", post.likes)
                    print("Averagelikes", average_likes)
                    if post.likes > average_likes:
                        L.download_post(post, username)
                k = 0





def main():
    print()
    # config file causes error, remove it before logging in
    if exists("C:\\Users\\Johan\\Documents\\Python Projects\\ProjectMicroverse\\config"):
        shutil.rmtree("C:\\Users\\Johan\\Documents\\Python Projects\\ProjectMicroverse\\config")

    # create you database of posts
    MASTER_LIST = ['epic.png', 'inhalemybees']

    getPosts(MASTER_LIST)


if __name__ == '__main__':
    main()


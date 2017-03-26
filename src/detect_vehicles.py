#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to run in order to detect vehicles in a video

@author: Carlton Joseph
"""
import utils
import argparse
import config
from moviepy.editor import VideoFileClip


def video(args):
    """video detection function"""

    videos_in = config.get_videos(args.id)
    
    channels, ssahbs, colors = config.get_channel_ssahb_color(args.cfg)
    channel, ssahb, color = utils.check_singles(channels, ssahbs, colors)
    heat_only = False
    bs = args.ds=="big"
    detect = utils.detect(channel, ssahb, color, bs, heat_only)
    
    for video_in in videos_in:
        video_out = utils.get_video_out(video_in, channel, ssahb, color, bs)
        print("From =>", video_in, "To =>", video_out)

        clip2 = VideoFileClip(video_in)
        clip = clip2.fl_image(detect.cars)
        clip.write_videofile(video_out, audio=False)

def train(args):
    """train the classifiers"""
    
    utils.gen_trained_sets(args.ds == 'big', args.cfg)

def main():
    """Main vehicle detection function"""
    parser = argparse.ArgumentParser(description='Process video file or train svm.')

    subparsers = parser.add_subparsers(help='Process video file')

    parser_a = subparsers.add_parser('video', help='Video file processing seletion')
    parser_a.set_defaults(func=video)
    parser_a.add_argument('-i', '--id', help="video sequence", required=True, type=int, 
                          choices=range(1, len(config.videos) + 1))

    parser_b = subparsers.add_parser('train', help='train the classifier')
    parser_b.set_defaults(func=train)

    parser.add_argument('-d','--ds', help="dataset to use for training", 
                          choices=['big', 'small'], required=True)
    parser.add_argument('-c','--cfg', help="training configuration options", 
                          type=int, required=True, 
                          choices=range(1, len(config.channel_ssahb_color) + 1))

    args = parser.parse_args()
    if len(vars(args)) == 0:
        parser.print_help()
        return
    
    args.func(args)

if __name__ == "__main__":
    main()

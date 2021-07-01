"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.status         = None
        self.paused         = False
        """Note: the status of a player can be
        1. None             : the initial state, or state when any played video is stopped 
        2. <title>          : title of the current video playing
        # 3. <title_paused>   : title of any played video when paused
        """

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos: ")

        videos = self._video_library.get_all_videos()
        # sort videos by titles
        sorted_videos = sorted(videos, key = lambda x: x.title)
        for video in sorted_videos:
            print(f"  {video.title} ({video.video_id}) [{' '.join([tag for tag in video.tags])}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        if video_id in (video.video_id for video in self._video_library.get_all_videos()):
            if self.status is None:
                self.status = self._video_library.get_video(video_id).title
                print(f"Playing video: {self.status}")
            elif self._video_library.get_video(video_id) is not None:
                print(f"Stopping video: {self.status}")
                self.paused = False
                self.status = self._video_library.get_video(video_id).title
                print(f"Playing video: {self.status}")
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.status is not None:
            print(f"Stopping video: {self.status}")
            self.paused = False
            self.status = None
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        if len(self._video_library.get_all_videos())==0:
                print('No videos available')
        else:
            random_id = random.choice(self._video_library.get_all_videos()).video_id
            if self.status is not None:
                print(f"Stopping video: {self.status}")
            self.paused = False
            self.status = self._video_library.get_video(random_id).title
            print(f"Playing video: {self.status}")

    def pause_video(self):
        """Pauses the current video."""
        if self.status is not None:
            if self.paused is False:
                print(f"Pausing video: {self.status}")
                self.paused = True
            elif self.paused is True:
                print(f"Video already paused: {self.status}")
        elif self.status is None:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.status is not None: # video playing
            if self.paused is True:
                print(f"Continuing video: {self.status}")
                self.paused = False
            elif self.paused is not True:
                print(f"Cannot continue video: Video is not paused")
        elif self.status is None: # no video playing
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        videos = self._video_library.get_all_videos()

        if self.status is not None: # video playing
            now_vid = next(video for video in videos if video.title == self.status)
            print(f"Currently playing: {now_vid.title} ({now_vid.video_id}) [{' '.join([tag for tag in now_vid.tags])}]{' - PAUSED' if self.paused is True else ''}")
        elif self.status is None: # no video playing
            print("No video is currently playing")
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

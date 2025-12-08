import ffmpeg
import rapidfuzz
import pandas as pd
from collections import Counter

class Logic_Handler():
    @staticmethod
    def has_cover_art(info):
        streams = info.get("streams", [])
        for s in streams:
            if s.get("codec_type") == "video":
                if s.get("disposition", {}).get("attached_pic") == 1:
                    return True
        return False
    
    @staticmethod
    def has_lyrics(audio):
        tags = audio.get("format", {}).get("tags", {})
        if any(k.lower().startswith("lyrics") for k in tags):
            return True
        return False
    
    @staticmethod
    def basic_duplicates_handler(music_dir, highest_bit_rate_only=False):
        keep = {}
        highest_bit_rate = 0
        files_with_max_bit_rate = []
        for file in music_dir:
            criteria = 0
            audio = ffmpeg.probe(str(file))
            bit_rate = int(audio['streams'][0]['bit_rate'])
          
            if not highest_bit_rate_only:
                if Logic_Handler.has_lyrics(audio):
                    criteria += 2
                if Logic_Handler.has_cover_art(audio):
                    criteria += 1

            if bit_rate > highest_bit_rate:
                highest_bit_rate = bit_rate
                files_with_max_bit_rate = [file]
            elif bit_rate == highest_bit_rate:
                files_with_max_bit_rate.append(file)
            keep[file] = criteria

        for f in files_with_max_bit_rate:
            keep[f] += 1
        file_dir_to_keep, __ = max(keep.items(), key=lambda x: (x[1], -len(str(x[0]))))
        return file_dir_to_keep

    @staticmethod
    def is_extract_match(str1, str2):
        return str1==str2

    @staticmethod
    def special_duplicates_handler(FILE_NAMES):
        # implements fuzzy clustering
        for name in FILE_NAMES:
            audio = ffmpeg.probe(name)
            artist_name = audio.get('format').get('tags', {}).get('artist', {})
            title = audio.get('format').get('tags', {}).get('title', {})
            album = audio.get('format').get('tags', {}).get('album', {})
            date = audio.get('format').get('tags', {}).get('date', {})
        pd.DataFrame({
            'artist_name': artist_name,
            'title': title,
            'album': album,
            'date': date
        })

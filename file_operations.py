from logic_handler import Logic_Handler
from pathlib import Path
import os
import re


class file_operations:
    @staticmethod
    def _get_duplicated_files(self, special_duplicates=False):
        FILE_NAMES = os.listdir(self.input_Path)
        clean_map = {}

        if not special_duplicates:
            for name in FILE_NAMES:
                name_without_stem = re.sub(r"[., _-]", "", Path(name).stem)
                clean_map.setdefault(name_without_stem, []).append(name)
        else:
            return Logic_Handler.special_duplicates_handler(FILE_NAMES)

        return {
            clean_stem: [Path(self.input_Path) / fname for fname in filenames]
            for clean_stem, filenames in clean_map.items()
            if len(filenames) > 1
        }
     
    @staticmethod
    def _get_sorted_items(self, duplicated_files, seeDetails=True, highest_bit_rate_only=False):
        final_items = {}
        for song_name, duplicated_file in duplicated_files.items():
            # prioritize file with lyrics, album cover, high bit rate
            final_items[song_name] =  Logic_Handler.basic_duplicates_handler(duplicated_file, highest_bit_rate_only)
        if seeDetails:
            print(final_items)
        return final_items
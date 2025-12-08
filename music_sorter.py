from pathlib import Path
import argparse
from file_operations import file_operations


class Music_Sorter():
    def __init__(self, input_Path, output_Path):    
        self.input_Path = input_Path
        self.output_Path = output_Path
        if self.input_Path is None:
            self.input_Path = "tmp_dir"
        if self.output_Path is None:
            self.output_Path = "output"
        Path(self.input_Path).mkdir(parents=True ,exist_ok=True)
        
    
    def _file_mover(self, items_list):
        Path(self.output_Path).mkdir(parents=True ,exist_ok=True)   
        for source in items_list.values():
            destination = Path(self.output_Path) / source.name
            source.rename(destination)

    def start_sorting(self, highest_bit_rate_only):
        if highest_bit_rate_only is None:
            highest_bit_rate_only = False
        duplicated_files = file_operations._get_duplicated_files()
        sorted_duplicated_files = file_operations._get_sorted_items(duplicated_files, highest_bit_rate_only)
        self._file_mover(sorted_duplicated_files)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--output")
    parser.add_argument("--bitrateonly")
    args = parser.parse_args()

    ms = Music_Sorter(args.input, args.output)
    ms.start_sorting(args.bitrateonly)
    print("============\nSuccess!")
            
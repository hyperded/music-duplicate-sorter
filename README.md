
1. **Group duplicates**  
   - Files are grouped by “same song name” (ignoring punctuation, spaces, underscores, etc.)

2. **Score files**  
   - For each group of duplicates, files are scored based on:
     - **Embedded lyrics** → +2
     - **Highest bit rate** → +1
     - **Album cover** → +1

3. **Resolve ties**  
   - If multiple files have the same score, the file with the **shortest filename** is chosen.

4. **Move files**  
   - The selected "best" file for each song is moved to the **output folder**.

---

## Usage

```bash
python amogus.py --input <input_folder> --output <output_folder>

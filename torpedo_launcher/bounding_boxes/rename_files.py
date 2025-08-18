import os

def rename_frames_sequentially_from_number(folder_path, start_number):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]
    files.sort()

    for i, old_name in enumerate(files):
        old_path = os.path.join(folder_path, old_name)
        tmp_path = os.path.join(folder_path, f'tmp_{i}.jpg')
        os.rename(old_path, tmp_path)

    tmp_files = [f for f in os.listdir(folder_path) if f.startswith('tmp_') and f.endswith('.jpg')]
    tmp_files.sort()

    for i, tmp_name in enumerate(tmp_files):
        tmp_path = os.path.join(folder_path, tmp_name)
        final_path = os.path.join(folder_path, f'{start_number + i}.jpg')
        os.rename(tmp_path, final_path)

    print(f"Renamed {len(files)} .jpg files in '{folder_path}' starting from {start_number}.")

folder_path = '/home/pranav/Documents/train'
#start_number = 0
#rename_frames_sequentially_from_number(folder_path, start_number)

import os
import shutil

def organize_folders():
    # 바탕화면 경로
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # MP, REL 폴더 생성
    mp_folder = os.path.join(desktop_path, "MP")
    rel_folder = os.path.join(desktop_path, "REL")
    os.makedirs(mp_folder, exist_ok=True) ## 디렉토리 생성
    os.makedirs(rel_folder, exist_ok=True) 
    
    # 1과 2 폴더를 REL로 이동
    for item_name in ["1", "2"]:
        item_path = os.path.join(desktop_path, item_name)
        if os.path.exists(item_path):
            shutil.move(item_path, rel_folder)
    
    # 3 파일을 MP로 이동
    file3_path = os.path.join(desktop_path, "3.txt")
    if os.path.exists(file3_path):
        shutil.move(file3_path, mp_folder)
        new_file_name = "product.txt"  # 변경될 파일 이름
        new_file_path = os.path.join(mp_folder, new_file_name) ## 변경된 이름을 새롭게 경로 지정
        os.rename(os.path.join(mp_folder, "3.txt"), new_file_path) ## 실제 값으로 변경 적용
    

    # REL 폴더 안의 폴더 이름 변경 및 바로가기 생성
    for folder in os.listdir(rel_folder):
        if folder == "1":
            new_folder_name = "변경하는 이름" # 변경될 폴더 이름 (1번 폴더는 "T0", 2번 폴더는 "ORT")
            folder_path = os.path.join(rel_folder, folder)
            new_folder_path = os.path.join(rel_folder, new_folder_name)
            os.rename(folder_path, new_folder_path)


        if folder == "2":
            new_folder_name = "변경하는 탸그" # 변경될 폴더 이름 (1번 폴더는 "T0", 2번 폴더는 "ORT")
            folder_path = os.path.join(rel_folder, folder)
            new_folder_path1 = os.path.join(rel_folder, new_folder_name)
            os.rename(folder_path, new_folder_path1)        

if __name__ == "__main__":
    organize_folders()

import re

def solution(folders, files, selected, excepted):
    # 폴더를 dict 으로 변환
    folder_dict = {}
    for folder in folders:
        child, parent = folder

        # root 아래 여러 폴더가 있을 수 있으니까, 부모 밑에 여러 자식 폴더가 리스트 형태로 저장될 수 있도록.
        if parent not in folder_dict:
            folder_dict[parent] = []
        folder_dict[parent].append(child)

    all_file_size = 0
    all_file_count = 0
    
    # 폴더를 선택하고 하위 파일들을 탐색하며 정보를 반환받는다.
    for selected_folder in selected:
        for file in file_info(selected_folder, folder_dict, files, excepted):
            get_file_size, get_file_unit = re.match(r'(\d+)(\w+)', file[1]).groups()

            if get_file_unit == 'B':
                all_file_size += int(get_file_size)

            elif get_file_unit == 'KB':
                all_file_size += int(get_file_size) * 1024

            all_file_count += 1

    return [all_file_size, all_file_count]

def file_info(folder, folder_dict, files, excepted):
    result = []

    for child in folder_dict.get(folder, []):
        result += file_info(child, folder_dict, files, excepted)

    for file in files:
        file_name, file_size, parent = file
        if parent == folder and file_name not in excepted:
            result.append(file)

    return result

print(solution(folders=[['animal', 'root'], ['fruit', 'root']],
               files=[['cat', '1B', 'animal'], ['dog', '2B', 'animal'], ['apple', '4B', 'fruit']],
               selected=['animal'],
               excepted=['apple']))


print(solution(folders=[['food', 'root'], ['meet', 'food'], ['fruit', 'food'], ['animal', 'root']],
               files=[['cat', '1B', 'animal'], ['dog', '2B', 'animal'], ['fork', '1KB', 'meat'], ['beef', '8KB', 'meat'], ['apple', '4B', 'fruit'], ['fire', '83B', 'root']],
               selected=['root', 'meat'],
               excepted=['fork', 'apple']))
from pprint import pprint
from ya_disk import YandexDisk
TOKEN=""

ya = YandexDisk(token=TOKEN)
pprint(ya.get_files_list())
ya.upload_file_to_disk("Задания/NetoTest.txt", "test.txt")
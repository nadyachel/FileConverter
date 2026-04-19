import os
from converter.facade import BatchConverterFacade

def main():
    print("=== Универсальный Конвертер Файлов ===")
    input_dir = input("Введите путь к папке с исходными файлами: ").strip()
    output_dir = input("Введите путь к папке для сохранения: ").strip()
    target_format = input("Введите целевой формат (например, jpg, png, json): ").strip()
    
    if target_format in ['jpg', 'jpeg', 'webp']:
        quality = input("Введите качество (1-100, по умолчанию 100): ").strip()
        settings = {'quality': int(quality) if quality.isdigit() else 100}
    else:
        settings = {}

    if not os.path.exists(input_dir):
        print("Ошибка: Входная папка не существует.")
        return

    converter = BatchConverterFacade(input_dir, output_dir)
    print("\nНачинаю пакетную конвертацию...")
    converter.convert_batch(target_format, **settings)

if __name__ == "__main__":
    main()
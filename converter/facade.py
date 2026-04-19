import os
from .factory import ConverterFactory

class BatchConverterFacade:
    """Фасад для упрощения пакетной конвертации файлов."""
    
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = input_dir
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def convert_batch(self, target_ext: str, **kwargs):
        """Пакетная конвертация всех поддерживаемых файлов в целевой формат."""
        target_ext = target_ext.lower()
        if not target_ext.startswith('.'):
            target_ext = f'.{target_ext}'

        success_count = 0
        error_count = 0

        for filename in os.listdir(self.input_dir):
            input_path = os.path.join(self.input_dir, filename)
            if not os.path.isfile(input_path):
                continue

            name, ext = os.path.splitext(filename)
            output_path = os.path.join(self.output_dir, f"{name}{target_ext}")

            try:
                converter = ConverterFactory.get_converter(ext.lower(), target_ext)
                converter.convert(input_path, output_path, **kwargs)
                print(f"[OK] {filename} -> {os.path.basename(output_path)}")
                success_count += 1
            except ValueError as e:
                # Пропускаем неподдерживаемые файлы
                pass
            except Exception as e:
                print(f"[ERROR] Ошибка конвертации {filename}: {e}")
                error_count += 1

        print(f"\nКонвертация завершена! Успешно: {success_count}, Ошибок: {error_count}")
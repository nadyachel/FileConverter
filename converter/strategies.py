from abc import ABC, abstractmethod
import os
import json
import csv
from PIL import Image

class IConverterStrategy(ABC):
    """Интерфейс для всех стратегий конвертации."""
    @abstractmethod
    def convert(self, input_path: str, output_path: str, **kwargs):
        pass

class ImageConverter(IConverterStrategy):
    """Конвертер изображений (PNG, JPG, WEBP). Поддерживает настройку качества."""
    def convert(self, input_path: str, output_path: str, **kwargs):
        quality = kwargs.get('quality', 100)
        with Image.open(input_path) as img:
            # Конвертация в RGB (убираем альфа-канал, если сохраняем в JPG)
            if img.mode in ("RGBA", "P") and output_path.lower().endswith('.jpg'):
                img = img.convert("RGB")
            img.save(output_path, quality=quality)

class CsvToJsonConverter(IConverterStrategy):
    """Конвертер текстовых данных (CSV в JSON)."""
    def convert(self, input_path: str, output_path: str, **kwargs):
        indent = kwargs.get('indent', 4)
        with open(input_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        with open(output_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=indent, ensure_ascii=False)
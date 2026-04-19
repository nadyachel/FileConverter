from .strategies import IConverterStrategy, ImageConverter, CsvToJsonConverter

class ConverterFactory:
    """Фабрика для выбора подходящей стратегии конвертации."""
    
    @staticmethod
    def get_converter(input_ext: str, output_ext: str) -> IConverterStrategy:
        image_formats =['.png', '.jpg', '.jpeg', '.webp']
        
        if input_ext in image_formats and output_ext in image_formats:
            return ImageConverter()
        elif input_ext == '.csv' and output_ext == '.json':
            return CsvToJsonConverter()
        else:
            raise ValueError(f"Конвертация из {input_ext} в {output_ext} не поддерживается.")
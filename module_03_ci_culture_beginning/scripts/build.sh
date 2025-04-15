#!/bin/bash

# Переходим в корень проекта (из scripts в python_advanced_3)
cd "$(dirname "$0")/../.."

# Устанавливаем PYTHONPATH, чтобы Python видел модули проекта
export PYTHONPATH=$(pwd)

# Пути к файлам
program_file="./module_03_ci_culture_beginning/homework/hw2/decrypt.py"
test_file="./module_03_ci_culture_beginning/materials/previous_hw_test/tests/test_decrypt.py"

# Указываем директорию для отчётов (прямой путь в нужную папку)
reports_dir="./module_03_ci_culture_beginning/reports"  # Папка reports внутри module_03_ci_culture_beginning
pylint_report="$reports_dir/pylint_report_$(date +%Y%m%d_%H%M%S).json"

# Разделитель для вывода
divider="------------------------------------"

# Создаём папку для отчётов, если не существует
mkdir -p "$reports_dir"

# 🔍 Pylint
echo -e "${BLUE}🔍 Статический анализ файла $program_file...${NC}"
echo -e "${divider}"
pylint "$program_file" --output-format=json --reports=y > "$pylint_report"
pylint_res=$?

if [[ pylint_res -eq 0 ]]; then
  echo -e "${GREEN}✅ Pylint: Код прошёл анализ без ошибок.${NC}"
else
  echo -e "${RED}❌ Pylint нашёл ошибки в коде. Отчёт сохранён в $pylint_report${NC}"
  exit 1
fi

echo -e "${divider}"

# 🚀 Тесты
echo -e "${BLUE}🚀 Запуск юнит-тестов для файла $test_file...${NC}"
echo -e "${divider}"
python -m unittest "$test_file"
test_res=$?

if [[ test_res -eq 0 ]]; then
  echo -e "${GREEN}✅ Тесты прошли успешно!${NC}"
else
  echo -e "${RED}❌ Некоторые тесты не прошли. Проверьте их выше.${NC}"
  exit 1
fi

echo -e "${divider}"
echo -e "${GREEN}✅ Сборка завершена успешно!${NC}"

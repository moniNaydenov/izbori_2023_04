# Анализ на протоколи от ЦИК

Този проект анализира протоколите от Централната избирателна комисия (ЦИК). Следвайте тези стъпки, за да извършите анализа:

1. Изтеглете data.js от тук [https://results.cik.bg/ns2023/protokoli/data.js](https://results.cik.bg/ns2023/protokoli/data.js)
2. Запазете файла като `protokoli.js` в папката `data`
3. Изпълнете следната команда: `python parse_js.py`
4. След това изпълнете следната команда: `python fetch_protocols.py`
5. След това изпълнете следната команда: `python convert_results_to_json.py`
6. Накрая изпълнете следната команда: `python calculate_results_from_json.py`
7. Крайният резултат е json със следните данни (за всяка партия):
   1. auto_machine - общият брой гласове от машините от флаш паметта
   2. human_machine - общият брой гласове от машините, както са въведени в крайния протокол
   3. human_paper - общият брой гласове от хартиени бюлетини, както са въведени в крайния протокол
   4. human_total - общият брой гласове (и от машините, и от хартията) въведени в крайния протокол
   5. calculated_total - общият брой гласове (и от машините, и от хартията), изчислен от сумата на auto_machine + human_paper
   6. calculated_human_total - общият брой гласове (и от машините, и от хартията), изчислен от сумата на human_machine + human_paper
   7. human_total_percent - процент на гласовете от human_total
   8. calculated_total_percent - процент на гласовете от calculated_total
   9. calculated_human_total_percent - процент на гласовете от calculated_human_total

Анализ на разликата в резултатите между крайния протокол и протокола от флаш паметта на машините (броени само секции, в които е прочетена флаш паметта): [https://docs.google.com/spreadsheets/d/1GzoXYVOkIJ15SO6_rKPmlNySLLVbF3OQjiKgYzf_Hyk/edit#gid=0](https://docs.google.com/spreadsheets/d/1GzoXYVOkIJ15SO6_rKPmlNySLLVbF3OQjiKgYzf_Hyk/edit#gid=0)
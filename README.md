# Анализ на протоколи от ЦИК

This project analyzes the protocols from the Central Election Commission (ЦИК). Follow these steps to perform the analysis:

1. Open `parse_js.html`.
2. Copy and save the URLs in `data/urls.txt`.
3. Run the following command in your terminal or command prompt: `python fetch_protocols.py`
4. Next, run the following command: `python convert_results_to_json.py`
5. Finally, run the following command: `python calculate_results_from_json.py`

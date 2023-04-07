# Анализ на протоколи от ЦИК

This project analyzes the protocols from the Central Election Commission (ЦИК). Follow these steps to perform the analysis:

1. Download data.js from here [https://results.cik.bg/ns2023/protokoli/data.js](https://results.cik.bg/ns2023/protokoli/data.js)
2. Save the file as `protokoli.js` in the `data` folder
3. Run the following command in your terminal or command prompt: `python parse_js.py`
4. Next, run the following command: `python fetch_protocols.py`
5. Next, run the following command: `python convert_results_to_json.py`
6. Finally, run the following command: `python calculate_results_from_json.py`

You can find summarized results here - [https://docs.google.com/spreadsheets/d/1GzoXYVOkIJ15SO6_rKPmlNySLLVbF3OQjiKgYzf_Hyk/edit#gid=0](https://docs.google.com/spreadsheets/d/1GzoXYVOkIJ15SO6_rKPmlNySLLVbF3OQjiKgYzf_Hyk/edit#gid=0)

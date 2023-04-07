# Анализ на протоколи от ЦИК

This project analyzes the protocols from the Central Election Commission (ЦИК). Follow these steps to perform the analysis:

1. Download data.js from here [https://results.cik.bg/ns2023/protokoli/data.js](https://results.cik.bg/ns2023/protokoli/data.js)
2. Save the file as `protokoli.js` in the `data` folder
3. Run the following command in your terminal or command prompt: `python parse_js.py`
4. Next, run the following command: `python fetch_protocols.py`
5. Next, run the following command: `python convert_results_to_json.py`
6. Finally, run the following command: `python calculate_results_from_json.py`
7. Final result is json with the following data (for each Party):
   1. auto_machine - total number of votes from machines from flash memory
   2. human_machine - total number of votes from machines as entered in the final protocol
   3. human_paper - total number of votes from paper ballots as entered in the final protocol
   4. human_total - total number of votes (both machine and paper) as entered in the final protocol
   5. calculated_total - total number of votes (both machine and paper) calculated from sum of auto_machine + human_paper
   6. calculated_human_total - total number of votes (both machine and paper) calculated from sum of human_machine + human_paper
   7. human_total_percent - percentage of votes from human_total
   8. calculated_total_percent - percentage of votes from calculated_total
   9. calculated_human_total_percent - percentage of votes from calculated_human_total

You can find summarized results here - [https://docs.google.com/spreadsheets/d/1GzoXYVOkIJ15SO6_rKPmlNySLLVbF3OQjiKgYzf_Hyk/edit#gid=0](https://docs.google.com/spreadsheets/d/1GzoXYVOkIJ15SO6_rKPmlNySLLVbF3OQjiKgYzf_Hyk/edit#gid=0)

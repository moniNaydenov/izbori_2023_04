import json

RESULTS = {}
def load_data_from_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def calculate_results(data):
    count = 0
    for sectionnum, sectiondata in data.items():
        for partyid in range(1, 22):
            #if "auto_machine" not in sectiondata: # if there is no machine data from flash memory for this section, ignore it
            #    continue
            auto_machine = 0
            if "auto_machine" in sectiondata and str(partyid) in sectiondata["auto_machine"]:
                auto_machine = int(sectiondata["auto_machine"][str(partyid)])
            human_machine = 0
            if "human_machine" in sectiondata and str(partyid) in sectiondata["human_machine"]:
                human_machine = int(sectiondata["human_machine"][str(partyid)])
            human_paper = 0
            if "human_paper" in sectiondata and str(partyid) in sectiondata["human_paper"]:
                human_paper = int(sectiondata["human_paper"][str(partyid)])
            human_total = 0
            if "human_total" in sectiondata and str(partyid) in sectiondata["human_total"]:
                human_total = int(sectiondata["human_total"][str(partyid)])
            calculated_total = auto_machine + human_paper
            calculated_human_total = human_machine + human_paper
            RESULTS[str(partyid)]["auto_machine"] += auto_machine
            RESULTS[str(partyid)]["human_machine"] += human_machine
            RESULTS[str(partyid)]["human_paper"] += human_paper
            RESULTS[str(partyid)]["human_total"] += human_total
            RESULTS[str(partyid)]["calculated_total"] += calculated_total
            RESULTS[str(partyid)]["calculated_human_total"] += calculated_human_total

        count += 1

def calculate_percent():
    total = {}
    for partyid, partydata in RESULTS.items():
        total["human_total"] = 0
        total["calculated_total"] = 0
        total["calculated_human_total"] = 0
    for partyid, partydata in RESULTS.items():
        total["human_total"] += partydata["human_total"]
        total["calculated_total"] += partydata["calculated_total"]
        total["calculated_human_total"] += partydata["calculated_human_total"]
    for partyid, partydata in RESULTS.items():
        partydata["human_total_percent"] = round(partydata["human_total"] / total["human_total"] * 100, 2)
        partydata["calculated_total_percent"] = round(partydata["calculated_total"] / total["calculated_total"] * 100, 2)
        partydata["calculated_human_total_percent"] = round(partydata["calculated_human_total"] / total["calculated_human_total"] * 100, 2)



if __name__ == '__main__':
    for i in range(0, 21):
        partyid = str(i+1)
        RESULTS[partyid] = {}
        RESULTS[partyid]["auto_machine"] = 0
        RESULTS[partyid]["human_machine"] = 0
        RESULTS[partyid]["human_paper"] = 0
        RESULTS[partyid]["human_total"] = 0
        RESULTS[partyid]["calculated_total"] = 0
        RESULTS[partyid]["calculated_human_total"] = 0

    input_file_path = './data/results.json'
    data = load_data_from_json_file(input_file_path)

    calculate_results(data)
    calculate_percent()
    formatted_data = json.dumps(RESULTS, indent=2)
    print(formatted_data)
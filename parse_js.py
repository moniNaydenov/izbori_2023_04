import json

def load_data_from_json_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    start_index = content.find("HAS_PROTO = ")
    if start_index == -1:
        raise ValueError("The 'HAS_PROTO = ' string was not found in the file.")

    json_start = start_index + len("HAS_PROTO = ")
    json_data = content[json_start:-2]

    return json.loads(json_data)

def convert_data_to_urls(data):
    urls = []
    sourceurl = 'https://results.cik.bg/ns2023/protokoli/'

    count = 0
    for electionid, electiondata in data.items():
        for areaid, areadata in electiondata.items():
            for sectionid, sectiondata in areadata.items():
                if int(sectionid) < 100000:
                    sectionid = '00' + sectionid
                elif int(sectionid) < 1000000:
                    sectionid = '0' + sectionid
                if sectiondata['1'] == 24 or sectiondata['1'] == 28: # only paper based
                    urls.append(sourceurl + electionid + '/' + areaid + '/' + areaid + sectionid + '.1.html')
                    count += 1
                elif '2' in sectiondata and ((sectiondata['1'] == 26 and sectiondata['2'] == 32) or (sectiondata['1'] == 30 and sectiondata['2'] == 41)): # paper and machine based
                    urls.append(sourceurl + electionid + '/' + areaid + '/' + areaid + sectionid + '.1.html')
                    urls.append(sourceurl + electionid + '/' + areaid + '/' + areaid + sectionid + '.2.html')
                    count += 2
                else: # error in machine data
                    urls.append(sourceurl + electionid + '/' + areaid + '/' + areaid + sectionid + '.1.html')
                    count += 1
    return urls


if __name__ == '__main__':
    input_file_path = './data/protokoli.js'
    output_file_path = './data/urls.txt'
    data = load_data_from_json_file(input_file_path)
    urls = convert_data_to_urls(data)
    print("Total URLs: ", len(urls))
    with open(output_file_path, "w") as file:
        for url in urls:
            file.write(url + "\n")
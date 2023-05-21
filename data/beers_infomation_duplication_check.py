import json,sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# 빈 딕셔너리를 만듭니다. 이 딕셔너리는 각 맥주 이름의 출현 횟수를 저장합니다.
name_count = {}

# json 파일을 열어서 데이터를 로드합니다.
with open('C:\\Users\\jkypc\\OneDrive\\문서\\1.대학(3-1)\\전공_캡스톤디자인1\\fastapi_0519\data\\beers.json',encoding="UTF-8") as f:
    data = json.load(f)
    # 각 맥주에 대해 이름을 추출하고 딕셔너리에 저장합니다.
    for beer in data:
        name = beer['name']
        # 이름이 딕셔너리에 이미 존재하면, 출현 횟수를 증가시킵니다.
        if name in name_count:
            name_count[name] += 1
        # 이름이 딕셔너리에 없으면, 새로운 이름으로 간주하고 출현 횟수를 1로 설정합니다.
        else:
            name_count[name] = 1
            
    #     beer['image_path'] = "https://port-0-fastapi-0519-pi0mb2blhomfq05.sel4.cloudtype.app/data/img/"+name+".jpg"
    # with open('C:\\Users\\jkypc\\OneDrive\\문서\\1.대학(3-1)\\전공_캡스톤디자인1\\fastapi_0519\data\\beers.json','w',encoding="UTF-8") as file:
    #     json.dump(data, file, ensure_ascii=False, indent=4)

# 이름의 출현 횟수를 검사하여 중복된 이름을 찾습니다.
check = True
for name, count in name_count.items():
    if count > 1:
        print(f'맥주 이름 "{name}"이(가) {count}번 중복되었습니다.')
        check= False

if check:
    print("중복된 항목이 없습니다.")
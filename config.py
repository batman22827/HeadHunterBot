import json



def write_data_qa_industry(spans):
    data = {}
    data['spans'] = []
    for i in spans:
        if i.get_attribute('data-qa')!= None and len(i.text)>=3:
            print(f"{i.text}:{i.get_attribute('data-qa')}")
            data['spans'].append({
            'data-qa': f'{i.get_attribute("data-qa")}',
            'text': f'{i.text}',
            })
            #data['spans'].append({i.text,i.get_attribute('data-qa')})
        span_json = open('data/config.json', 'w', encoding='utf-8')

        json.dump(data,span_json, ensure_ascii=False,indent=True)

        span_json.close()   


def get_text_vacancy(vacancy):
    res = ''
    with open(f'data/resumes/{vacancy}.txt','r',encoding="utf-8") as f:
        content = f.read()
        f.close()
        return content

def get_text_data_qa():
    with open('data/config.json','r',encoding='utf-8') as f:
        data = json.load(f)
        s = data['spans']
        for i in s:
            print(s['text'])

 

        
get_text_data_qa()
                 



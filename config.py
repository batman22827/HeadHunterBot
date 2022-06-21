



def get_text_vacancy(vacancy):
    res = ''
    with open(f'data/resumes/{vacancy}.txt','r',encoding="utf-8") as f:
        content = f.read()
        f.close()
        return content




                 



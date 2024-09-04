from bert_cancer_question_answer import answer_question
import json
import os
content_list = ['breast_cancer', 'colorectal_cancer', 'lung_cancer', 'prostate_cancer', 'skin_cancer']
path = os.path.realpath('../data/')

with open(os.path.join(path, 'questions.json'), 'r') as f:
    questions_dict = json.load(f)
    f.close()

generated_answer_list = []

for each_dict in questions_dict:
    if each_dict['type'] in content_list:
        question = each_dict['question']
        content_file = each_dict['content_file']
        print(f'question-{question}-content file-{content_file}')
        with open(os.path.join(path, content_file), 'r') as f:
            related_content = f.read()
        generated_answer_list.append(question)
        generated_answer_list.append(answer_question(question, related_content))
        generated_answer_list.append('\n')

with open('generated_answer.txt', 'w') as f:
    f.write("\n".join(generated_answer_list))

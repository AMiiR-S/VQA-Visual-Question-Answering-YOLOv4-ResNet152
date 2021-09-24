# In[2]:
"""
Basic Configurations
"""
configs = {}
configs['cdsign']                                                   = '\\'
configs['path_root']                                                = 'C:\\VQA_Project\\'
configs['path_datasets']                                            = configs['path_root'] + 'Datasets' + configs['cdsign']
configs['datasets']                                                 = {}

#####################################################################  VQAv1 #########################################################################
configs['datasets']['VQAv1']                                        = {}
configs['datasets']['VQAv1']['Train']                               = {}
configs['datasets']['VQAv1']['Train']['Questions']                  = {}
configs['datasets']['VQAv1']['Train']['Questions']['File']          = 'OpenEnded_mscoco_train2014_questions.json'
configs['datasets']['VQAv1']['Train']['Questions']['Zip_File']      = 'Questions_Train_mscoco.zip'
configs['datasets']['VQAv1']['Train']['Questions']['Link']          = 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/Questions_Train_mscoco.zip'
configs['datasets']['VQAv1']['Train']['Questions']['Path']          = configs['path_datasets'] + 'VQAv1' + configs['cdsign'] + 'Questions' + configs['cdsign'] + configs['datasets']['VQAv1']['Train']['Questions']['File']

configs['datasets']['VQAv1']['Train']['Annotations']                = {}
configs['datasets']['VQAv1']['Train']['Annotations']['File']        = 'mscoco_train2014_annotations.json'
configs['datasets']['VQAv1']['Train']['Annotations']['Zip_File']    = 'Annotations_Train_mscoco.zip'
configs['datasets']['VQAv1']['Train']['Annotations']['Link']        = 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/Annotations_Train_mscoco.zip'
configs['datasets']['VQAv1']['Train']['Annotations']['Path']         = configs['path_datasets'] + 'VQAv1' + configs['cdsign'] + 'Annotations' + configs['cdsign'] + configs['datasets']['VQAv1']['Train']['Annotations']['File']

configs['datasets']['VQAv1']['Train']['Images']                     = {}
configs['datasets']['VQAv1']['Train']['Images']['File']             = 'train2014'
configs['datasets']['VQAv1']['Train']['Images']['Zip_File']         = 'train2014.zip'
configs['datasets']['VQAv1']['Train']['Images']['Link']             = 'http://images.cocodataset.org/zips/train2014.zip'
configs['datasets']['VQAv1']['Train']['Images']['Path']             = configs['path_datasets'] + 'VQAv1' + configs['cdsign'] + 'Images' + configs['cdsign'] + configs['datasets']['VQAv1']['Train']['Images']['File'] + configs['cdsign']

configs['datasets']['VQAv1']['Val']                                 = {}
configs['datasets']['VQAv1']['Val']['Questions']                    = {}
configs['datasets']['VQAv1']['Val']['Questions']['File']            = 'OpenEnded_mscoco_val2014_questions.json'
configs['datasets']['VQAv1']['Val']['Questions']['Zip_File']        = 'Questions_Val_mscoco.zip'
configs['datasets']['VQAv1']['Val']['Questions']['Link']            = 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/Questions_Val_mscoco.zip'
configs['datasets']['VQAv1']['Val']['Questions']['Path']             = configs['path_datasets'] + 'VQAv1' + configs['cdsign'] + 'Questions' + configs['cdsign'] + configs['datasets']['VQAv1']['Val']['Questions']['File']

configs['datasets']['VQAv1']['Val']['Annotations']                  = {}
configs['datasets']['VQAv1']['Val']['Annotations']['File']          = 'mscoco_val2014_annotations.json'
configs['datasets']['VQAv1']['Val']['Annotations']['Zip_File']      = 'Annotations_Val_mscoco.zip'
configs['datasets']['VQAv1']['Val']['Annotations']['Link']          = 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/Annotations_Val_mscoco.zip'
configs['datasets']['VQAv1']['Val']['Annotations']['Path']          = configs['path_datasets'] + 'VQAv1' + configs['cdsign'] + 'Annotations' + configs['cdsign'] + configs['datasets']['VQAv1']['Val']['Annotations']['File']

configs['datasets']['VQAv1']['Val']['Images']                       = {}
configs['datasets']['VQAv1']['Val']['Images']['File']               = 'val2014'
configs['datasets']['VQAv1']['Val']['Images']['Zip_File']           = 'val2014.zip'
configs['datasets']['VQAv1']['Val']['Images']['Link']               = 'http://images.cocodataset.org/zips/val2014.zip'
configs['datasets']['VQAv1']['Val']['Images']['Path']               = configs['path_datasets'] + 'VQAv1' + configs['cdsign'] + 'Images' + configs['cdsign'] + configs['datasets']['VQAv1']['Val']['Images']['File'] + configs['cdsign']
###################################################################################################################################################
#####################################################################  VQAv2 #########################################################################
configs['datasets']['VQAv2']                                        = {}
configs['datasets']['VQAv2']['Train']                               = {}
configs['datasets']['VQAv2']['Train']['Questions']                  = {}
configs['datasets']['VQAv2']['Train']['Questions']['File']          = 'v2_OpenEnded_mscoco_train2014_questions.json'
configs['datasets']['VQAv2']['Train']['Questions']['Zip_File']      = 'v2_Questions_Train_mscoco.zip'
configs['datasets']['VQAv2']['Train']['Questions']['Link']          = 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Train_mscoco.zip'
configs['datasets']['VQAv2']['Train']['Questions']['Path']          = configs['path_datasets'] + 'VQAv2' + configs['cdsign'] + 'Questions' + configs['cdsign'] + configs['datasets']['VQAv2']['Train']['Questions']['File']

configs['datasets']['VQAv2']['Train']['Annotations']                = {}
configs['datasets']['VQAv2']['Train']['Annotations']['File']        = 'v2_mscoco_train2014_annotations.json'
configs['datasets']['VQAv2']['Train']['Annotations']['Zip_File']    = 'v2_Annotations_Train_mscoco.zip'
configs['datasets']['VQAv2']['Train']['Annotations']['Link']        = 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Train_mscoco.zip'
configs['datasets']['VQAv2']['Train']['Annotations']['Path']        = configs['path_datasets'] + 'VQAv2' + configs['cdsign'] + 'Annotations' + configs['cdsign'] + configs['datasets']['VQAv2']['Train']['Annotations']['File']

configs['datasets']['VQAv2']['Train']['Images']                     = configs['datasets']['VQAv1']['Train']['Images']

configs['datasets']['VQAv2']['Val']                                 = {}
configs['datasets']['VQAv2']['Val']['Questions']                    = {}
configs['datasets']['VQAv2']['Val']['Questions']['File']            = 'v2_OpenEnded_mscoco_val2014_questions.json'
configs['datasets']['VQAv2']['Val']['Questions']['Zip_File']        = 'v2_Questions_Val_mscoco.zip'
configs['datasets']['VQAv2']['Val']['Questions']['Link']            = 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Val_mscoco.zip'
configs['datasets']['VQAv2']['Val']['Questions']['Path']            = configs['path_datasets'] + 'VQAv2' + configs['cdsign'] + 'Questions' + configs['cdsign'] + configs['datasets']['VQAv2']['Val']['Questions']['File']

configs['datasets']['VQAv2']['Val']['Annotations']                  = {}
configs['datasets']['VQAv2']['Val']['Annotations']['File']          = 'v2_mscoco_val2014_annotations.json'
configs['datasets']['VQAv2']['Val']['Annotations']['Zip_File']      = 'v2_Annotations_Val_mscoco.zip'
configs['datasets']['VQAv2']['Val']['Annotations']['Link']          = 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Val_mscoco.zip'
configs['datasets']['VQAv2']['Val']['Annotations']['Path']          = configs['path_datasets'] + 'VQAv2' + configs['cdsign'] + 'Annotations' + configs['cdsign'] + configs['datasets']['VQAv2']['Val']['Annotations']['File']

configs['datasets']['VQAv2']['Val']['Images']                       = configs['datasets']['VQAv1']['Val']['Images']
###################################################################################################################################################
#####################################################################  VGv1.0 #########################################################################
configs['datasets']['VGv1.0']                                       = {}
configs['datasets']['VGv1.0']['Images']                             = {}
configs['datasets']['VGv1.0']['Images']['Part_1']                   = {}
configs['datasets']['VGv1.0']['Images']['Part_1']['File']           = 'VG_100K'
configs['datasets']['VGv1.0']['Images']['Part_1']['Zip_File']       = 'images.zip'
configs['datasets']['VGv1.0']['Images']['Part_1']['Link']           = 'https://cs.stanford.edu/people/rak248/VG_100K_2/images.zip'
configs['datasets']['VGv1.0']['Images']['Part_1']['Path']           = configs['path_datasets'] + 'VGv1.0' + configs['cdsign'] + 'Images' + configs['cdsign'] + configs['datasets']['VGv1.0']['Images']['Part_1']['File'] + configs['cdsign']

configs['datasets']['VGv1.0']['Images']['Part_2']   = {}
configs['datasets']['VGv1.0']['Images']['Part_2']['File']           = 'VG_100K_2'
configs['datasets']['VGv1.0']['Images']['Part_2']['Zip_File']       = 'images2.zip'
configs['datasets']['VGv1.0']['Images']['Part_2']['Link']           = 'https://cs.stanford.edu/people/rak248/VG_100K_2/images2.zip'
configs['datasets']['VGv1.0']['Images']['Part_2']['Path']           = configs['path_datasets'] + 'VGv1.0' + configs['cdsign'] + 'Images' + configs['cdsign'] + configs['datasets']['VGv1.0']['Images']['Part_2']['File'] + configs['cdsign']

configs['datasets']['VGv1.0']['Questions_Answers']                  = {}
configs['datasets']['VGv1.0']['Questions_Answers']['File']          = 'question_answers.json'
configs['datasets']['VGv1.0']['Questions_Answers']['Zip_File']      = 'question_answers.json.zip'
configs['datasets']['VGv1.0']['Questions_Answers']['Link']          = 'https://visualgenome.org/static/data/dataset/question_answers.json.zip'
configs['datasets']['VGv1.0']['Questions_Answers']['Path']          = configs['path_datasets'] + 'VGv1.0' + configs['cdsign'] + 'Questions_Answers' + configs['cdsign'] + configs['datasets']['VGv1.0']['Questions_Answers']['File']
####################################################### VGv1.2##### ###############################################################################
configs['datasets']['VGv1.2']                                       = configs['datasets']['VGv1.0']
###################################################################################################################################################


configs['chosen_datasets_list']     = ['VQAv1'] #['VQAv1', 'VQAv2', 'VGv1.0', 'VGv1.2']
configs['chosen_datasets_str']      = '_'.join(configs['chosen_datasets_list'])


configs['image_model']              = 'YOLOv4-448-1024' # ['ResNet152-448-2048', 'YOLOv4-448-1024']
configs['random_seed']              = 100

configs['path_image_model']         = configs['path_root'] + 'Image_Models' + configs['cdsign'] + configs['image_model'] + configs['cdsign']

configs['path_images_features']     = configs['path_image_model'] + 'Images_Features' + configs['cdsign']

configs['path_histories']           = configs['path_root'] + 'Histories' + configs['cdsign'] + configs['chosen_datasets_str'] + '_' + configs['image_model'] + configs['cdsign']
configs['path_plots']               = configs['path_root'] + 'Plots' + configs['cdsign'] + configs['chosen_datasets_str'] + '_' + configs['image_model'] + configs['cdsign']
configs['path_test_images']         = configs['path_root'] + 'Test_Images' + configs['cdsign']


# In[3]:


def create_directories(configs):
    for key, value in configs.items():
        if 'path_' in key:
            Path(value).mkdir(parents=True, exist_ok=True)
            print('Created ', value)
    return True


# In[4]:


def save_pickle_data(data, path):
    try:
        with open(path, 'wb') as handle:
            pk.dump(data, handle, protocol=pk.HIGHEST_PROTOCOL)
        return True
    except:
        return False


# In[5]:


def load_pickle_data(path):
    if os.path.exists(path) == True:
        with open(path, 'rb') as handle:
            data = pk.load(handle)
        return data
    else:
        return False


# In[6]:


def check_MSCOCO_data(configs, dataset):

    directory = configs['path_datasets'] + dataset + configs['cdsign']
    Path(directory).mkdir(parents=True, exist_ok=True)

    train_val = list(configs['datasets'][dataset].keys())


    for tv in train_val:
        data_types = list(configs['datasets'][dataset][tv].keys())

        for dt in data_types:
            file_name = configs['datasets'][dataset][tv][dt]['File']
            file_path = configs['datasets'][dataset][tv][dt]['Path']
#             file_path = directory + dt + configs['cdsign'] + file_name
            zip_file = configs['datasets'][dataset][tv][dt]['Zip_File']
            file_link = configs['datasets'][dataset][tv][dt]['Link']

            ##### Just for Development. Remove it Later ######
            if dt == 'Images':
                Path(file_path).mkdir(parents=True, exist_ok=True)
            ##################################################

            if not os.path.exists(file_path):
                print('Donwloading {0}'.format(file_name))
                os.system('cd {0} && wget {1} && unzip {2} && rm {2}'.format(directory, file_link, zip_file))
            else:
                print('Exists {0}'.format(file_name))


# In[7]:


def check_VG_data(configs, dataset):

    directory = configs['path_datasets'] + dataset + configs['cdsign']
    Path(directory).mkdir(parents=True, exist_ok=True)

    data_types = list(configs['datasets'][dataset].keys())

    for dt in data_types:
        if dt == 'Images':
            for p in configs['datasets'][dataset]['Images']:
                file_name = configs['datasets'][dataset][dt][p]['File']
                file_path = configs['datasets'][dataset][dt][p]['Path']
#                 file_path = directory  + dt + configs['cdsign'] + file_name
                zip_file = configs['datasets'][dataset][dt][p]['Zip_File']
                file_link = configs['datasets'][dataset][dt][p]['Link']

                ##### Just for Development. Remove it Later ######
                Path(file_path).mkdir(parents=True, exist_ok=True)
                ##################################################

                if not os.path.exists(file_path):
                    print('Donwloading {0}'.format(file_name))
                    os.system('cd {0} && wget {1} && unzip {2} && rm {2}'.format(directory, file_link, zip_file))
                else:
                    print('Exists {0}'.format(file_name))

        else:
            file_name = configs['datasets'][dataset][dt]['File']
            file_path = configs['datasets'][dataset][dt]['Path']
#             file_path = directory  + dt + configs['cdsign'] + file_name
            zip_file = configs['datasets'][dataset][dt]['Zip_File']
            file_link = configs['datasets'][dataset][dt]['Link']

            if not os.path.exists(file_path):
                print('Donwloading {0}'.format(file_name))
                os.system('cd {0} && wget {1} && unzip {2} && rm {2}'.format(directory, file_link, zip_file))
            
            else:
                print('Exists {0}'.format(file_name))


# In[8]:


def get_MSCOCO_data(configs, dataset):
    results = []

    for key, value in configs['datasets'][dataset].items():

        path_questions      = configs['path_datasets'] + dataset + configs['cdsign'] + 'Questions' + configs['cdsign'] + value['Questions']['File']
        path_annotations    = configs['path_datasets'] + dataset + configs['cdsign'] + 'Annotations' + configs['cdsign'] + value['Annotations']['File']

        with open(file=path_questions, mode='r') as questions:
            data_questions = json.load(questions)
        
        with open(file=path_annotations, mode='r') as answers:
            data_answers = json.load(answers)
    
        data_size = len(data_answers['annotations'])
    
        for i in range(data_size):
            question = data_questions['questions'][i]
            answer = data_answers['annotations'][i]
            answer_type = answer['answer_type']

            data = {}
            data['image_id']                = question['image_id']
            data['question_id']             = question['question_id']
            data['question']                = question['question'].lower()
            data['answer']                  = answer['multiple_choice_answer'].lower()
            data['answers']                 = answer['answers']
            data['question_type']           = answer['question_type'].lower()

            results.append(data)
    
    print('{0} Q/A: {1}'.format(dataset, len(results)))

    return results


# In[9]:


def get_VG_data(configs, dataset):
    results = []
    
    qap = configs['path_datasets'] + dataset + configs['cdsign'] + 'Questions_Answers' + configs['cdsign'] + configs['datasets'][dataset]['Questions_Answers']['File']

    with open(file=qap, mode='r') as qa:
        data = json.load(qa)

    for d in data:
        for j in range(len(d['qas'])):
            que_ans = d['qas'][j]

            temp = {}
            temp['image_id']        = que_ans['image_id']
            temp['question_id']     = que_ans['qa_id']
            temp['answer']          = que_ans['answer'][:-1].lower()
            temp['question']        = que_ans['question'].lower()
            
            results.append(temp)
    
    print('{0} Q/A: {1}'.format(dataset, len(results)))
        
    return results


# In[10]:


def get_original_data(configs):
    data = []

    for dataset in configs['chosen_datasets_list']:
        print('Preparing {0} Dataset:'.format(dataset))
        
        if 'VQA' in dataset:
            check_MSCOCO_data(configs, dataset)
            data = data +  get_MSCOCO_data(configs, dataset)

        elif 'VG' in dataset:
            check_VG_data(configs, dataset)
            data = data + get_VG_data(configs, dataset)

    return data


# In[11]:


def plot_questions_types_frequency(freqs, fname='Questions_Types'):
    temp = {}
    temp['keys'] = list(freqs.keys())
    temp['vals'] = list(freqs.values())
    temp = pd.DataFrame(temp)
    temp.set_index('keys').vals.plot(kind='bar', figsize=(25,25))
    Path(configs['path_plots']).mkdir(parents=True, exist_ok=True)
    path = configs['path_plots'] + fname + str(time.strftime("%Y-%m-%d_%H-%M-%S")) +'.png'
    plt.savefig(r'{}'.format(path))


# In[12]:


def plot_answers_types_frequency(freqs, fname='Questions_Types'):
    temp = {}
    temp['keys'] = list(freqs.keys())
    temp['vals'] = list(freqs.values())
    temp = pd.DataFrame(temp)
    temp.set_index('keys').vals.plot(kind='bar', figsize=(25,25))
    Path(configs['path_plots']).mkdir(parents=True, exist_ok=True)
    path = configs['path_plots'] + fname + str(time.strftime("%Y-%m-%d_%H-%M-%S")) +'.png'
    plt.savefig(r'{}'.format(path))


# In[13]:


def plot_answers_frequency(freqs, fname, split_keys=[]):

    sorted_temp = sorted(freqs.items(), key=operator.itemgetter(1), reverse=True)
    data_size = sum([i[1] for i in sorted_temp])

    print('Data Size: {0}'.format(data_size))
    print('Number of Unique Answers: {0}'.format(len(sorted_temp)))

    temp = {}
    temp['keys'] = split_keys + [len(sorted_temp)]
    temp['vals'] = [sum([j[1] for j in sorted_temp[:sk]]) / data_size  for sk in split_keys] + [1]

    temp = pd.DataFrame(temp)
    temp.set_index('keys').vals.plot(kind='bar', figsize=(25,25))
    Path(configs['path_plots']).mkdir(parents=True, exist_ok=True)
    path = configs['path_plots'] + fname + str(time.strftime("%Y-%m-%d_%H-%M-%S")) +'.png'
    plt.savefig(r'{}'.format(path))

    for sk in split_keys:
        sum_temp = sum([j[1] for j in sorted_temp[:sk]])
        print('{0} of Most Frequent Answers are in {1} of {2} questions, ({3} % of total data)'.format(sk, sum_temp, data_size, sum_temp / data_size * 100))
    
    print('{0} of Most Frequent Answers are in {1} of {2} questions, ({3} % of total data)'.format(len(sorted_temp), data_size, data_size, data_size / data_size * 100))


# In[14]:


def plot_tokens_length_frequency(freqs, fname, split_keys=[]):
    sorted_freqs = sorted(freqs.items(), key=operator.itemgetter(0), reverse=False)
    data_size = sum([i[1] for i in sorted_freqs])

    temp = {}
    temp['keys'] = [i[0] for i in sorted_freqs]
    temp['vals'] = [i[1] for i in sorted_freqs]
    temp = pd.DataFrame(temp)
    temp.set_index('keys').vals.plot(kind='bar', figsize=(25,25))
    Path(configs['path_plots']).mkdir(parents=True, exist_ok=True)
    path = configs['path_plots'] + fname + str(time.strftime("%Y-%m-%d_%H-%M-%S")) +'.png'
    plt.savefig(r'{}'.format(path))

    count = 0
    for sf in sorted_freqs:
        count = count + sf[1]
        print('{0} Tokens = {1} of {2} ({3} %)'.format(sf[0], count, data_size, count / data_size * 100))


# In[15]:


def plot_tokens_frequency(freqs, fname, split_keys=[]):

    sorted_temp = sorted(freqs.items(), key=operator.itemgetter(1), reverse=True)
    data_size = sum([i[1] for i in sorted_temp])

    print('Data Size: {0}'.format(data_size))
    print('Number of Unique Tokens: {0}'.format(len(sorted_temp)))

    temp = {}
    temp['keys'] = split_keys + [len(sorted_temp)]
    temp['vals'] = [sum([j[1] for j in sorted_temp[:sk]]) / data_size  for sk in split_keys] + [1]

    temp = pd.DataFrame(temp)
    temp.set_index('keys').vals.plot(kind='bar', figsize=(25,25))
    Path(configs['path_plots']).mkdir(parents=True, exist_ok=True)
    path = configs['path_plots'] + fname + str(time.strftime("%Y-%m-%d_%H-%M-%S")) +'.png'
    plt.savefig(r'{}'.format(path))

    for sk in split_keys:
        sum_temp = sum([j[1] for j in sorted_temp[:sk]])
        print('{0} of Most Frequent Tokens are in {1} of {2} questions, ({3} % of total data)'.format(sk, sum_temp, data_size, sum_temp / data_size * 100))
    
    print('{0} of Most Frequent Tokens are in {1} of {2} questions, ({3} % of total data)'.format(len(sorted_temp), data_size, data_size, data_size / data_size * 100))


# In[16]:


def question_types_filter(data):
    results = []

    que_types = collections.defaultdict(int)
    
    que_1_types = ['what', 'how', 'whose', 'which', 'when', 'where', 'who', 'why', 'can', 'could', 'am', 'is', 'are', 'was',                         'were', 'did', 'does', 'do', 'has', 'have', 'had', 'should', 'would', 'will']

    que_2_types = []
    #-------------------
    
    que_words = ['man']
    

    for d in data:
        q = d['question'].replace("'s", ' ')
        q_1 = d['question'].replace("'s", ' ').split()[0]
        q_2 = " ".join(d['question'].replace("'s", ' ').split()[:2])

        if (q_2 in que_2_types):
            que_types[q_2] += 1
            d['question_type'] = q_2
            results.append(d)
            
        
        elif (q_1 in que_1_types):
            que_types[q_1] += 1
            d['question_type'] = q_1
            results.append(d)
            
        else:

            for qw in que_words:

                if qw in q:

                    que_types[qw] += 1
                    d['question_type'] = 'others'
                    results.append(d)
    
    print('Questions Reduced from {0} to {1}'.format(len(data), len(results)))
            
    return results, que_types


# In[17]:


def answer_types_filter(data, ans_types=['yes/no', 'number', 'binary', 'others_single_word', 'others_multiple_words']):
    
    
    results = []

    ans_types_count = collections.defaultdict(int)

    for d in data:
        ans = d['answer']
        que = d['question']

        if ans.isnumeric():
            d['answer_type'] = 'number'
            ans_types_count['number'] += 1
            results.append(d)
        
        elif ans in ['yes', 'no']:
            d['answer_type'] = 'yes/no'
            ans_types_count['yes/no'] += 1
            results.append(d)
        
        elif ('or' in que) and (ans in que):
            d['answer_type'] = 'binary'
            ans_types_count['binary'] += 1
            results.append(d)
        
        else:
            ans_list = ans.split()
            if len(ans_list) == 1:
                    
                d['answer_type'] = 'others_single_word'
                ans_types_count['others_single_word'] += 1
                results.append(d)

            else:
                d['answer_type'] = 'others_multiple_words'
                ans_types_count['others_multiple_words'] += 1
                results.append(d)

    print('Questions Reduced from {0} to {1}'.format(len(data), len(results)))

    return results, ans_types_count


# In[18]:


def get_answers_frequency(data, view=0):
    ans_freq = collections.defaultdict(int)

    for d in data:
        ans_freq[d['answer']] += 1
    
    sorted_ans_freq = sorted(ans_freq.items(), key=operator.itemgetter(1), reverse=True)
    
    for i in range(view):
        print(sorted_ans_freq[i])
    return ans_freq


# In[19]:


def get_top_answers(ans_freq, num_ans):

    temp = sorted(ans_freq.items(), key=operator.itemgetter(1), reverse=True)
    
    top_ans = [a for a in temp[:num_ans]]

    index_to_answer = {i:w[0] for i, w in enumerate(top_ans)}
    answer_to_index = {w[0]:i for i, w in enumerate(top_ans)}

    return top_ans, index_to_answer, answer_to_index


# In[20]:


def filter_data(data, top_ans):
    results = []

    ans = [i[0] for i in top_ans]

    for d in data:
        if d['answer'] in ans:
            results.append(d)

    print('Questions reduced from {0} to {1}'.format(len(data), len(results)))
    return results


# In[21]:


def tokenize_questions(data, view=0):
    for i, d in enumerate(data):
        d['tokens'] = nltk.word_tokenize(d['question'].lower())

    for i in range(view):
        print('---------------------- Example {0} ----------------------'.format(i+1))
        print('Original Question: \t', data[i]['question'])
        print('Tokenized Question: \t', data[i]['tokens'])
        print('---------------------------------------------------------')
        print('\n')
    return data


# In[22]:


def get_tokens_length_frequency(data):
    results = collections.defaultdict(int)
    
    for d in data:
        results[len(d['tokens'])] += 1
    
    return results


# In[23]:


def apply_max_tokens(data, max_tokens):
    for d in data:
        d['tokens'] = d['tokens'][:max_tokens]
    return data


# In[24]:


def get_tokens_frequency(data):
    results = collections.defaultdict(int)

    for d in data:
        t = d['tokens']
        for l in range(len(t)):
            results[t[l]] += 1

    return results


# In[25]:


def get_vocab(freqs, num_tokens):

    temp = sorted(freqs.items(), key=operator.itemgetter(1), reverse=True)

    vocab = [i for i in temp[:num_tokens-1]] + [('UNK', sum([i[1] for i in temp[num_tokens-1:]]))]

    index_to_word = {i:w[0] for i, w in enumerate(vocab)}
    word_to_index = {w[0]:i for i, w in enumerate(vocab)}

    return vocab, index_to_word, word_to_index


# In[26]:


def vectorize_tokens(data, word_to_index):
    nb_samples = len(data)

    for d in data:
        v = np.zeros(configs['que_max_length'], dtype=np.int32)
        tokens = d['tokens']

        for j in range(len(tokens)):
                v[j] = word_to_index.get(tokens[j], word_to_index['UNK'])
    
        d['vector'] = v
    return data


# In[27]:


def get_answers_matrix(data, answer_to_index):
    answers = np.zeros((len(data), len(answer_to_index)), dtype=np.int8)
    
    for i, d in enumerate(data):
        answers[i, answer_to_index[d['answer']]] = 1

    return answers


# In[28]:


import os
import gc
import time
import json
import nltk
import random
import operator
import collections
import numpy as np
import pandas as pd
from math import ceil
from pathlib import Path
import matplotlib.pyplot as plt


# nltk.download('punkt')


# In[29]:


data_orig = get_original_data(configs)


# In[30]:


# data_orig, que_types = question_types_filter(data_orig)
# plot_questions_types_frequency(que_types, fname='Questions_Types')


# In[31]:


data_orig, ans_types = answer_types_filter(data_orig)
plot_answers_types_frequency(ans_types, fname='Answers_Types')


# In[32]:


answers_frequency = get_answers_frequency(data_orig, view=5)
plot_answers_frequency(answers_frequency, fname='Answers_Frequency', split_keys=[100, 500, 1000, 2000, 3000, 5000, 10000, 50000, 100000, 200000])


# In[33]:


configs['num_ans'] = 3000
top_ans, index_to_answer, answer_to_index = get_top_answers(answers_frequency, num_ans=configs['num_ans'])


# In[34]:


data_orig = filter_data(data_orig, top_ans)


# In[35]:


data_orig = tokenize_questions(data_orig, view=0)


# In[36]:


tokens_length_frequency = get_tokens_length_frequency(data_orig)
plot_tokens_length_frequency(tokens_length_frequency, fname='Tokens')


# In[37]:


configs['que_max_length'] = 17


# In[38]:


data_orig = apply_max_tokens(data_orig, configs['que_max_length'])


# In[39]:


tokens_frequency = get_tokens_frequency(data_orig)
plot_tokens_frequency(tokens_frequency, fname='Tokens_Frequency', split_keys=[50, 100, 500, 1000, 5000, 10000])


# In[40]:


configs['num_tokens'] = 10000 # + 1 'UNK' token


# In[41]:


vocab, index_to_word, word_to_index = get_vocab(tokens_frequency, configs['num_tokens'])


# In[42]:


data_orig = vectorize_tokens(data_orig, word_to_index)


# In[43]:


random.Random(configs['random_seed']).shuffle(data_orig)


# In[44]:


configs['val_percent']              = 0.10
configs['train_percent']              = 1 - configs['val_percent']


data_size = len(data_orig)
val_size = ceil(configs['val_percent'] * len(data_orig))
train_size = data_size - val_size

train_data = data_orig[:-val_size]
val_data = data_orig[-val_size:]

print('Train Data Size: {0} of {1} ({2} %)'.format(len(train_data), data_size, len(train_data) / data_size * 100))
print('Val Data Size: {0} of {1} ({2} %)'.format(len(val_data), data_size, len(val_data) / data_size * 100))

print('{0} of {1} Train Data Have Unique Images: '.format(len(set(d['image_id'] for d in train_data)), len(train_data)))
print('{0} of {1} Validation Data Have Unique Images: '.format(len(set(d['image_id'] for d in val_data)), len(val_data)))


# In[45]:


X_train_questions = np.array([d['vector'] for d in train_data], dtype=np.int32)
X_val_questions = np.array([d['vector'] for d in val_data], dtype=np.int32)


# In[46]:


Y_train_answers = get_answers_matrix(train_data, answer_to_index)
Y_val_answers = get_answers_matrix(val_data, answer_to_index)

gc.collect()


# In[47]:


X_train_questions.shape, X_val_questions.shape, Y_train_answers.shape, Y_val_answers.shape


# In[48]:


import os
import cv2
import numpy as np
import pickle as pk

from tqdm import tqdm
from tensorflow.keras.applications.resnet import ResNet152, preprocess_input
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.models import Model, load_model


# In[49]:


def get_image_model(configs):
    temp = configs['image_model'].split('-')
    image_model = temp[0]
    input_size = int(temp[1])

    print('Loading {0} Image Model'.format(image_model))

    if image_model == 'ResNet152':
        model_temp = ResNet152(include_top=False, weights='imagenet', input_shape=(input_size, input_size, 3))
        model = GlobalAveragePooling2D()(model_temp.output)

    elif image_model == 'YOLOv4':
        model_temp = load_model(configs['path_image_model'] + 'YOLOv4' + configs['cdsign'])
        model = GlobalAveragePooling2D()(model_temp.get_layer('tf.math.multiply_71').output)

    model = Model(inputs=model_temp.input, outputs=model)
    model.trainable = False

    return model


# In[50]:


def get_features(img_path, image_model):
    """
    Returns the features of image using image model
    """
    input_size = int(configs['image_model'].split('-')[1])
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (input_size, input_size))
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    img_features = image_model.predict(img)[0]
    return img_features


# In[51]:


def get_images_features(configs):

    image_model = get_image_model(configs)
    
    images_features = {}
    
    for dataset in configs['chosen_datasets_list']:
        print(dataset)
        if 'VQA' in dataset:
            temp = load_pickle_data(configs['path_images_features'] + 'VQAv1_' + configs['image_model'] + '_images_features.pickle')
            images_features.update(temp)
            
            for key, value in configs['datasets'][dataset].items():
                images_names = os.listdir(value['Images']['Path'])
                
                for i in tqdm(range(len(images_names))):
                    img_name = images_names[i]
                    img_id = 'COCO_' + img_name[-16:-4]
                    img_path = value['Images']['Path'] + img_name
                    
                    if img_id not in images_features:
                        images_features[img_id] = get_features(img_path, image_model)[0]
            
                        save_pickle_data(images_features, configs['path_images_features'] + 'VQAv1_' + configs['image_model'] + '_images_features.pickle')
        
        elif 'VG' in dataset:
            temp = load_pickle_data(configs['path_images_features'] + 'VGv1.0_' + configs['image_model'] + '_images_features.pickle')
            images_features.update(temp)
            
            for key, value in configs['datasets'][dataset]['Images'].items():
                images_names = os.listdir(value['Path'])
                
                for i in tqdm(range(len(images_names))):
                    img_name = images_names[i]
                    img_id = 'VG_' + img_name[:-4]
                    img_path = value['Path'] + img_name
                    
                    if img_id not in images_features:
                        images_features[img_id] = get_features(img_path, image_model)[0]
                        save_pickle_data(images_features, configs['path_images_features'] + 'VGv1.0_' + configs['image_model'] + '_images_features.pickle')
            
    return images_features


# In[52]:


def get_images_matrix(data, images_features, img_dim):

    nb_samples = len(data)

    images_matrix = np.zeros((nb_samples, img_dim), dtype=np.float32)
    for i in range(nb_samples):
        img_id = 'COCO_%012d'%(data[i]['image_id'])
        if img_id not in images_features:
            img_id = 'VG_' + str(data[i]['image_id'])
        
        images_matrix[i] = images_features[img_id]

    return images_matrix


# In[53]:


images_features = get_images_features(configs)


# In[54]:


configs['img_dim'] = next(iter(images_features.values())).shape[0]


# In[55]:


X_train_images = get_images_matrix(train_data, images_features, configs['img_dim'])
X_val_images = get_images_matrix(val_data, images_features, configs['img_dim'])


# In[56]:


X_train_images.shape


# In[ ]:





# In[57]:


import tensorflow as tf
from tensorflow.keras.layers import *
import tensorflow.keras.backend as K
from tensorflow.keras.utils import plot_model
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras.models import Model, save_model, load_model, Sequential



K.set_floatx('float32')


# In[58]:


def compact_bilinear(tensors_list):

    def _generate_sketch_matrix(rand_h, rand_s, output_dim):
        """
        Return a sparse matrix used for tensor sketch operation in compact bilinear
        pooling
        Args:
            rand_h: an 1D numpy array containing indices in interval `[0, output_dim)`.
            rand_s: an 1D numpy array of 1 and -1, having the same shape as `rand_h`.
            output_dim: the output dimensions of compact bilinear pooling.
        Returns:
            a sparse matrix of shape [input_dim, output_dim] for tensor sketch.
        """

        # Generate a sparse matrix for tensor count sketch
        rand_h = rand_h.astype(np.int64)
        rand_s = rand_s.astype(np.float32)
        assert (rand_h.ndim == 1 and rand_s.ndim == 1 and len(rand_h) == len(rand_s))
        assert (np.all(rand_h >= 0) and np.all(rand_h < output_dim))
        input_dim = len(rand_h)
        indices = np.concatenate((np.arange(input_dim)[..., np.newaxis],
                                  rand_h[..., np.newaxis]), axis=1)
        sparse_sketch_matrix = tf.sparse.reorder(
            tf.SparseTensor(indices, rand_s, [input_dim, output_dim]))
        return sparse_sketch_matrix

    bottom1, bottom2 = tensors_list
    output_dim = 8192

    # Static shapes are needed to construction count sketch matrix
    input_dim1 = bottom1.get_shape().as_list()[-1]
    input_dim2 = bottom2.get_shape().as_list()[-1]

    # print (bottom1.get_shape().as_list())
    # print (bottom2.get_shape().as_list())

    # Step 0: Generate vectors and sketch matrix for tensor count sketch
    # This is only done once during graph construction, and fixed during each
    # operation
    seed_h_1 = 1
    seed_s_1 = 3
    seed_h_2 = 5
    seed_s_2 = 7

    # Generate sparse_sketch_matrix1 using rand_h_1 and rand_s_1
    np.random.seed(seed_h_1)
    rand_h_1 = np.random.randint(output_dim, size=input_dim1)
    np.random.seed(seed_s_1)
    rand_s_1 = 2 * np.random.randint(2, size=input_dim1) - 1
    sparse_sketch_matrix1 = _generate_sketch_matrix(rand_h_1, rand_s_1, output_dim)

    # Generate sparse_sketch_matrix2 using rand_h_2 and rand_s_2
    np.random.seed(seed_h_2)
    rand_h_2 = np.random.randint(output_dim, size=input_dim2)
    np.random.seed(seed_s_2)
    rand_s_2 = 2 * np.random.randint(2, size=input_dim2) - 1
    sparse_sketch_matrix2 = _generate_sketch_matrix(rand_h_2, rand_s_2, output_dim)

    # Step 1: Flatten the input tensors and count sketch
    bottom1_flat = tf.reshape(bottom1, [-1, input_dim1])
    bottom2_flat = tf.reshape(bottom2, [-1, input_dim2])

    # Essentially:
    #   sketch1 = bottom1 * sparse_sketch_matrix
    #   sketch2 = bottom2 * sparse_sketch_matrix
    # But tensorflow only supports left multiplying a sparse matrix, so:
    #   sketch1 = (sparse_sketch_matrix.T * bottom1.T).T
    #   sketch2 = (sparse_sketch_matrix.T * bottom2.T).T
    sketch1 = tf.transpose(tf.sparse.sparse_dense_matmul(sparse_sketch_matrix1,
                                                         bottom1_flat, adjoint_a=True, adjoint_b=True))
    sketch2 = tf.transpose(tf.sparse.sparse_dense_matmul(sparse_sketch_matrix2,
                                                         bottom2_flat, adjoint_a=True, adjoint_b=True))

    # Step 2: FFT
    fft1 = tf.signal.fft(tf.complex(real=sketch1, imag=tf.zeros_like(sketch1)))
    fft2 = tf.signal.fft(tf.complex(real=sketch2, imag=tf.zeros_like(sketch2)))

    # Step 3: Elementwise product
    fft_product = tf.multiply(fft1, fft2)

    # Step 4: Inverse FFT and reshape back
    # Compute output shape dynamically: [batch_size, height, width, output_dim]
    cbp_flat = tf.math.real(tf.signal.ifft(fft_product))

    output_shape = tf.add(tf.multiply(tf.shape(bottom1), [1, 1, 0]),
                          [0, 0, output_dim])
    cbp = tf.reshape(cbp_flat, output_shape)

    # print (cbp.get_shape().as_list())

    return cbp


# In[59]:


class WeightedSum(Layer):

    def __init__(self, **kwargs):
        super(WeightedSum, self).__init__(**kwargs)
    
    def build(self, input_shape):
        super(WeightedSum, self).build(input_shape)

    def call(self, x):
        return 0.1 * x[0] + (1 - 0.1) * x[1]


# In[60]:


img_dim         = configs['img_dim'] # 1024
num_ans         = configs['num_ans'] # 2000
num_tokens      = configs['que_max_length'] # 15
emb_dim         = configs['emb_dim'] = 512
dropout_rate    = configs['dropout_rate'] = 0.4
activations     = configs['activations'] = 'relu'
vocab           = configs['num_tokens'] # 15100
out_dim = 8192

"""
Inputs
"""
input_images = Input(shape=(img_dim), dtype=np.float32)
input_images_rv = RepeatVector(n=num_tokens)(input_images)
input_images_rv = Dropout(rate=dropout_rate)(input_images_rv)

print('input_images Shape: ', input_images.shape)
print('input_images_rv Shape: ', input_images_rv.shape)

input_questions = Sequential()
input_questions.add(Embedding(input_dim=vocab+1, output_dim=512, input_length=num_tokens, mask_zero=True))
input_questions.add(LSTM(units=1024, dropout=dropout_rate, return_sequences=True))
input_questions.add(LSTM(units=1024, dropout=dropout_rate, return_sequences=True))
input_questions.add(Dropout(rate=dropout_rate))

# input_questions.add(Dropout(rate=dropout_rate))

print('Question Embedding Input Shape: ', input_questions.input_shape)
print('Question Embedding Output Shape: ', input_questions.output_shape)

x = Lambda(compact_bilinear, name='compact_bilinear_1', output_shape=(None, num_tokens, out_dim))([input_images_rv, input_questions.output])
x = Reshape(target_shape=(num_tokens, out_dim))(x)

x = Conv1D(filters=512, kernel_size=num_tokens, padding='same')(x)
x = Activation(activation='relu')(x)

x = Conv1D(filters=1, kernel_size=num_tokens, padding='same')(x)
x = Activation(activation='softmax')(x)
x = WeightedSum()([x, input_images_rv])

x = Lambda(compact_bilinear, name='compact_bilinear_2', output_shape=(None, num_tokens, out_dim))([x, input_questions.output])
x = Reshape(target_shape=(num_tokens, out_dim))(x)

x = GlobalAveragePooling1D()(x)
x = Dropout(rate=dropout_rate)(x)

x = Dense(units=4096)(x)
x = Activation(activation='relu')(x)
x = Dropout(rate=dropout_rate)(x)

x = Dense(units=num_ans)(x)
x = Activation(activation='softmax')(x)

model = Model(inputs=[input_questions.input, input_images], outputs=x)
# model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.000006), metrics=['accuracy'])
model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=6e-6), metrics=['accuracy'])

model.summary()


# In[61]:


plot_model(model, configs['path_plots'] + 'Model.png', show_shapes=True, show_dtype=True)


# In[62]:


from tensorflow.keras.callbacks import ModelCheckpoint
max_accuracy = ModelCheckpoint(
    configs['path_image_model'] + configs['chosen_datasets_str'] + '_50 Epochs_Max_Accuracy.h5',
    monitor="val_accuracy",
    verbose=1,
    save_best_only=True,
    save_weights_only=False,
    mode="max",
    save_freq="epoch",
)

min_loss = ModelCheckpoint(
    configs['path_image_model'] + configs['chosen_datasets_str'] + '_50 Epochs_Min_Loss.h5',
    monitor="val_loss",
    verbose=1,
    save_best_only=True,
    save_weights_only=False,
    mode="min",
    save_freq="epoch",
)


# In[63]:


configs['batch_size']               = 256
configs['num_epochs']               = 100
start_time = time.time()
results = model.fit(x=[X_train_questions, X_train_images],
                    y=Y_train_answers,
                    verbose=1,
                    epochs=configs['num_epochs'],
                    batch_size=configs['batch_size'],
                    validation_data=([X_val_questions, X_val_images], Y_val_answers),
                    callbacks=[max_accuracy, min_loss]
                    )
end_time = time.time()
results.history['start_time'] = start_time
results.history['end_time'] = end_time
Path(configs['path_histories']).mkdir(parents=True, exist_ok=True)
save_pickle_data(results.history, configs['path_histories'] + '{0}_Epochs.pickle'.format(configs['num_epochs']))
gc.collect()


# In[64]:


# model.load_weights(configs['path_image_model'] + configs['chosen_datasets_str'] + '_100_Epochs_Max_Accuracy.h5')


# In[65]:


# history = load_pickle_data(configs['path_histories'] + '100_Epochs.pickle')
# configs['num_epochs'] = len(history['loss'])

# fig = plt.figure(figsize=(20, 20))

# plt.subplot(2, 2, 1)
# plt.plot(range(configs['num_epochs']), history['loss'])
# plt.title('Train Loss')
# plt.grid()

# plt.subplot(2, 2, 2)
# plt.plot(range(configs['num_epochs']), history['accuracy'])
# plt.title('Train Accuracy')

# plt.grid()

# plt.subplot(2, 2, 3)
# plt.plot(range(configs['num_epochs']), history['val_loss'])
# plt.title('Validation Loss')

# plt.grid()

# plt.subplot(2, 2, 4)
# plt.plot(range(configs['num_epochs']), history['val_accuracy'])
# plt.title('Validation Accuracy')

# plt.grid()
# plt.savefig(configs['path_plots'] + 'Train-Val-Loss-Accuracy.png')

# plt.show()


# In[66]:


def calculate_accuracy(data, X_questions, X_images, model, index_to_answer):
    total = collections.defaultdict(int)
    corrects = collections.defaultdict(int)


    ans_types = ['number', 'yes/no', 'binary', 'others_single_word', 'others_multiple_words']

    y_pred = model.predict([X_questions, X_images])
    y_pred = np.argmax(y_pred, axis=1)

    for i in range(len(data)):
        d = data[i]
        d['prediction'] = index_to_answer[y_pred[i]]
        prediction = d['prediction']
        ans = d['answer']
        ans_list = ans.split(' ')

        if len(ans_list) == 1:
            ans = ans_list[0]

            if ans.isnumeric():
                total['number'] += 1
                if ans == prediction:
                    corrects['number'] += 1
            
            elif ans in ['yes', 'no']:
                total['yes/no'] += 1
                if ans == prediction:
                    corrects['yes/no'] += 1
            
            else:
                total['others_single_word'] += 1
                if ans == prediction:
                    corrects['others_single_word'] += 1
        
        else:
            total['others_multiple_words'] += 1
            if d['answer'] == prediction:
                corrects['others_multiple_words'] += 1

    print('Yes or no: {0} of {1}, Accuracy: {2}'.format(corrects['yes/no'], total['yes/no'], corrects['yes/no']/total['yes/no']))
#     print('Number: {0} of {1}, Accuracy: {2}'.format(corrects['number'], total['number'], corrects['number']/total['number']))
    print('Others (Single Word): {0} of {1}, Accuracy: {2}'.format(corrects['others_single_word'], total['others_single_word'], corrects['others_single_word']/total['others_single_word']))
    print('Others (Multiple Word): {0} of {1}, Accuracy: {2}'.format(corrects['others_multiple_words'], total['others_multiple_words'], corrects['others_multiple_words']/total['others_multiple_words']))
    final_total = sum(total.values())
    final_corrects = sum(corrects.values())

    print('Final: {0} of {1}, Accuracy: {2}'.format(final_corrects, final_total, final_corrects/final_total))


# In[67]:


calculate_accuracy(train_data, X_train_questions, X_train_images, model, index_to_answer)


# In[68]:


calculate_accuracy(val_data, X_val_questions, X_val_images, model, index_to_answer)


# In[69]:


import tensorflow as tf
import colorsys
from PIL import Image


# In[70]:


def read_class_names(class_file_name):
    names = {}
    with open(class_file_name, 'r') as data:
        for ID, name in enumerate(data):
            names[ID] = name.strip('\n')
    return names


# In[71]:


def draw_bbox(image, bboxes, classes=read_class_names(configs['path_image_model'] + 'YOLOv4' + configs['cdsign'] + 'coco.names'), show_label=True):
    num_classes = len(classes)
    image_h, image_w, _ = image.shape
    hsv_tuples = [(1.0 * x / num_classes, 1., 1.) for x in range(num_classes)]
    colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
    colors = list(map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)), colors))

    random.seed(0)
    random.shuffle(colors)
    random.seed(None)

    out_boxes, out_scores, out_classes, num_boxes = bboxes
    for i in range(num_boxes[0]):
        if int(out_classes[0][i]) < 0 or int(out_classes[0][i]) > num_classes: continue
        coor = out_boxes[0][i]
        coor[0] = int(coor[0] * image_h)
        coor[2] = int(coor[2] * image_h)
        coor[1] = int(coor[1] * image_w)
        coor[3] = int(coor[3] * image_w)

        fontScale = 0.5
        score = out_scores[0][i]
        class_ind = int(out_classes[0][i])
        bbox_color = colors[class_ind]
        bbox_thick = int(0.6 * (image_h + image_w) / 600)
        c1, c2 = (coor[1], coor[0]), (coor[3], coor[2])
        cv2.rectangle(image, c1, c2, bbox_color, bbox_thick)

        if show_label:
            bbox_mess = '%s: %.2f' % (classes[class_ind], score)
            t_size = cv2.getTextSize(bbox_mess, 0, fontScale, thickness=bbox_thick // 2)[0]
            c3 = (c1[0] + t_size[0], c1[1] - t_size[1] - 3)
            cv2.rectangle(image, c1, (np.float32(c3[0]), np.float32(c3[1])), bbox_color, -1) #filled

            cv2.putText(image, bbox_mess, (c1[0], np.float32(c1[1] - 2)), cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale, (0, 0, 0), bbox_thick // 2, lineType=cv2.LINE_AA)
    return image


# In[72]:


def draw_bounding_box(image_path):
    original_image = cv2.imread(image_path)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    image_data = cv2.resize(original_image, (448, 448))
    image_data = image_data / 255.
    images_data = []
    images_data.append(image_data)
    images_data = np.asarray(images_data).astype(np.float32)

    yolo_model = tf.saved_model.load(configs['path_image_model'] + 'YOLOv4', tags=[tf.compat.v1.saved_model.tag_constants.SERVING])
    
    infer = yolo_model.signatures['serving_default']
    batch_data = tf.constant(images_data)
    pred_bbox = infer(batch_data)

    for key, value in pred_bbox.items():
        boxes = value[:, :, 0:4]
        pred_conf = value[:, :, 4:]
        
    boxes, scores, classes, valid_detections = tf.image.combined_non_max_suppression(
        boxes=tf.reshape(boxes, (tf.shape(boxes)[0], -1, 1, 4)),
        scores=tf.reshape(
            pred_conf, (tf.shape(pred_conf)[0], -1, tf.shape(pred_conf)[-1])),
            max_output_size_per_class=50,
            max_total_size=50,
            iou_threshold=0.45,
            score_threshold=0.25
        )
    
    pred_bbox = [boxes.numpy(), scores.numpy(), classes.numpy(), valid_detections.numpy()]
    image = draw_bbox(original_image, pred_bbox)
    image = Image.fromarray(image.astype(np.uint8))
    return image
    


# In[73]:


def predict(image_path, question, model, configs, word_to_index, image_model, nltk, index_to_answer, view=5):
    data = {}
    data['tokens'] = nltk.word_tokenize(question.lower())
    data = [data]
    data = vectorize_tokens(data, word_to_index)
    X_image = np.expand_dims(get_features(image_path, image_model), axis=0)
    X_question = np.array([d['vector'] for d in data], dtype=np.float32)
    
    plt.imshow(draw_bounding_box(image_path))
    
    y_predict = model.predict(x=[X_question, X_image])
    y_predict_list = list(y_predict[0])
    y_predict_sorted = sorted(y_predict_list, reverse=True)
    
    for i in range(view):
        prob = y_predict_sorted[i]
        index = y_predict_list.index(prob)
        label = index_to_answer[index]
        print('{0} % {1}'.format(str(prob)[:5], label))


# In[74]:


image_model = get_image_model(configs)


# In[75]:


question = 'what is he typing with?'
image_path = configs['path_test_images'] + '11.jpg'
predict(image_path, question, model, configs, word_to_index, image_model, nltk, index_to_answer)



# %%
import nltk
from nltk.tokenize import word_tokenize
from nltk.text import Text
from nltk.corpus import stopwords

import multiprocessing as mp
from tqdm import tqdm
import time

# %%
# download packages
# nltk.download('stopwords')

# %%
def filter_slave(tokens, stopwords, task_idx):
        with tqdm(total=len(tokens), ncols=100, desc=f"task: {task_idx}", position=task_idx, leave=True) as pbar:
            filtered = []
            for w in tokens:
                if w not in stopwords:
                    filtered.append(w)
                pbar.update()
        return filtered

def filter_master(tokens):
    num_cores = int(mp.cpu_count())
    pool = mp.Pool(num_cores)
    num_tasks = 8
    task_size = len(tokens) // num_tasks
    print("Start eliminating stopwords...")
    print("total number of tokens:", len(tokens))
    print("task size:", task_size)
    print("number of tasks:", num_tasks)
    print("start filtering...")

    t_begin = time.time()
    results = [
        pool.apply_async(filter_slave,
                            args=(tokens[task_idx * task_size: min(len(tokens), (task_idx+1) * task_size)],
                                stopwords.words('english'), task_idx,))
        for task_idx in range(num_tasks)
    ]
    pool.close()
    pool.join()
    t_end = time.time()
    print(f"Done. Time used: {t_end - t_begin}s")

    return results

# %%
if __name__ == '__main__':

    # %%
    # read text
    with open("Sherlock_Holmes.txt", "r") as f:
        content = f.read()

    # %%
    # preprocess
    content = content.lower()
    puncts = '\\\'~`!@#$%^&*()-_=+[]{}|;:",./<>?'
    for char in puncts:
        content = content.replace(char, ' ')

    # %%
    # tokenize
    tokens = word_tokenize(content)

    # %%
    # eliminate stopwords
    stopwords = stopwords.words('english')
    # filtered = [w for w in tokens if w not in stopwords]
    filtered = []
    for i, w in enumerate(tokens):
        if w not in stopwords:
            filtered.append(w)
        print(f"{i}/{len(tokens)}", end='\r')


    # %%
    # mp stopwords
    # results = filter_master(tokens)

    # %%
    # filtered = []
    # for i in range(8):
    #     filtered.extend(results[i].get())

    # %%
    text = Text(tokens)

import googlesearch as engine 
import pandas as pd 
import numpy as np 
import pickle 
from tqdm import tqdm 
import os

def main():
    try:
        os.mkdir('Jobs2')
    except Exception as e:
        pass

    places = list(
        pd.read_csv(
            r'ds\places.csv'
        ).place.unique()
    ) 

    batch_init = 1857 + 32
    batches = 100
    batch_size = int(np.ceil(len(places)/batches))  
    

    link_counter = 1856+33
    for batch in range(60, 101, 1):

        reviews = []
        for place in tqdm(places[batch_init:batch_init+batch_size]): 
            

            pause = np.random.randint(1, 3)

            print(f' requesting link for {place}\n')

            link = next(
                engine.search(
                    query = f'{place} tripadvisor review', 
                    start = 0, 
                    stop = 1, 
                    pause = pause
                )
            ) 
            

            print(f'Link {link_counter} caught. ')
            link_counter += 1
            reviews.append(link)

        file = open(f'./Jobs2/links{batch+1}.pkl', 'wb') 
        pickle.dump(reviews, file)
        file.close()

        batch_init += batch_size

if __name__ == '__main__':
    main()
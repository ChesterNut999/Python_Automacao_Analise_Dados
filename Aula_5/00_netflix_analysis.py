### LIBRIRIES
import pandas as pd

### PANDAS PARAMETERS
pd.options.display.max_rows = 1000
pd.options.mode.chained_assignment = None  # default='warn'

### FUNCTIONS
def fn_read_file():

    dir = "./dataset/"
    file_name = "netflix_titles.csv"

    source = pd.read_csv(dir + file_name,
                        float_precision = "round_trip",
                        date_format = "%d/%m/%Y",
                        dayfirst = True,
                        encoding = "utf-8",
                        skipinitialspace = True,
                        skip_blank_lines = True)
    
    return source

def fn_process_file(file):

    df = pd.DataFrame(file)
    
    df = df.drop(['show_id', 'Unnamed: 12'], axis = 1)\
           .drop_duplicates()
    
    df = df.rename({'rating': 'parental_guidelines'}, axis = 1)

    ### ------------------------------------------------------------------------------------

    df['director'] = df['director'].fillna('n/a')\
                                   .str.strip()

    df['cast'] = df['cast'].fillna('n/a')\
                           .str.strip()

    df['country'] = df['country'].replace([r'^, |\s+\"', r'^, | \s'], '', regex = True)\
                                 .replace([r'^,|\s+\"'], '', regex = True)\
                                 .replace(' ', '')\
                                 .fillna('n/a')\
                                 .str.strip()
        
    df['date_added'] = pd.to_datetime(df['date_added'],
                                      format = 'mixed',
                                      yearfirst = True)

    df['release_year'] = df['release_year'].astype(int)

    df['parental_guidelines'] = df['parental_guidelines'].replace(['PG-13'], '13+')\
                                                         .replace(['TV-MA', 'R', 'NC-17'], '17+')\
                                                         .replace(['PG'], '15+')\
                                                         .replace(['TV-14'], '14+')\
                                                         .replace(['TV-PG'], '10+')\
                                                         .replace(['TV-Y'], '6+')\
                                                         .replace(['TV-Y7', 'TV-Y7-FV'], '7+')\
                                                         .replace(['TV-G', 'G'], 'General Audience')\
                                                         .replace(['NR', 'UR'], 'No Rated/Unrated')\
                                                         .replace(['A'], '18+')\
                                                         .str.strip()
    
    df['duration'] = df['duration'].fillna('n/a')\
                                   .str.strip()
    
    df['listed_in'] = df['listed_in'].fillna('n/a')\
                                     .replace([' ', '"'], '')

    ### SIGN DATAFRAME
    df = df

    return df

def fn_analysis(data):

    ### ------------------------------------------------------------------------------------
    ### (PT-BR) Qual a qtd. total_movies de filmes produzidos anualmente por cada país desconsiderando co-produções?
    ### (ENG) WHAT IS THE total_movies AMOUNT OF FILMS PRODUCED ANNUALLY BY EACH COUNTRY DISREGARDING COPRODUCTIONS?

    df_movie_by_country = data[['country', 'type', 'release_year']]
    
    df_movie_by_country = df_movie_by_country.groupby(['country', 'release_year'], as_index = False)['type']\
                                             .count()\
                                             .sort_values(['country', 'release_year'], ascending = True)
    
    df_movie_by_country = df_movie_by_country[~df_movie_by_country['country'].str.contains(',')]

    # print('\n', df_movie_by_country)

    ### ------------------------------------------------------------------------------------
    ### (PT-BR) Quais as faixas etárias do controle parental que se destacam e quantos filmes foram produzidos para cada uma delas?
    ### (ENG) WHICH ARE THE AGE GROUPS (PARENTAL CONTROL) THAT STAND OUT AMONG ALL THE FILMS PRODUCED?

    df_parental_guidelines = data[['parental_guidelines']]

    df_parental_guidelines['total_movies'] = ''

    df_parental_guidelines = df_parental_guidelines.groupby(['parental_guidelines', 'total_movies'], as_index = False)['total_movies']\
                                                   .count()\
                                                   .sort_values(['total_movies'], ascending = False)\
                                                   .reindex([4, 2, 0, 1, 7, 6, 3, 8, 9, 5])\
                                                   .reset_index()\
                                                   .drop(['index'], axis = 1)
    
    # df_parental_guidelines = df_parental_guidelines[df_parental_guidelines.index < 5]

    df_parental_guidelines = df_parental_guidelines[['total_movies', 'parental_guidelines']]

    # print('\n', df_parental_guidelines)                                                 

    ### ------------------------------------------------------------------------------------
    
    return df_movie_by_country, df_parental_guidelines

def fn_store_data(analysis):

    df_movie_by_country, df_parental_guidelines = analysis

    dir = "./dataset/"
    file_name_1 = "df_movie_by_country.csv"
    file_name_2 = "df_parental_guidelines.csv"

    df_movie_by_country.to_csv(dir + file_name_1, index = False)
    df_parental_guidelines.to_csv(dir + file_name_2, index = False)
    
    return print('\nTASKS FINISHED! CHECK THE FILES IN THE OUTPUT DIRECTORY!\n')

### EXEC.
if __name__ == "__main__":

    file = fn_read_file()

    data = fn_process_file(file)

    analysis = fn_analysis(data)

    store = fn_store_data(analysis)
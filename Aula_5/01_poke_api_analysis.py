### LIBRARIES
import urllib3
import json

### GLOBAL OBJECTS
http = urllib3.PoolManager()
pokemon_name_list = []
pokemon_url_list = []
pokemon_specs_list = []

### FUNCTIONS
def fn_request_pokemon_name():

    poke_api_url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"   

    ### REQUEST_ALL_DATA
    poke_api_request = http.request("GET", poke_api_url)
    poke_api_resp = poke_api_request.data
    poke_api_resp = json.loads(poke_api_resp)
    poke_api_resp = poke_api_resp['results']

    # print(poke_api_resp)

    ### POKEMON NAME FILTER
    for pokemon_name in poke_api_resp:
        pokemon_name_list.append(pokemon_name['name'])
        pokemon_name_list.sort()
    
    return pokemon_name_list

def fn_request_pokemon_specs():

    poke_api_url = "https://pokeapi.co/api/v2/pokemon/"   

    for pokemon_name in pokemon_name_list:
        pokemon_url_list.append(poke_api_url + pokemon_name)
        pokemon_url_list.sort()
    
    # print(pokemon_url_list)

    for i in pokemon_url_list:
        poke_api_request = http.request("GET", i)
        poke_api_resp = poke_api_request.data
        poke_api_resp = json.loads(poke_api_resp)
        poke_api_resp = poke_api_resp

        pokemon_specs_list.append(poke_api_resp)

    print(pokemon_specs_list)

    return pokemon_specs_list

### EXEC.
if __name__ == "__main__":

    fn_request_pokemon_name()

    fn_request_pokemon_specs()